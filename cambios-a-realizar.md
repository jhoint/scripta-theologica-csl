# Cambios a realizar

Estado a 2026-11-11. Los tipos de documento y los casos que figuraban aquí como pendientes (febrero de 2026) se han comprobado con `pruebas-tipos.json` (ver `readme.md`, apartado Pruebas).

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
| Nota suelta | `document` | Resuelto (archivo e inéditos). |
| Preprint | `article` | Resuelto (obras independientes). |

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
* **Edición y editorial en las voces de obras de consulta:** hoy no salen, como en el ejemplo de las normas («ILLANES, J.L., «Vocación», en *Gran Enciclopedia Rialp* 23 (1975) 659-662»). Chicago sí las pone; decidir si se añaden.

* **Obras patrísticas y ediciones críticas:** el modelo actual (Sección de un libro con `type: classic`) describe una obra dentro de un volumen numerado de una serie, con editor (PL, PG). Casos que hay que decidir:
  1. Obra dentro de un volumen de una serie: cubierto. Probar con ediciones críticas en serie (CCSL, CSEL, GCS…).
  2. Edición crítica que ocupa un libro entero (p. ej. un volumen de *Sources Chrétiennes* con una sola obra): *Libro* con `type: classic` (ver la propuesta más abajo).
  3. Obra en varios volúmenes: depende de «Volumen en las citas posteriores».
  4. Traducción usada además del original: depende de «Traductor en los libros traducidos» y de los datos de la edición original.
  5. Cita por divisiones internas (libro, capítulo): cubierto con el locator (ver `OBRAS-CLASICAS.md`).

  Antes de decidir: qué dicen las normas de *Scripta* sobre fuentes patrísticas, cómo citan los Padres los artículos recientes de la revista y una tabla con casos reales. Consultarlo con el director de tesis.

  Propuesta y decisiones de formato (2026-11-10). Nombres: el de la interfaz de Zotero en español, con la variable CSL entre paréntesis (esquema de Zotero, versión 45).
  * **Dos modelos con `type: classic`:** obra dentro de un volumen de una colección (PL, PG) → *Sección de un libro*; edición crítica u obra publicada como libro propio (CCSL, SC, una traducción) → *Libro*. Con `type: classic` al estilo le llega el tipo `classic` en los dos casos, sin saber cuál era el tipo de Zotero; los distingue por los campos: *Sección de un libro* trae Páginas (`page`), que *Libro* no tiene (solo Número de páginas, `number-of-pages`).
  * **Número de la colección:** usar Número de la serie (`collection-number`) en lugar de Volumen (`volume`), con Volumen como alternativa si Número de la serie está vacío (las fichas actuales de PL siguen funcionando). Según la especificación de CSL 1.0.2, `collection-number` es el «número que identifica la colección que contiene el ítem (p. ej. el número de serie de un libro)» y `volume`, el volumen del ítem o de su contenedor. Con los dos rellenos, Volumen es el tomo (p. ej. SC 264, t. 1; formato del tomo por decidir). Hoy, con Serie = Sources Chrétiennes, Número de la serie = 264 y Volumen = 1, sale «Sources Chrétiennes 1». Cambia el estilo, los ejemplos de `OBRAS-CLASICAS.md` y `CAMPOS.md`, y hay que repetir las pruebas de obras clásicas.
  * **Editorial (`publisher`):** en `classic` no sale («Paris, 1849»). Correcto para PL; decidir para las ediciones críticas (Brepols, Cerf).
  * **«en … (ed.)»:** tiene sentido cuando la obra está dentro de un volumen editado por otro (PL), no cuando ocupa el libro entero: ahí sería algo como «ed. A. Mutzenbecher». Decidir el formato.
  * **Traductor (`translator`):** en `classic` no sale (prueba con *Contre les hérésies* y *Vida de Moisés*). Ver «Traductor en los libros traducidos».
  * **Obra clásica sin datos de edición** (*Confessiones*, citada por sus divisiones: «AGUSTÍN DE HIPONA, *Confessiones*, 1.1.1»): sale bien; documentarla en `OBRAS-CLASICAS.md` como uso válido. Decidir si entra en la bibliografía: Chicago 18 no la incluye si no tiene editor, traductor, editorial o archivo (según los comentarios de su código, CMOS18 14.143-14.147); el estilo sí («AGUSTÍN DE HIPONA, *Confessiones*.»).
  * **Pregunta:** el editor de un clásico sale «en Vallarsi, D. (ed.)», sin versalitas y con inicial; el de una obra colectiva, «en VAUCHEZ, André (ed.)». ¿Decisión de febrero o incoherencia?

### Por implementar
* **Artículo sin fecha:** debería salir «s.f.». Ahora sale sin fecha ni paréntesis («Revista de Ejemplo 1 1-2»).
* **Libro con fecha original y fecha de edición:** `original-date` no se muestra.
* **Tipo de tesis:** sale tal como está en el campo *Tipo* de Zotero; «Doctoral dissertation» sale sin traducir. Se resuelve rellenándolo en español, o se traduce en el estilo.
* **Bibliografía por bloques** (fuentes, estudios…): no implementada.

### Detectado al comparar con Chicago 18 (2026-11-04)
Comparación de los 51 casos de `pruebas-tipos.json` con `chicago-notes-bibliography.csl` (18.ª ed.). Solo afecta a tipos que las normas de la revista no regulan.
* **Fechas completas en web, blogs, redes, eventos, representaciones, tratados y emisiones:** Chicago imprime la fecha entera («2 de enero de 2020»); el estilo solo el año. Decidir si se quiere el día (revistas y periódicos ya la llevan completa).
* **Reseñas (`review`, `review-book`):** Chicago antepone «review of» al título reseñado; en las reseñas de libros el estilo pone el título reseñado entre comillas sin indicar que es una reseña. Se pierde esa información.
* **Número de informe (`report`):** sale sin etiqueta («Informe de ejemplo, 12, Madrid: …») y se confunde con la página. Chicago pone «no. 12».
* **Partituras (`musical_score`):** en la cita posterior el título pasa de cursiva a comillas. Incoherencia interna, probablemente un error.
* **Voces de obras de consulta:** la cita posterior omite la página; Chicago la mantiene. Confirmar con las normas si es deliberado.
* **Tesis y conjuntos de datos:** Chicago pone el título de una tesis entre comillas; el estilo lo pone en cursiva (igual que los conjuntos de datos). Decidir.

### Detectado con «CMOS18 test» (2026-11-04)
Comparación de los 229 ejemplos de la colección «CMOS18 test» de Zotero (la de pruebas del estilo Chicago) con `chicago-notes-bibliography.csl` (18.ª ed.): campos que Chicago imprime y el estilo no. Origen de los datos (no se publican en este repositorio): colección «CMOS18 test» del grupo de Zotero 2205533 (la que enlaza la cabecera de `chicago-notes-bibliography.csl`), exportada como Better CSL JSON; para repetir la comparación basta exportarla de nuevo y pasarla por Pandoc con los dos estilos.
* **Obras «en prensa» (`status: forthcoming`):** se pierde en libros y capítulos (Chicago: «Publisher, forthcoming»). Decidir cómo mostrarlo («en prensa») y de qué campo de Zotero sale.
* **Editor de un libro que también tiene autor** (15 de 77 libros): Chicago imprime «Editado por …»; el estilo lo omite, igual que el traductor (6 libros). Afecta a ediciones preparadas por otro. Relacionado con «Traductor en los libros traducidos» (más arriba).
* **Serie del libro** (`collection-title` y su número, 15 libros): el estilo no la imprime, tampoco en los ejemplos oficiales de la revista. Comprobar con las normas si hay que ponerla.
* **Número de volúmenes** («2 vols.», 10 libros): el estilo solo lo imprime en 1 de 10.
* **Detalles menores:** duración de grabaciones y discursos («4 min., 40 sec.»), número de ProQuest en las tesis y «after» en fechas de manuscritos: Chicago los imprime y el estilo no.

### Detectado por un usuario del estilo (2026-11-10)
Dudas de un compañero tras probar el estilo, reproducidas con Pandoc 3.8.2 y con citeproc-js (el motor de Zotero con Word; no probado dentro de Zotero ni de Word).
* **Volumen en las citas posteriores:** en una obra en varios volúmenes, la primera cita da «SCHMAUS, Michael, *Teología dogmática*, I, Madrid: Rialp, 1960, 30» y las posteriores «SCHMAUS, Michael, *Teología dogmática*, 31» para todos los volúmenes, que no se distinguen. Añadir el volumen en la cita posterior. Arreglo provisional: Título corto `Teología dogmática, <i>II</i>` (el número sale en redonda con citeproc-js; con Pandoc, sin comprobar en Word).
* **Comillas dentro de un título entre comillas (solo Pandoc):** si el título de un artículo o capítulo lleva comillas españolas escritas en Zotero (`«persona»`), Pandoc las deja anidadas («El concepto de «persona» en…»); citeproc-js las pasa a “ ”. Con comillas rectas (`"persona"`) los dos motores dan “persona”. **Resuelto con documentación (2026-11-10):** ya lo decía `readme.md`; ampliado allí con la jerarquía de la RAE (*Diccionario panhispánico de dudas*, «comillas», apdo. 1; confirmada para este caso por una consulta a la RAE) y remisión desde `CAMPOS.md`. Limitación sin arreglo en el estilo: el tercer nivel sale «…» en lugar de ‘…’ (el archivo de idioma español de CSL solo define dos niveles).
* **Varios capítulos de la misma obra colectiva:** cada capítulo repite la descripción completa del libro en su primera cita. Sin solución automática en CSL 1.0.2: la condición `position` solo se refiere a citas anteriores del mismo ítem («first», «subsequent», «ibid»…), no de su obra colectiva (especificación de CSL 1.0.2, condición `position`, https://docs.citationstyles.org/en/stable/specification.html). En el foro del proyecto CSL se trata como funcionalidad no soportada que exigiría relaciones entre ítems (hilo «More complex citation/bibliography formats», https://discourse.citationstyles.org/t/more-complex-citation-bibliography-formats/1588). Se descarta usar la extensión CSL-M. Se anota para no volver a investigarlo.

### Variables que Chicago imprime y el estilo ignora (2026-11-10)
Comparando las variables que lee cada estilo: `chicago-notes-bibliography.csl` usa 76 y `scripta-theologica.csl` 38. `CAMPOS.md` ya avisa de que estos campos no salen; lo que falta es decidir, con las normas de la revista, cuáles debe imprimir el estilo (que Chicago las imprima no obliga a hacerlo).

Fuentes normativas: qué significa cada variable, la especificación de CSL 1.0.2, apéndice IV «Variables» (https://docs.citationstyles.org/en/stable/specification.html); qué campo de Zotero va a cada variable y su etiqueta en español, el esquema de Zotero, versión 45 (https://github.com/zotero/zotero-schema, `schema.json`). Sin comprobar que Zotero 10 use exactamente la versión 45 del esquema.

Ya anotadas más arriba: serie y número, número de volúmenes, editor o traductor junto al autor, obras en prensa y fecha original.

**Con campo propio en Zotero** (prioritarias: puede haber datos ya rellenados que se pierden):
* **Accedido** (`accessed`, casi todos los tipos): fecha de consulta de una web o documento en línea. Ya decidido: no se añade (ver «Otros puntos», en Resuelto). Revisar solo si cambia el criterio.
* **Fecha original, Editor original, Lugar original** (`original-date`, `original-publisher`, `original-publisher-place`; libro y sección de un libro): datos de la edición original en traducciones y reediciones. «Editor original» es la editorial.
* **Número de volúmenes** (`number-of-volumes`) y **Número de la serie** (`collection-number`): ya anotados más arriba.
* **Editor de la serie** (creador; `collection-editor`): director de la serie.
* **Contribuidor** (creador; `contributor`): colaborador menor («con la colaboración de»).
* **Número de la parte, Título de la parte** (`part-number`, `part-title`; solo artículo de revista académica y estándar): artículo publicado en varias entregas.
* **Estado** (`status`): solo existe en patente y estándar. Para una obra «en prensa» de tipo libro habría que escribir en Extra / Adicional `status: forthcoming` (afecta al pendiente de obras en prensa).

**Sin campo en Zotero** (solo salen si se escriben en Extra / Adicional como `variable: valor`):
* **Título del volumen** (`volume-title`): título de un volumen de una obra en varios volúmenes (*Teología dogmática*, II: *Dios creador*) y, según la especificación, de los números monográficos de revista. Relacionado con «Volumen en las citas posteriores». Práctica documentada en el foro de Zotero: escribir `volume-title: …` en Extra; según los participantes, Chicago 18, APA, MHRA, MLA y Oxford lo leen y SBL no (hilo «Volume title field?», enero-abril de 2026, https://forums.zotero.org/discussion/comment/505663/). Si se implementa, documentarlo en `CAMPOS.md`.
* **Título original** (`original-title`): título de la obra original en una traducción.
* **Compilador** (`compiler`): quien reúne o selecciona textos de otros (antologías, recopilaciones de escritos).
* **Tipo de obra reseñada** (`reviewed-genre`): relacionado con el pendiente de reseñas.
* **Menos frecuentes:** suplemento de revista (`supplement-number`), fecha de un congreso o acto (`event-date`) y fecha de publicación anticipada en línea (`available-date`).
* **Editor y traductor a la vez** (`editor-translator`): no se escribe; según la especificación lo genera el procesador cuando editor y traductor son la misma persona. El estilo ya define el término «ed. y trad.»: comprobar si sale.

**Otras disciplinas** (hoy no salen y `CAMPOS.md` lo indica; objetivo: que el estilo sea completo): Compositor (`composer`, música litúrgica o sacra), Comisario (`curator`, catálogos de exposición de arte sacro; sin campo en Zotero), Ilustrador (`illustrator`; sin campo en Zotero), Productor, Productor ejecutivo, Guionista, Creador de la serie, Miembro del reparto, Invitado y Narrador (`producer`, `executive-producer`, `script-writer`, `series-creator`, `performer`, `guest`, `narrator`: cine, televisión y pódcast), Organizador y Moderador (`organizer`, `chair`: congresos), Duración y Tamaño de la obra (`dimensions`) y Escala (`scale`).

**Descartadas** (no aplican a un estilo de notas teológico): `references` y `submitted` (Chicago las usa en tipos jurídicos y patentes), `page-first` (la calcula el procesador; Chicago solo la usa en macros jurídicas), `year-suffix` (para estilos autor-fecha), `event` (variante obsoleta de `event-title`, que el estilo ya usa) y `original-author` (Creador original; en Zotero solo en grabaciones de sonido).

### Prueba sobre la biblioteca exportada (2026-11-11)
Objetivo: que el estilo sea completo, no solo para la tesis. Exportación Better CSL JSON de la biblioteca de Zotero (455 obras: 206 de la tesis, 230 de la colección «CMOS18 test» y 19 de las pruebas del estilo). Para cada obra y cada campo relleno se quita el campo y se vuelve a generar con citeproc-js la primera cita, una posterior y la bibliografía; si nada cambia, el estilo ignora ese campo en esa obra. Informe completo, con las claves de cada obra, fuera del repositorio (`Claude outputs/campos-ignorados-2026-11-11.md`, porque incluye la bibliografía de la tesis); el CMOS18 test sirve de batería de pruebas para cada cambio.

**Obras afectadas por pendientes ya anotados** (tesis / CMOS18 test):
* Serie del libro (`collection-title`) y su número (`collection-number`): 35 libros y 3 capítulos / 21 libros y 4 capítulos. Es lo que más afecta a la tesis.
* Contribuidor (`contributor`): 13 / 12. Antes de decidir, revisar en la tesis si son traductores o prologuistas mal clasificados.
* Editorial en obras clásicas: 6 de 8 / 3.
* Editor de un libro que también tiene autor: 1 / 15.
* Número de volúmenes: 1 / 14 (incluye un clásico).
* Traductor: 0 / 10 (7 libros, 2 clásicos y 1 artículo de revista).
* Editor de la serie: 0 / 12. Estado (obras en prensa): 0 / 11. Título del volumen: 0 / 11. Fecha del acto: 0 / 10. Publicación anticipada en línea: 0 / 6. Fecha original: 0 / 4. Reseñas (autor y título reseñados): 0 / 4 y 3.

**Nuevos, detectados solo con el CMOS18 test:**
* **Obra completa dentro de un volumen recopilatorio** (Libro con Título del libro y Páginas: una novela en *Later novels*, una obra en *The complete works* de Shakespeare): se pierden el volumen y las páginas. Es el mismo caso que una obra patrística dentro de un volumen; resolverlo junto con «Obras patrísticas y ediciones críticas».
* **Cartas publicadas en una colección** (`personal_communication` con Título del libro, Editor, Editorial, Volumen y Páginas: *Letters of Henry Adams*, *Letters of E. B. White*): se pierden todos los datos de la edición. Relevante para epistolarios.
* **Capítulo en un libro de varios volúmenes** (Volumen en un capítulo): se pierde el volumen. Número de capítulo (`chapter-number`): se pierde.
* **Prólogos, epílogos y similares** (Género, `genre`, en un capítulo: «foreword»): se pierde; Chicago escribe «foreword to». También en una carta al director («letter to the editor») y en un fragmento clásico («frag. 115 Diels-Kranz»).
* **Soporte** (`medium`): libro electrónico (EPUB, Kindle), microfilme, vídeo, «exhibition catalog». Se pierde.
* **Número de artículo en revistas electrónicas** (Número, `number`, p. ej. «e0263069»): se pierde; en revistas sin páginas es el único localizador.
* **Editor de un número de revista** (Editor en un artículo de revista): se pierde.
* **Serie de una revista** («n.s.», «2nd ser.», Serie en un artículo): se pierde.
* **Sección de periódicos y revistas** (`section`: «Sports», «Arts»): se pierde. **Volumen en revistas no académicas** (`article-magazine`): se pierde (también 4 de la tesis).
* **Edición de un capítulo** (Edición en un capítulo de un libro en 2.ª ed.): se pierde. Edición de un periódico («late city») y de una ley: menor.
* **Base de datos y número de tesis** (Archivo «ProQuest», «EBSCOhost», «LexisNexis»; Número de la tesis en ProQuest): se pierden (los de ProQuest ya estaban como «detalle menor»).
* **Folio en un manuscrito** (Páginas «fol. 466r»): se pierde. Relevante para documentos de archivo.
* **Entrevistas:** emisora (Editorial: «PBS», «NPR»), lugar, páginas y sección cuando la entrevista está publicada: se pierden. Entrevistador en una entrevista publicada en una revista: se pierde.
* **Mapas en un atlas** (Volumen y Páginas «fig. 51.3»), **número suelto de una revista** (Volumen en `periodical`), **partitura en una edición crítica** (Serie y Editor), **país en una película** (Lugar), **editorial de un discurso** (sitio que lo publica), **autor del libro contenedor** (`container-author`) y **plataforma en una reseña de televisión** (`event-title`): se pierden.

**Datos que conviene limpiar en la biblioteca de la tesis** (no es cosa del estilo):
* Páginas con el total o con texto en un libro: IsastiElizaran («P»), Ormaetxea («26 p»), Whyte1991 («x+317–x+317»).
* Sección con el subtítulo de la revista: ReteguiAyastuy2017, Sinde2022.
* Archivo con nombres de catálogo: CruzFreyre2013 («WorldCat.org»), Oyarzabal1989 (catálogo de Mondragon Unibertsitatea), RufinodeAquileya1849 («Patrologia Latina»).
* Obras clásicas con Título del libro relleno: HilariodePoitiers1916, HilariodePoitiers2019, PascasioRadberto1969 y 1969a (ver «Del repositorio»).
* Contribuidores: revisar los 13 (p. ej. Borne1944).

### Del repositorio
* `zotero-outputs.md` es de febrero de 2026 y no refleja el estilo actual: regenerarlo con `pruebas-scripta.json` o retirarlo.
* Obras clásicas: con «Título del libro» (`container-title`) rellenado, la bibliografía imprime ese título en lugar del Título, y las citas no. Decidir si se unifica (hoy se evita dejando el campo vacío; ver `OBRAS-CLASICAS.md`).
* Comentarios del estilo desactualizados: la macro `classic-editor` dice «en Domenico Vallarsi (ed.)» y el resultado es «en Vallarsi, D. (ed.)». Solo es un comentario.
