# Scripta Theologica CSL

Hoja de estilos CSL (*Citation Style Language*) adaptada a las normas de edición de la revista **Scripta Theologica** (Facultad de Teología de la Universidad de Navarra).

> **Nota:** Este proyecto es un desarrollo independiente en fase de pruebas y optimización para flujos de trabajo con Zotero, Obsidian y Pandoc.

---

## Archivos del repositorio

* `scripta-theologica.csl`: Archivo de estilo CSL (versión 1.0).
* `pruebas-scripta.json`: Colección bibliográfica de prueba con los ejemplos oficiales de la revista.
* `Lorem ipsum dolor sit amet.docx`: Documento de prueba para verificación visual de maquetación en Word.

---

## Convenciones de uso en Zotero

Para garantizar un renderizado exacto de los casos especiales exigidos por la revista, sigue estas indicaciones al introducir los datos en Zotero:

### 1. Directores de obras colectivas (`dir.` / `dirs.`)
Si una obra colectiva tiene director/es en lugar de editor/es:
* En el campo **Extra / Adicional** de Zotero, añade:
  ```text
  editorial-director: Apellido || Nombre
  ```

---

### 2. Obras Clásicas y Patrísticas (`type: classic`)
Para citar fuentes antiguas o colecciones patrísticas (ej. *Patrologia Latina*, *Patrologia Graeca*):

1. Crea un elemento de tipo **Sección de un libro** (*Book Section*).
2. Rellena los campos con la siguiente estructura:

| Campo Zotero | Valor de Ejemplo | Descripción / Función |
| :--- | :--- | :--- |
| **Título** | `Historia ecclesiastica` | Título de la obra clásica. |
| **Autor** | `Rufino de Aquileya` | Autor antiguo. |
| **Serie / Colección** | `Patrologia Latina` | Nombre completo de la colección. |
| **Volumen** | `21` | Número del volumen dentro de la colección. |
| **Páginas** | `461-540` | Rango completo de páginas de la edición. |
| **Lugar** | `Paris` | Lugar de edición. |
| **Fecha** | `1849` | Año de la edición consultada. |
| **Editor** | `Domenico Vallarsi` | Editor científico de la versión. |
| **Extra / Adicional** | `type: classic`<br>`collection-title-short: PL` | **OBLIGATORIO.** Define el comportamiento especial y la abreviatura. |

#### Resultados esperados:
* **Primera cita (Nota):** RUFINO DE AQUILEYA, *Historia ecclesiastica*, I, 6: Patrologia Latina 21, 473-475.
* **Citas posteriores (Nota):** RUFINO DE AQUILEYA, *Historia ecclesiastica*, I, 7: PL 21, 477.
* **Bibliografía:** RUFINO DE AQUILEYA, *Historia ecclesiastica*, Patrologia Latina 21, Paris, 1849, 461-540.

#### Uso del *locator* (Página / Pasaje específico):
Al insertar la cita en Word/Obsidian, introduce el pasaje (ej. `I, 6` o `libros X-XI`) en el campo **Locator** / **Página**.


## Resultados no conseguidos:
Cuando se cita un capítulo de libro y coinciden autor y editor, el editor aparece con apellidos y nombre en vez de con «Id.».
---

## Licencia y referencias

Desarrollado siguiendo las especificaciones oficiales de la [documentación de CSL](https://docs.citationstyles.org/). Licencia Creative Commons Attribution-ShareAlike 3.0.

Se han empleado las [Directrices para autores](https://revistas.unav.edu/index.php/scripta-theologica/about/submissions) de *Scripta Theologica*.