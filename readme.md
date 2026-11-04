# Scripta Theologica CSL

Hoja de estilos CSL (*Citation Style Language*) adaptada a las normas de edición de la revista **Scripta Theologica** (Facultad de Teología, Universidad de Navarra).

> **Nota:** Este proyecto es un desarrollo independiente, en uso y en fase de pruebas y optimización, para flujos de trabajo con Zotero, Obsidian y Pandoc. Los cambios, versión a versión, están en [`CHANGELOG.md`](CHANGELOG.md).

---

## Archivos del repositorio

* `scripta-theologica.csl`: el estilo (versión 0.2.0).
* `CHANGELOG.md`: historial de cambios.
* `cambios-a-realizar.md`: pendientes y puntos por decidir.
* `CAMPOS.md`: guía de campos de Zotero: qué campos de cada tipo llegan a la cita y a la bibliografía, y qué se puede escribir en Extra.
* `OBRAS-CLASICAS.md`: guía detallada para citar obras clásicas y patrísticas.
* `pruebas-scripta.json`: colección de prueba con los ejemplos de las normas de la revista y algunos casos más (21 obras).
* `pruebas-tipos.json` y `pruebas-tipos.md`: 51 casos con datos ficticios, uno por cada tipo de documento más casos límite (ver [Pruebas](#pruebas)).
* `chicago-notes-bibliography.csl`: copia del estilo Chicago (notas y bibliografía), referencia para lo que las normas de la revista no regulan.
* `zotero-outputs.md`: salidas de Zotero de febrero de 2026, con el estilo en su primera versión. Es histórico: no refleja el estilo actual.

---

## Uso

### En Zotero

Instala `scripta-theologica.csl` (Editar → Ajustes → Citar → «+»). Si ya lo tenías, vuelve a instalarlo cuando cambie: Zotero usa la copia instalada, no la del repositorio.

### Con Pandoc

```text
pandoc texto.md --citeproc -M notes-after-punctuation=false \
  --bibliography=biblioteca.json --csl=scripta-theologica.csl -o texto.docx
```

`notes-after-punctuation=false` pone la llamada de nota antes del signo de puntuación, como pide la revista. Probado con Pandoc 3.8.2 y 3.13.

Sintaxis de las citas (la página, **sin «p.»**, porque el estilo imprime las páginas sin etiqueta):

| Para | Se escribe |
|---|---|
| Página | `[@clave, 45]` |
| Varias obras | `[@a, 12; @b, 30]` |
| Texto delante | `[véase @clave, 50]` |
| Obra clásica (locator entre llaves, páginas de la edición después) | `[@clave{II, 4}, 255]` |
| Dentro de una nota con texto propio | `^[Texto, véase @clave [45].]` |

---

## Tipos de documento

El estilo tiene rama propia para **los 45 tipos de CSL 1.0.2** (los 44 del Chicago oficial, 18.ª ed., más `classic`). Zotero exporta los preprints como `article` y las notas sueltas como `document`.

| Familia | Tipos CSL |
| :--- | :--- |
| Libros | `book` |
| Capítulos y comunicaciones | `chapter`, `paper-conference` |
| Revistas y prensa | `article-journal`, `article-magazine`, `article-newspaper`, `review`, `review-book` |
| Obras de consulta | `entry`, `entry-dictionary`, `entry-encyclopedia` |
| Tesis | `thesis` |
| Música | `musical_score`, `song` |
| Obras clásicas | `classic` |
| Archivo e inéditos | `personal_communication`, `manuscript`, `document`, `interview`, `speech` |
| Web | `webpage`, `post`, `post-weblog` |
| Obras independientes | `collection`, `dataset`, `graphic`, `map`, `pamphlet`, `periodical`, `report`, `software`, `standard`, `figure`, `article` |
| Audiovisuales | `broadcast`, `motion_picture`, `performance`, `event` |
| Jurídicos | `legislation`, `bill`, `regulation`, `legal_case`, `treaty`, `hearing`, `patent` |

Las normas de la revista regulan libros y monografías, capítulos de obras colectivas, artículos de revista, voces de diccionario y enciclopedia, obras clásicas y patrísticas, y dan un ejemplo de documento web. **Para los demás tipos, que las normas no regulan** (tesis y comunicaciones, partituras y grabaciones, archivo e inéditos, web, obras independientes, audiovisuales y jurídicos), el estilo se apoya en Chicago (18.ª ed.) para los elementos y su orden, y en *Scripta* para la forma: autor en versalitas, cursiva para las obras, «» para las partes.

---

## Convenciones de uso en Zotero

Para que salgan bien los casos especiales, sigue estas indicaciones al introducir los datos. La lista completa de campos que usa el estilo en cada tipo de documento está en [`CAMPOS.md`](CAMPOS.md).

### 1. Directores de obras colectivas (`dir.` / `dirs.`)
Si una obra colectiva tiene director/es en lugar de editor/es, en el campo **Extra / Adicional** de Zotero:
```text
editorial-director: Apellido || Nombre
```

### 2. Comillas dentro de un título
Escríbelas **rectas y emparejadas** (`"así"`). El estilo pone «» por fuera y “” por dentro: «Título con “comillas interiores” emparejadas». Las comillas inglesas “ ” también funcionan si están bien emparejadas y orientadas; no funcionan las «» interiores ni las comillas sueltas o al revés.

### 3. Revistas y obras de consulta
* **Revistas:** si el elemento tiene el campo *Journal Abbr* (abreviatura de la revista), el estilo la usa en lugar del título completo en las citas y en la bibliografía: «*ScrTh* 17 (1985) 227-243».
* **Voces de diccionario o enciclopedia:** Zotero no tiene campo de abreviatura para estos tipos. La sigla de la obra se escribe en **Extra**: `container-title-short: DTC`. El estilo la usa en lugar del título de la obra («en DTC 6 (1920) 1-10»), y en las citas posteriores pone el *Título corto* de la voz si lo tiene.

### 4. Archivo e inéditos
Cartas, manuscritos, documentos, entrevistas y discursos salen con el autor siempre, la fecha completa en cifras, y el archivo y la signatura a partir de los campos de archivo de Zotero (*Archive* y *Loc. in Archive*): «EJEMPLO, Ana, Carta a Carlos Ruiz, 23-3-1962, Archivo Ejemplo 087.39.128». Sin título, una carta (o un correo) toma el tipo de documento y el destinatario: «Carta a Carlos Ruiz». **Este formato es provisional**: las normas de la revista no lo regulan y está pendiente de confirmar.

### 5. Tesis
El tipo de tesis sale tal como está en el campo **Tipo** de Zotero («tesis doctoral»); el estilo no lo traduce ni pone uno por defecto.

### 6. Obras clásicas y patrísticas (`type: classic`)
Para citar fuentes antiguas o colecciones patrísticas (*Patrologia Latina*, *Patrologia Graeca*…):

1. Crea un elemento de tipo **Sección de un libro** (*Book Section*).
2. Rellena los campos así:

| Campo Zotero | Valor de ejemplo | Descripción / función |
| :--- | :--- | :--- |
| **Título** | `Historia ecclesiastica` | Título de la obra clásica. |
| **Autor** | `Rufino de Aquileya` | Autor antiguo. |
| **Serie / Colección** | `Patrologia Latina` | Nombre completo de la colección. |
| **Volumen** | `21` | Número del volumen dentro de la colección. |
| **Páginas** | `461-540` | Rango completo de páginas de la edición. |
| **Lugar** | `Paris` | Lugar de edición. |
| **Fecha** | `1849` | Año de la edición consultada. |
| **Editor** | `Domenico Vallarsi` | Editor científico de la versión. |
| **Extra / Adicional** | `type: classic`<br>`collection-title-short: PL` | **OBLIGATORIO.** Define el comportamiento especial y la sigla de la colección. |

#### Resultados (comprobados con Pandoc 3.8.2)
* **Primera cita:** RUFINO DE AQUILEYA, *Historia ecclesiastica*, I, 6: Patrologia Latina 21, 473-475.
* **Citas posteriores:** RUFINO DE AQUILEYA, *Historia ecclesiastica*, I, 7: PL 21, 477.
* **Bibliografía:** RUFINO DE AQUILEYA, *Historia ecclesiastica*, en Vallarsi, D. (ed.), Patrologia Latina 21, Paris, 1849, 461-540.

(El editor sale en la bibliografía solo si lo hay.) El pasaje (`I, 6`, `libros X-XI`) es el **locator**; las páginas de la edición van después. Más detalles en [`OBRAS-CLASICAS.md`](OBRAS-CLASICAS.md).

---

## Criterios del estilo

* **Forma abreviada** en las citas posteriores, no «Ibid.».
* **Rangos de páginas completos** (`227-243`, no `227-43`).
* **Varios autores:** hasta tres se citan todos; a partir de cuatro, el primero y «y otros» (las normas admiten ambas formas desde tres).
* **El nombre del autor se repite** en la bibliografía, sin raya.
* **Revistas:** solo el volumen, sin número de fascículo y sin coma antes de la página: «*Scripta Theologica* 17 (1985) 227-243». El número, solo si no hay volumen.
* **Enlace** solo si no hay DOI; en las notas, después de la página. Con la forma «recuperado de», sin fecha de acceso, como en el ejemplo de la revista.
* **Edición:** «2 ed. Aschaffenburg: Pattloch, 1978».
* **Obras de consulta y revistas no académicas o periódicos**, con el título de la publicación.

### Desviación consciente de las normas

Cuando el editor de la obra es el mismo autor del capítulo, las normas piden «en ID. (ed.)». El estilo **repite el nombre**: «PELLITERO, Ramiro, «Título», en PELLITERO, Ramiro (ed.), *Obra*…». Es una preferencia del autor del estilo, en línea con las ediciones recientes de Chicago; se cambiará si hace falta.

---

## Pruebas

```text
pandoc pruebas-tipos.md --citeproc -M notes-after-punctuation=false \
  --bibliography=pruebas-tipos.json --csl=scripta-theologica.csl -t plain --wrap=none
```

Con `pruebas-scripta.json` (ejemplos oficiales de la revista) se hace igual cambiando la bibliografía. Antes de publicar un cambio en el estilo conviene comparar el resultado antes y después sobre ambos archivos, y validar el `.csl` contra el esquema de CSL 1.0.2.

---

## Pendientes

Ver [`cambios-a-realizar.md`](cambios-a-realizar.md).

---

## Licencia y referencias

Desarrollado siguiendo las especificaciones oficiales de la [documentación de CSL](https://docs.citationstyles.org/). Licencia Creative Commons Attribution-ShareAlike 3.0.

Se han empleado las [Directrices para autores](https://revistas.unav.edu/index.php/scripta-theologica/about/submissions) de *Scripta Theologica* y el estilo Chicago Manual of Style, 18.ª ed. (notas y bibliografía).
