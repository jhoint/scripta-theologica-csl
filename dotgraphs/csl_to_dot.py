"""
csl_to_dot.py
Genera grafos DOT de dependencias entre macros de un archivo CSL.

Uso:
  python csl_to_dot.py <archivo.csl> <salida.dot> [citation|bibliography] [--leaves]

Si se omite el tercer argumento, se incluyen ambos puntos de entrada.
Además del grafo detallado, genera automáticamente un grafo de vista general
inter-cluster con el sufijo -overview.dot/.svg.

Tipos de nodo:
  - Elipse azul/verde        : <citation> / <bibliography>
  - Hexágono amarillo        : macro condicional (contiene <choose>)
  - Caja redondeada naranja  : macro terminal (emite variables, no llama macros)
  - Caja blanca              : macro agregadora (llama otras macros, sin <choose>)
  - Óvalo gris               : variable CSL (solo con --leaves)
  - Óvalo rosa               : término CSL  (solo con --leaves)

Clusters (fondo de color):
  Nombres · Títulos · Fechas · Fuente · Notas · Bibliografía · Otros

Aristas:
  - Continua   : llamada normal
  - Discontinua: llamada desde <substitute> (fallback)
"""

import sys
import os
import xml.etree.ElementTree as ET
from collections import defaultdict, deque

NS = "http://purl.org/net/xbiblio/csl"

# ---------------------------------------------------------------------------
# Familias de macros según esquema CMOS 18 §1-§5
# Tupla: (id, lista_de_prefijos, etiqueta, color_fondo)
# Orden importa: prefijos más específicos primero.
# Las macros legal-* se excluyen del grafo por completo.
# ---------------------------------------------------------------------------
CLUSTERS = [
    # §1 Autor
    ("c1_author",    ["author"],
                     "§1 Autor",              "#D6EAF8"),
    # §2 Fecha (standalone)
    ("c2_date",      ["date"],
                     "§2 Fecha",              "#D1F8F5"),
    # §3.1 Título
    ("c3_title",     ["title"],
                     "§3.1 Título",           "#FEF9E7"),
    # §3.2 Descripción
    ("c3_desc",      ["description"],
                     "§3.2 Descripción",      "#FEF3E2"),
    # §3.3 Identificadores (edición, colaboradores, volumen)
    ("c3_ident",     ["identifier"],
                     "§3.3 Identificadores",  "#FDEBD0"),
    # Etiquetas (helpers transversales, término/label CSL)
    ("c_label",      ["label"],
                     "Etiquetas",             "#F2F3F4"),
    # §4.1 Fuente serial
    ("c4_serial",    ["source-serial"],
                     "§4.1 Serial",           "#EBF5EB"),
    # §4.2 Fuente monográfica
    ("c4_mono",      ["source-monographic"],
                     "§4.2 Monográfico",      "#D5F5E3"),
    # §4.3+4.4 Serie y evento
    ("c4_series_ev", ["source-series", "source-event"],
                     "§4.3-4 Serie/Evento",   "#ABEBC6"),
    # §4.9+4.10 Archivo y URL/DOI  ← debe ir ANTES de source-date para
    #           capturar source-date-accessed-* correctamente
    ("c4_arch_url",  ["source-archive", "source-DOI-URL", "source-date-accessed"],
                     "§4.9-10 Arch./URL",     "#B2DFDB"),
    # §4.5+4.6 Editor y fecha de fuente
    ("c4_pub_date",  ["source-publication", "source-date"],
                     "§4.5-6 Editor/Fecha",   "#C8E6C9"),
    # §4.7+4.8 Localizador y medio
    ("c4_loc_med",   ["source-locator", "source-medium"],
                     "§4.7-8 Loc./Medio",     "#A9DFBF"),
    # §4 Fuente (general — captura source-bib, source-note, etc.)
    ("c4_source",    ["source"],
                     "§4 Fuente (gen.)",      "#F0FFF4"),
    # §5 Notas y citas
    ("c5_notes",     ["bibliography-notes", "citation-notes", "citation-short"],
                     "§5 Notas/Citas",        "#F5EEF8"),
    # Resto no clasificado
    ("other",        [],
                     "Otros",                 "#F8F9FA"),
]

LEGAL_PREFIX = "legal"


def is_legal(name):
    """True si la macro pertenece al bloque de referencias legales."""
    return name == LEGAL_PREFIX or name.startswith(LEGAL_PREFIX + "-")


def assign_cluster(name):
    for cluster_id, prefixes, _label, _color in CLUSTERS:
        if cluster_id == "other" or not prefixes:
            continue
        for p in prefixes:
            if name == p or name.startswith(p + "-") or name.startswith(p + "_"):
                return cluster_id
    return "other"


# ---------------------------------------------------------------------------
# Helpers de XML
# ---------------------------------------------------------------------------

def tag(name):
    return f"{{{NS}}}{name}"


def has_choose(element):
    return element.find(f".//{tag('choose')}") is not None


def _is_inside_substitute(root_el, target_el):
    for subst_el in root_el.iter(tag("substitute")):
        for desc in subst_el.iter():
            if desc is target_el:
                return True
    return False


def find_macro_calls(element):
    """Devuelve (normal_calls, substitute_calls)."""
    normal = set()
    subst  = set()
    for el in element.iter():
        macro_attr = el.get("macro")
        if not macro_attr:
            continue
        if _is_inside_substitute(element, el):
            subst.add(macro_attr)
        else:
            normal.add(macro_attr)
    return normal, subst


def find_variable_leaves(element):
    variables = set()
    for el in element.iter():
        if el.get("macro"):
            continue
        var = el.get("variable")
        if var:
            for v in var.split():
                variables.add(v)
    return variables


def find_term_leaves(element):
    terms = set()
    for el in element.iter(tag("text")):
        t = el.get("term")
        if t:
            terms.add(t)
    for el in element.iter(tag("label")):
        t = el.get("variable")
        if t:
            terms.add(f"[label:{t}]")
    return terms


# ---------------------------------------------------------------------------
# Clasificación de macros
# ---------------------------------------------------------------------------

def classify_macro(macro_el, deps_normal, deps_subst):
    name = macro_el.get("name")
    all_deps = deps_normal.get(name, set()) | deps_subst.get(name, set())
    if has_choose(macro_el):
        return "conditional"
    if not all_deps:
        return "terminal"
    return "aggregator"


# ---------------------------------------------------------------------------
# Paleta y formas
# ---------------------------------------------------------------------------

COLOR = {
    "entry_citation":     "#AED6F1",
    "entry_bibliography": "#A9DFBF",
    "conditional":        "#FFF2CC",
    "terminal":           "#FCE5CD",
    "aggregator":         "#FFFFFF",
    "variable":           "#E8E8E8",
    "term":               "#FADBD8",
}

SHAPE = {
    "conditional": "hexagon",
    "terminal":    "box",
    "aggregator":  "box",
    "variable":    "oval",
    "term":        "oval",
}


def safe_id(name):
    return (name.replace("-", "_").replace(" ", "_")
                .replace(":", "_").replace("[", "_").replace("]", "_"))


# ---------------------------------------------------------------------------
# BFS de profundidades
# ---------------------------------------------------------------------------

def bfs_depths(root_macros, deps_normal, deps_subst, all_used):
    depth = {}
    queue = deque()
    for m in root_macros:
        if m in all_used and m not in depth:
            depth[m] = 1
            queue.append(m)
    while queue:
        name = queue.popleft()
        children = (deps_normal.get(name, set()) | deps_subst.get(name, set())) & all_used
        for child in children:
            if child not in depth:
                depth[child] = depth[name] + 1
                queue.append(child)
    return depth


# ---------------------------------------------------------------------------
# Grafo detallado con clusters
# ---------------------------------------------------------------------------

def build_dot(
    all_used, macro_defs, deps_normal, deps_subst,
    citation_calls, biblio_calls,
    include_leaves, entry_filter, graph_title
):
    macro_class = {}
    for name in all_used:
        macro_class[name] = (
            classify_macro(macro_defs[name], deps_normal, deps_subst)
            if name in macro_defs else "aggregator"
        )

    # Agrupar por cluster
    by_cluster = defaultdict(list)
    for name in sorted(all_used):
        by_cluster[assign_cluster(name)].append(name)

    # Hojas opcionales
    var_leaves  = set()
    term_leaves = set()
    if include_leaves:
        for name in all_used:
            if name in macro_defs:
                el = macro_defs[name]
                var_leaves  |= find_variable_leaves(el)
                term_leaves |= find_term_leaves(el)

    lines = []
    lines.append(f'digraph CSL_Macros {{')
    lines.append(f'    label="{graph_title}";')
    lines.append('    labelloc=t;')
    lines.append('    rankdir=LR;')
    lines.append('    concentrate=true;')
    lines.append('    splines=curved;')
    lines.append('    fontname="Helvetica"; fontsize=13;')
    lines.append('    node [fontname="Helvetica", fontsize=10];')
    lines.append('    edge [fontname="Helvetica", fontsize=8, arrowsize=0.6];')
    lines.append("")

    # Leyenda
    lines.append('    subgraph cluster_legend {')
    lines.append('        label="Leyenda"; style=dotted; fontsize=9; rank=sink;')
    lines.append(f'        _L_entry [label="<citation>\\n<bibliography>", shape=ellipse, style=filled, fillcolor="{COLOR["entry_citation"]}", fontsize=8];')
    lines.append(f'        _L_cond  [label="Condicional\\n(con <choose>)", shape=hexagon, style=filled, fillcolor="{COLOR["conditional"]}", fontsize=8];')
    lines.append(f'        _L_term  [label="Terminal\\n(solo variables)", shape=box, style="filled,rounded", fillcolor="{COLOR["terminal"]}", fontsize=8];')
    lines.append(f'        _L_aggr  [label="Agregadora\\n(llama macros)", shape=box, style=filled, fillcolor="{COLOR["aggregator"]}", fontsize=8];')
    lines.append('        _L_norm  [label="llamada normal", shape=plaintext, fontsize=8];')
    lines.append('        _L_sub   [label="llamada substitute", shape=plaintext, fontsize=8];')
    lines.append('        _L_norm -> _L_sub [style=dashed, color=gray, arrowsize=0.5];')
    lines.append('    }')
    lines.append("")

    # Puntos de entrada
    entry_ids = []
    if entry_filter in (None, "citation"):
        lines.append(f'    __citation__ [label="<citation>", shape=ellipse, style=filled, fillcolor="{COLOR["entry_citation"]}"];')
        entry_ids.append("__citation__")
    if entry_filter in (None, "bibliography"):
        lines.append(f'    __bibliography__ [label="<bibliography>", shape=ellipse, style=filled, fillcolor="{COLOR["entry_bibliography"]}"];')
        entry_ids.append("__bibliography__")
    if entry_ids:
        lines.append(f'    {{ rank=same; {" ".join(entry_ids)} }}')
    lines.append("")

    # Clusters con sus nodos
    for cluster_id, _prefixes, label, bg_color in CLUSTERS:
        members = by_cluster.get(cluster_id, [])
        if not members:
            continue
        lines.append(f'    subgraph cluster_{cluster_id} {{')
        lines.append(f'        label="{label}"; style=filled; fillcolor="{bg_color}";')
        lines.append( '        fontname="Helvetica"; fontsize=11; fontcolor="#444444";')
        for name in members:
            sid   = safe_id(name)
            cls   = macro_class[name]
            color = COLOR[cls]
            shape = SHAPE[cls]
            extra = ', style="filled,rounded"' if cls == "terminal" else ", style=filled"
            lines.append(f'        {sid} [label="{name}", shape={shape}{extra}, fillcolor="{color}"];')
        lines.append('    }')
        lines.append("")

    # Hojas
    if include_leaves:
        lines.append('    subgraph cluster_leaves {')
        lines.append('        label="Variables / Términos"; style=dotted;')
        for v in sorted(var_leaves):
            sid = "VAR_" + safe_id(v)
            lines.append(f'        {sid} [label="{v}", shape=oval, style=filled, fillcolor="{COLOR["variable"]}", fontsize=8];')
        for t in sorted(term_leaves):
            sid = "TERM_" + safe_id(t)
            lines.append(f'        {sid} [label="{t}", shape=oval, style=filled, fillcolor="{COLOR["term"]}", fontsize=8];')
        lines.append('    }')
        lines.append("")

    # Aristas desde puntos de entrada
    for m in sorted(citation_calls):
        if m in all_used:
            lines.append(f'    __citation__ -> {safe_id(m)};')
    for m in sorted(biblio_calls):
        if m in all_used:
            lines.append(f'    __bibliography__ -> {safe_id(m)};')
    lines.append("")

    # Aristas entre macros
    for name in sorted(all_used):
        src = safe_id(name)
        for child in sorted(deps_normal.get(name, set())):
            if child in all_used:
                lines.append(f'    {src} -> {safe_id(child)};')
    for name in sorted(all_used):
        src = safe_id(name)
        for child in sorted(deps_subst.get(name, set())):
            if child in all_used:
                lines.append(f'    {src} -> {safe_id(child)} [style=dashed, color="#AAAAAA"];')

    # Aristas hacia hojas
    if include_leaves:
        lines.append("")
        for name in sorted(all_used):
            if name not in macro_defs:
                continue
            el  = macro_defs[name]
            src = safe_id(name)
            for v in sorted(find_variable_leaves(el)):
                lines.append(f'    {src} -> VAR_{safe_id(v)} [color="#BBBBBB", style=dotted, arrowsize=0.4];')
            for t in sorted(find_term_leaves(el)):
                lines.append(f'    {src} -> TERM_{safe_id(t)} [color="#FFAAAA", style=dotted, arrowsize=0.4];')

    lines.append("}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Grafo de vista general inter-cluster
# ---------------------------------------------------------------------------

def build_overview_dot(
    all_used, deps_normal, deps_subst,
    citation_calls, biblio_calls,
    entry_filter, graph_title
):
    cluster_of = {name: assign_cluster(name) for name in all_used}

    # Aristas inter-cluster (contadas)
    inter = defaultdict(int)
    for name in all_used:
        sc = cluster_of[name]
        for child in (deps_normal.get(name, set()) | deps_subst.get(name, set())):
            if child in all_used:
                dc = cluster_of[child]
                if sc != dc:
                    inter[(sc, dc)] += 1

    # Aristas desde puntos de entrada
    entry_edges = defaultdict(int)
    for m in citation_calls:
        if m in all_used:
            entry_edges[("__citation__", cluster_of[m])] += 1
    for m in biblio_calls:
        if m in all_used:
            entry_edges[("__bibliography__", cluster_of[m])] += 1

    active = set(cluster_of.values())

    lines = []
    lines.append('digraph CSL_Overview {')
    lines.append(f'    label="{graph_title} — vista general";')
    lines.append('    labelloc=t;')
    lines.append('    rankdir=LR;')
    lines.append('    splines=ortho;')
    lines.append('    fontname="Helvetica"; fontsize=13;')
    lines.append('    node [fontname="Helvetica", fontsize=11];')
    lines.append('    edge [fontname="Helvetica", fontsize=9];')
    lines.append("")

    if entry_filter in (None, "citation"):
        lines.append(f'    __citation__ [label="<citation>", shape=ellipse, style=filled, fillcolor="{COLOR["entry_citation"]}"];')
    if entry_filter in (None, "bibliography"):
        lines.append(f'    __bibliography__ [label="<bibliography>", shape=ellipse, style=filled, fillcolor="{COLOR["entry_bibliography"]}"];')
    lines.append("")

    for cluster_id, _prefixes, label, bg_color in CLUSTERS:
        if cluster_id not in active:
            continue
        count = sum(1 for n in all_used if cluster_of[n] == cluster_id)
        lines.append(f'    OV_{cluster_id} [label="{label}\\n({count} macros)", shape=box, style=filled, fillcolor="{bg_color}", width=2.0];')
    lines.append("")

    for (src, dst), cnt in sorted(entry_edges.items()):
        lines.append(f'    {src} -> OV_{dst} [xlabel="{cnt}"];')
    for (src, dst), cnt in sorted(inter.items()):
        lines.append(f'    OV_{src} -> OV_{dst} [xlabel="{cnt}"];')

    lines.append("}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main(csl_path, dot_path, entry_filter=None, include_leaves=False):
    tree = ET.parse(csl_path)
    root = tree.getroot()

    macro_defs = {}
    for macro in root.findall(tag("macro")):
        name = macro.get("name")
        if name:
            macro_defs[name] = macro

    deps_normal = defaultdict(set)
    deps_subst  = defaultdict(set)
    for name, macro_el in macro_defs.items():
        n, s = find_macro_calls(macro_el)
        deps_normal[name] = n
        deps_subst[name]  = s

    citation_el = root.find(tag("citation"))
    biblio_el   = root.find(tag("bibliography"))
    citation_calls, _ = (find_macro_calls(citation_el)
                         if citation_el is not None and entry_filter in (None, "citation")
                         else (set(), set()))
    biblio_calls, _   = (find_macro_calls(biblio_el)
                         if biblio_el is not None and entry_filter in (None, "bibliography")
                         else (set(), set()))

    root_macros = citation_calls | biblio_calls

    def collect_used(name, visited):
        if name in visited:
            return
        visited.add(name)
        for child in (deps_normal.get(name, set()) | deps_subst.get(name, set())):
            collect_used(child, visited)

    all_used = set()
    for m in root_macros:
        collect_used(m, all_used)

    # Excluir macros legales del grafo
    all_used = {n for n in all_used if not is_legal(n)}

    titles = {
        "citation":     "CSL Citation",
        "bibliography": "CSL Bibliography",
        None:           "CSL Macros (Citation + Bibliography)",
    }
    title = titles[entry_filter]

    # Grafo detallado
    dot_content = build_dot(
        all_used, macro_defs, deps_normal, deps_subst,
        citation_calls, biblio_calls,
        include_leaves, entry_filter, title
    )
    with open(dot_path, "w", encoding="utf-8") as f:
        f.write(dot_content)

    # Grafo de vista general (mismo nombre, sufijo -overview)
    base, ext = os.path.splitext(dot_path)
    overview_path = base + "-overview" + ext
    ov_content = build_overview_dot(
        all_used, deps_normal, deps_subst,
        citation_calls, biblio_calls,
        entry_filter, title
    )
    with open(overview_path, "w", encoding="utf-8") as f:
        f.write(ov_content)

    # Estadísticas por cluster
    n_cond = sum(1 for n in all_used if n in macro_defs and has_choose(macro_defs[n]))
    n_term = sum(1 for n in all_used if n in macro_defs
                 and not (deps_normal.get(n) or deps_subst.get(n))
                 and not has_choose(macro_defs[n]))
    print(f"DOT generado  : {dot_path}")
    print(f"Overview      : {overview_path}")
    print(f"Filtro        : {entry_filter or 'ambos'}")
    print(f"Total macros  : {len(all_used)}  (condicionales={n_cond}, terminales={n_term}, agregadoras={len(all_used)-n_cond-n_term})")
    by_cl = defaultdict(int)
    for n in all_used:
        by_cl[assign_cluster(n)] += 1
    for cid, _p, _lbl, _c in CLUSTERS:
        if by_cl[cid]:
            print(f"  {_lbl:<30}: {by_cl[cid]} macros")


if __name__ == "__main__":
    if len(sys.argv) not in (3, 4, 5):
        print("Uso: python csl_to_dot.py <archivo.csl> <salida.dot> [citation|bibliography] [--leaves]")
        sys.exit(1)
    entry  = None
    leaves = False
    for arg in sys.argv[3:]:
        if arg == "--leaves":
            leaves = True
        elif arg in ("citation", "bibliography"):
            entry = arg
        else:
            print(f"Argumento desconocido: {arg}")
            sys.exit(1)
    main(sys.argv[1], sys.argv[2], entry, leaves)

