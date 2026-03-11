
## Estado de sesion (2026-03-11)

### Cerrado en esta sesion

- Se consolidaron 5 casos reales de tipo `book` en `sale-deberiasalir.md` con formato `Actual` vs `Deberia salir` + CSL-JSON.
- Se confirmo que las versalitas de apellidos funcionan en notas para autores principales.
- Se aislaron 5 ajustes pendientes para `book` (ya registrados tambien en `CHANGELOG.md`):
	- Expandir rangos de pagina (`128-35` -> `128-135`).
	- Pasar datos editoriales en notas a `Lugar: Editorial, ano` sin parentesis.
	- Evitar capitalizacion forzada tipo ingles en `title-primary`.
	- Ocultar `contributor` en notas.
	- Ocultar `collection-title` y `collection-number` en notas.

### Siguiente bloque de trabajo (preparado)

Objetivo: incorporar ejemplos no-book antes de tocar macros compartidas, para hacer cambios una sola vez y con menos regresion.

Tipos prioritarios para aportar ahora:

1. `article-journal` (2-3 casos)
2. `chapter` / `paper-conference` (2-3 casos)
3. `entry-dictionary` y `entry-encyclopedia` (2-3 casos)
4. `thesis` (1-2 casos)

Plantilla recomendada por caso:

- Tipo:
- Contexto: primera nota / subsiguiente / bibliografia
- Actual:
- Deberia salir:
- Comentarios: locator, DOI/URL, editor/traductor, fecha de acceso, etc.
- CSL-JSON: bloque del item exportado desde Zotero

Orden recomendado de aplicacion cuando haya ejemplos suficientes:

1. Cambios globales y seguros.
2. Ajustes por familias de macro (`book-like`, `journal-like`, `reference-like`).
3. Verificacion final transversal en notas y bibliografia.

## Tipos de documento a añadir

Tras haber bajado la biblioteca de prueba de [CSL Styles Development](https://www.zotero.org/groups/4211/csl_styles_development) he visto que hay unos cuantos tipos de documentos que no están desarrollados en este estilo, principalmente porque no aparecen en los ejemplos de las [instrucciones para los autores de ScrTH](https://revistas.unav.edu/index.php/scripta-theologica/about/submissions).

A continuación iré listando los tipos de documentos que veo que faltan y los que voy incorporando.

### Pending types

+ Carta (Letter). No aparece el recipient.
+ Software. No estoy seguro de que haga falta incorporarlo de momento.
+ Informe (report).
+ Correo electrónico. Aparece pero no tiene un buen formato. ¿Es necesario añadirlo?
+ Entrevista (interview)
+ Mapa (maps)
+ Artículo de periódico
+ Artículo de revista (no académica).
+ Grabación de sonido
+ Presentación
+ Grabación de vídeo (Film)
+ Caso jurídico. De momento no parece que me interese mucho añadirlo
+ Obra de arte
+ Patente
+ Manuscrito
+ Estatuto (Ley)
+ Presentación
+ Nota
+ Película. No aparecen los directores y tendrían que aparecer como dirs.
+ Página web
+ Caso judicial

### Added types

## Other issues

Cuando hay comillas en el título de un capítulo de libro, las cambia a comillas angulares, aunque en zotero estén de otra manera.

Habría que añadir el "accedido el" cuando aparezca una fecha de acceso.

Traducir doctoral disertation, pues aparece cuando hay un tipo de esos.

Un artículo de revista, si tiene DOI no tendría que poner la URL.

En un artículo si no hay fecha, tendría que poner s.f.

Añadir edición, editorial? a enciclopedia y artículo de diccionario.

¿Qué pasa si tengo fecha y fecha original en un libro?
