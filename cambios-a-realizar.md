# Cambios a realizar

Estado a 2026-11-03. Los tipos de documento y los casos que figuraban aquí como pendientes (febrero de 2026) se han comprobado con `pruebas-tipos.json` (ver `readme.md`, apartado Pruebas).

## Resuelto

### Tipos de documento
Zotero → tipo CSL → familia del estilo:

| Tipo en Zotero | Tipo CSL | Estado |
| :--- | :--- | :--- |
| Carta, correo electrónico | `personal_communication` | Resuelto. Sale el destinatario: «Carta a Carlos Ruiz», «Correo electrónico a Carlos Ruiz». |
| Informe | `report` | Resuelto (obras independientes). |
| Software | `software` | Resuelto: título, versión, editorial, año. |
| Entrevista | `interview` | Resuelto (archivo e inéditos): «entrevista de …». |
| Mapa | `map` | Resuelto (obras independientes). |
| Artículo de periódico, artículo de revista no académica | `article-newspaper`, `article-magazine` | Resuelto: con el título de la publicación y la fecha completa. |
| Grabación de sonido | `song` | Resuelto, con editorial o sello. |
| Presentación | `speech` | Resuelto (archivo e inéditos). |
| Grabación de vídeo, película | `motion_picture` | Resuelto. Los directores salen como «dirigido por Luis Director y Óscar Otro» (forma de Chicago), no como «dirs.». Cambiable si se prefiere. |
| Caso, caso judicial | `legal_case` | Resuelto (jurídicos). |
| Obra de arte | `graphic` | Resuelto (obras independientes). |
| Patente | `patent` | Resuelto (jurídicos). |
| Manuscrito | `manuscript` | Resuelto (archivo e inéditos). |
| Estatuto (ley) | `legislation` | Resuelto (jurídicos). |
| Página web | `webpage` | Resuelto (web). |
| Nota | — | No es un tipo del esquema CSL 1.0.2: se descarta. |

### Otros puntos
* **Comillas dentro del título de un capítulo:** resuelto con `quotes="true"`. En Zotero se escriben rectas y emparejadas (ver `readme.md`).
* **Artículo con DOI: no poner la URL:** resuelto. El enlace sale solo si no hay DOI.
* **«Accedido el» con fecha de acceso:** no se añade. El ejemplo de las normas de la revista usa «recuperado de» y el enlace, sin fecha.

## Pendiente

### Por decidir
* **Traductor en los libros traducidos** («trad. de …»): ahora no sale.
* **Directores de películas como «dir.»** en lugar de «dirigido por».
* **«(=SL)» en la primera cita de un clásico:** *Scripta* podría presentar la colección como «Corpus Christianorum. Series Latina (=SL) 36»; el estilo da el nombre completo y luego la sigla, sin «(=SL)». Comprobar con las normas antes de cambiarlo.
* **«ID.» cuando el editor de la obra es el autor del capítulo:** el estilo repite el nombre (desviación consciente de las normas; ver `readme.md`). Se cambiará si lo pide la revista o el director de la tesis.
* **Formato de los documentos de archivo:** provisional, las normas no lo regulan. Pendiente de confirmar (fecha en cifras o en romanos; cómo distinguir una carta de y a una misma persona).
* **Criterio para documentos del Magisterio:** las normas de la revista no lo regulan.

### Por implementar
* **Artículo sin fecha:** debería salir «s.f.». Ahora sale sin fecha ni paréntesis («Revista de Ejemplo 1 1-2»).
* **Libro con fecha original y fecha de edición:** `original-date` no se muestra.
* **Edición y editorial en voces de diccionario y enciclopedia:** no salen (comprobado con `entry-dictionary` y `entry-encyclopedia`).
* **Tipo de tesis:** sale tal como está en el campo *Tipo* de Zotero; «Doctoral dissertation» sale sin traducir. Se resuelve rellenándolo en español, o se traduce en el estilo.
* **`preprint`:** usa la rama genérica; no tiene rama propia.
* **Bibliografía por bloques** (fuentes, estudios…): no implementada.

### Del repositorio
* `zotero-outputs.md` es de febrero de 2026 y no refleja el estilo actual: regenerarlo con `pruebas-scripta.json` o retirarlo.
* Publicar la versión 0.2.0 (etiqueta y *release*) según el proceso del `CHANGELOG.md`.
