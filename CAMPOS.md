# Guía de campos: cómo rellenar Zotero para que la referencia salga bien

Esta guía dice, para cada tipo de documento de **Zotero** (interfaz en español), qué campos llegan a la referencia con el estilo `scripta-theologica.csl` y en qué parte: primera cita, cita posterior (forma abreviada) o bibliografía. Los campos que no aparecen en la tabla de un tipo **no producen ningún efecto** en la referencia, aunque se rellenen.

> Para otros gestores (Mendeley, etc.) no hay todavía guía; la lógica del estilo es la misma, pero cambian los nombres de campo y su correspondencia con CSL.

## Cómo se ha elaborado

1. Se tomó el esquema oficial de Zotero (versión 45 del esquema), que fija qué campos tiene cada tipo y a qué variable CSL se convierte cada uno ([zotero/zotero-schema](https://github.com/zotero/zotero-schema); conversión en `itemToCSLJSON`, [zotero/utilities](https://github.com/zotero/utilities)).
2. Para cada tipo se generó un elemento con **solo un campo relleno cada vez** y se pasó por Pandoc (citeproc 3.8.2) con este estilo, mirando si el valor aparecía en la primera cita, en la cita posterior y en la bibliografía. Después se repitió con todos los campos a la vez y se buscaron los campos que se anulan entre sí.
3. Los datos son ficticios y las pruebas están hechas sobre el estilo versión 0.2.0.

Lo comprobado es el comportamiento **del estilo** a partir de los datos que Zotero exporta. La conversión del campo Extra la hace Zotero (o Better BibTeX), no el estilo; ver el apartado de Extra.

## Cómo leer las tablas

Las columnas son **1.ª cita | cita posterior | bibliografía**. «✓» = aparece; «·» = no aparece.

## Reglas que valen para todos los tipos

* **DOI y URL:** si hay DOI, se imprime el DOI y **no** la URL. La URL solo sale si no hay DOI.
* **Título corto:** solo se usa en las **citas posteriores**. Si no lo hay, la cita posterior usa el Título completo. En la primera cita y en la bibliografía nunca sale.
* **Número (fascículo) de una revista:** solo sale si **no hay Volumen**.
* **Abreviatura de la revista:** si existe, sustituye al título de la publicación en las citas y en la bibliografía.
* **Volumen:** en un libro sale en cifras romanas («Título, IV»); en una obra clásica, el de la serie, en cifras árabes («Patrologia Latina 21»); en la sección de un libro no sale.
* **Autor:** el primer tipo de creador de cada ficha (el «Autor» en libros y artículos; «Artista» en una obra de arte; «Intérprete» en una grabación; etc.) es el que el estilo imprime como autor, en versalitas. Los demás tipos de creador no salen, salvo los que se indican en cada tabla.
* **Sin autor:** el estilo usa, por este orden, el editor, el traductor y el título (p. ej. «TRAD, Tomás (trad.), *Solo traductor*…»). Un libro sin ninguno de los tres empieza por el título.
* **Traductor con autor:** si el libro tiene autor, el traductor **no** se imprime.
* **Obra sin fecha:** el estilo no imprime nada (no pone «s. f.»). Está en pendientes.
* **Fecha de acceso:** nunca se imprime.
* **Campos que no se usan en ningún tipo:** Accedido, Catálogo de biblioteca, Clave de cita, Duración, Editor original, Escala, Estado, Estado legal, Fecha de prioridad, Fecha de solicitud, Fecha original, Historia, ISBN, ISSN, Idioma, Licencia, Lugar del evento, Lugar original, Nombre de la conferencia, Número de la parte, Número de la serie, Número de páginas, Número de solicitud, Número de volúmenes, Números de prioridad, PMCID, PMID, Referencias, Resumen, Signatura, Tamaño de la obra, Título de la parte, Título de la sesión.

## El campo Extra / Adicional

Zotero permite escribir en **Extra**, una línea por dato, `variable: valor`, para rellenar variables de CSL que no tienen campo propio. Al exportar, Zotero y Better BibTeX las convierten en campos CSL; Better BibTeX lo documenta, y admite nombres en la forma `Apellido || Nombre` ([Better BibTeX, Extra fields](https://retorque.re/zotero-better-bibtex/exporting/extra-fields/)).

**Importante (comprobado):** Pandoc **no** lee el Extra por sí mismo. Con un `biblioteca.json` exportado con **Better CSL JSON** el Extra funciona; con un JSON en el que el texto vaya como nota sin procesar, no. Si algo de Extra no sale en Pandoc, comprueba primero qué ha exportado Better BibTeX.

Usos de Extra que el estilo entiende:

| Línea en Extra | Para qué | Dónde se usa |
| :--- | :--- | :--- |
| `editorial-director: Apellido \|\| Nombre` | Director de una obra colectiva: sale «(dir.)» en lugar de «(ed.)» | Capítulos y obras colectivas |
| `type: classic` | Convierte el elemento en obra clásica o patrística | Sección de un libro (ver `OBRAS-CLASICAS.md`) |
| `collection-title-short: PL` | Sigla de la colección, para las citas posteriores y la bibliografía de obras clásicas | Obras clásicas |
| `container-title-short: DTC` | Sigla de un diccionario o enciclopedia | Diccionarios y enciclopedias (ver abajo) |

**Diccionarios y enciclopedias:** estos dos tipos de Zotero **no tienen campo de abreviatura** (solo las revistas tienen *Abrev. de revista*). La sigla de la obra se escribe en Extra: `container-title-short: DTC`. Comprobado: «VOZ, V, «Gracia», en DTC 6 (1920) 1-10». El *Título corto* de la voz se usa en las citas posteriores («Gracia corto»).

**Fecha original (`original-date`):** el estilo no la lee; escribirla en Extra no tiene efecto.

## Tablas por tipo de documento


### Obra de arte (`artwork`, CSL `graphic`)

**Creadores que salen** (1.ª cita | posterior | bibliografía): Artista (✓ | ✓ | ✓).  
No salen (salvo, si no hay autor, el Editor y el Traductor, que ocupan su lugar): Contribuidor.


| Campo | 1.ª | post. | bibl. | Observación |
| :--- | :-: | :-: | :-: | :--- |
| Título | ✓ | ✓ | ✓ | en citas posteriores lo sustituye el Título corto |
| Medio | ✓ | · | ✓ |  |
| Fecha | ✓ | · | ✓ |  |
| DOI | ✓ | · | ✓ |  |
| URL | ✓ | · | ✓ | solo si no hay DOI |
| Archivo | ✓ | · | ✓ |  |
| Posición en archivo | ✓ | · | ✓ |  |
| Título corto | · | ✓ | · |  |

### Grabación de sonido (`audioRecording`, CSL `song`)

**Creadores que salen** (1.ª cita | posterior | bibliografía): Intérprete (✓ | ✓ | ✓).  
No salen (salvo, si no hay autor, el Editor y el Traductor, que ocupan su lugar): Creador original, Compositor, Traductor, Contribuidor.


| Campo | 1.ª | post. | bibl. | Observación |
| :--- | :-: | :-: | :-: | :--- |
| Título | ✓ | ✓ | ✓ | en citas posteriores lo sustituye el Título corto |
| Formato | ✓ | · | ✓ |  |
| Etiqueta | ✓ | · | ✓ |  |
| Fecha | ✓ | · | ✓ |  |
| DOI | ✓ | · | ✓ |  |
| URL | ✓ | · | ✓ | solo si no hay DOI |
| Título corto | · | ✓ | · |  |

### Propuesta de ley (`bill`, CSL `bill`)

**Creadores que salen** (1.ª cita | posterior | bibliografía): Patrocinador (✓ | ✓ | ✓).  
No salen (salvo, si no hay autor, el Editor y el Traductor, que ocupan su lugar): Contribuidor.


| Campo | 1.ª | post. | bibl. | Observación |
| :--- | :-: | :-: | :-: | :--- |
| Título | ✓ | ✓ | ✓ |  |
| Número de propuesta de ley | ✓ | · | ✓ |  |
| Código | ✓ | · | ✓ |  |
| Volumen del código | ✓ | · | ✓ |  |
| Sección | ✓ | · | ✓ |  |
| Páginas del código | ✓ | ✓ | ✓ |  |
| Cuerpo legislativo | ✓ | · | ✓ |  |
| Sesión | ✓ | · | ✓ |  |
| Fecha | ✓ | · | ✓ |  |
| DOI | ✓ | · | ✓ |  |
| URL | ✓ | · | ✓ | solo si no hay DOI |

### Entrada de blog (`blogPost`, CSL `post-weblog`)

**Creadores que salen** (1.ª cita | posterior | bibliografía): Autor (✓ | ✓ | ✓).  
No salen (salvo, si no hay autor, el Editor y el Traductor, que ocupan su lugar): Traductor, Contribuidor.


| Campo | 1.ª | post. | bibl. | Observación |
| :--- | :-: | :-: | :-: | :--- |
| Título | ✓ | ✓ | ✓ | en citas posteriores lo sustituye el Título corto |
| Título del blog | ✓ | · | ✓ |  |
| Tipo de página Web | ✓ | · | ✓ |  |
| Fecha | ✓ | · | ✓ |  |
| DOI | ✓ | · | ✓ |  |
| URL | ✓ | · | ✓ | solo si no hay DOI |
| Título corto | · | ✓ | · |  |

### Libro (`book`, CSL `book`)

**Creadores que salen** (1.ª cita | posterior | bibliografía): Autor (✓ | ✓ | ✓).  
No salen (salvo, si no hay autor, el Editor y el Traductor, que ocupan su lugar): Contribuidor, Editor, Traductor, Editor de la serie.


| Campo | 1.ª | post. | bibl. | Observación |
| :--- | :-: | :-: | :-: | :--- |
| Título | ✓ | ✓ | ✓ | en citas posteriores lo sustituye el Título corto |
| Volumen | ✓ | · | ✓ |  |
| Edición | ✓ | · | ✓ |  |
| Fecha | ✓ | · | ✓ |  |
| Editorial | ✓ | · | ✓ |  |
| Lugar | ✓ | · | ✓ |  |
| DOI | ✓ | · | ✓ |  |
| URL | ✓ | · | ✓ | solo si no hay DOI |
| Título corto | · | ✓ | · |  |

### Sección de un libro (`bookSection`, CSL `chapter`)

**Creadores que salen** (1.ª cita | posterior | bibliografía): Autor (✓ | ✓ | ✓); Editor (✓ | · | ✓); Autor del libro (✓ | · | ✓).  
No salen (salvo, si no hay autor, el Editor y el Traductor, que ocupan su lugar): Contribuidor, Traductor, Editor de la serie.


| Campo | 1.ª | post. | bibl. | Observación |
| :--- | :-: | :-: | :-: | :--- |
| Título | ✓ | ✓ | ✓ | en citas posteriores lo sustituye el Título corto |
| Título del libro | ✓ | · | ✓ |  |
| Fecha | ✓ | · | ✓ |  |
| Editorial | ✓ | · | ✓ |  |
| Lugar | ✓ | · | ✓ |  |
| Páginas | ✓ | ✓ | ✓ |  |
| DOI | ✓ | · | ✓ |  |
| URL | ✓ | · | ✓ | solo si no hay DOI |
| Título corto | · | ✓ | · |  |

### Sección de un libro con `type: classic` (obra clásica o patrística)

Con la línea `type: classic` en Extra (ver `OBRAS-CLASICAS.md`), una Sección de un libro deja de tratarse como capítulo y los campos cambian. Comprobado con Pandoc 3.8.2 (un campo cada vez, sobre un elemento con Título, Autor y Fecha).

Creadores que salen: Autor (✓ | ✓ | ✓); Editor (· | · | ✓, como «en Vallarsi, D. (ed.)»). El pasaje (locator) sale en la primera cita y en las posteriores; las páginas que se escriben tras el locator, también.

| Campo | 1.ª | post. | bibl. | Observación |
| :--- | :-: | :-: | :-: | :--- |
| Título | ✓ | ✓ | ✓ | en citas posteriores lo sustituye el Título corto; en la bibliografía lo sustituye el Título del libro, si se rellena (conviene dejarlo vacío) |
| Serie | ✓ | ✓ | ✓ | en citas posteriores lo sustituye la sigla de Extra, si hay |
| `collection-title-short` (Extra) | · | ✓ | · | sigla de la serie |
| Volumen | ✓ | ✓ | ✓ | va con la serie |
| Fecha | · | · | ✓ |  |
| Lugar | · | · | ✓ |  |
| Páginas | · | · | ✓ | rango de la edición |
| DOI | ✓ | · | ✓ |  |
| URL | ✓ | · | ✓ | solo si no hay DOI |
| Título corto | · | ✓ | · |  |

No salen: Editorial, Edición, Traductor, Archivo, Posición en archivo, Número ni Sección.

### Caso (`case`, CSL `legal_case`)

**Creadores que salen** (1.ª cita | posterior | bibliografía): Autor (✓ | ✓ | ✓).  
No salen (salvo, si no hay autor, el Editor y el Traductor, que ocupan su lugar): Contribuidor.


| Campo | 1.ª | post. | bibl. | Observación |
| :--- | :-: | :-: | :-: | :--- |
| Nombre del caso | ✓ | ✓ | ✓ |  |
| Juzgado | ✓ | · | ✓ |  |
| Fecha de sentencia | ✓ | · | ✓ |  |
| Número de expediente | ✓ | · | ✓ |  |
| Acta judicial | ✓ | · | ✓ |  |
| Volumen de las actas | ✓ | · | ✓ |  |
| Primera página | ✓ | ✓ | ✓ |  |
| DOI | ✓ | · | ✓ |  |
| URL | ✓ | · | ✓ | solo si no hay DOI |

### Software (`computerProgram`, CSL `software`)

**Creadores que salen** (1.ª cita | posterior | bibliografía): Programador (✓ | ✓ | ✓).  
No salen (salvo, si no hay autor, el Editor y el Traductor, que ocupan su lugar): Contribuidor.


| Campo | 1.ª | post. | bibl. | Observación |
| :--- | :-: | :-: | :-: | :--- |
| Título | ✓ | ✓ | ✓ | en citas posteriores lo sustituye el Título corto |
| Título de la serie | ✓ | · | ✓ |  |
| Versión | ✓ | · | ✓ |  |
| Fecha | ✓ | · | ✓ |  |
| Sistema | ✓ | · | ✓ |  |
| Compañía | ✓ | · | ✓ |  |
| Lugar | ✓ | · | ✓ |  |
| Lenguaje de programación | ✓ | · | ✓ |  |
| URL | ✓ | · | ✓ | solo si no hay DOI |
| DOI | ✓ | · | ✓ |  |
| Archivo | ✓ | · | ✓ |  |
| Posición en archivo | ✓ | · | ✓ |  |
| Título corto | · | ✓ | · |  |

### Artículo en conferencia (`conferencePaper`, CSL `paper-conference`)

**Creadores que salen** (1.ª cita | posterior | bibliografía): Autor (✓ | ✓ | ✓); Editor (✓ | · | ✓).  
No salen (salvo, si no hay autor, el Editor y el Traductor, que ocupan su lugar): Contribuidor, Traductor, Editor de la serie.


| Campo | 1.ª | post. | bibl. | Observación |
| :--- | :-: | :-: | :-: | :--- |
| Título | ✓ | ✓ | ✓ | en citas posteriores lo sustituye el Título corto |
| Título de las actas | ✓ | · | ✓ |  |
| Editorial | ✓ | · | ✓ |  |
| Lugar | ✓ | · | ✓ |  |
| Fecha | ✓ | · | ✓ |  |
| Páginas | ✓ | ✓ | ✓ |  |
| DOI | ✓ | · | ✓ |  |
| URL | ✓ | · | ✓ | solo si no hay DOI |
| Título corto | · | ✓ | · |  |

### Conjunto de datos (`dataset`, CSL `dataset`)

**Creadores que salen** (1.ª cita | posterior | bibliografía): Autor (✓ | ✓ | ✓).  
No salen (salvo, si no hay autor, el Editor y el Traductor, que ocupan su lugar): Contribuidor.


| Campo | 1.ª | post. | bibl. | Observación |
| :--- | :-: | :-: | :-: | :--- |
| Título | ✓ | ✓ | ✓ | en citas posteriores lo sustituye el Título corto |
| Identificador | ✓ | · | ✓ |  |
| Tipo | ✓ | · | ✓ |  |
| Versión | ✓ | · | ✓ |  |
| Fecha | ✓ | · | ✓ |  |
| Repositorio | ✓ | · | ✓ |  |
| Ubicación del repositorio | ✓ | · | ✓ |  |
| Formato | ✓ | · | ✓ |  |
| DOI | ✓ | · | ✓ |  |
| URL | ✓ | · | ✓ | solo si no hay DOI |
| Archivo | ✓ | · | ✓ |  |
| Posición en archivo | ✓ | · | ✓ |  |
| Título corto | · | ✓ | · |  |

### Entrada de diccionario (`dictionaryEntry`, CSL `entry-dictionary`)

**Creadores que salen** (1.ª cita | posterior | bibliografía): Autor (✓ | ✓ | ✓).  
No salen (salvo, si no hay autor, el Editor y el Traductor, que ocupan su lugar): Contribuidor, Editor, Traductor, Editor de la serie.


| Campo | 1.ª | post. | bibl. | Observación |
| :--- | :-: | :-: | :-: | :--- |
| Título | ✓ | ✓ | ✓ | en citas posteriores lo sustituye el Título corto |
| Título del diccionario | ✓ | · | ✓ |  |
| Volumen | ✓ | · | ✓ |  |
| Fecha | ✓ | · | ✓ |  |
| Páginas | ✓ | · | ✓ |  |
| DOI | ✓ | · | ✓ |  |
| URL | ✓ | · | ✓ | solo si no hay DOI |
| Título corto | · | ✓ | · |  |

### Documento (`document`, CSL `document`)

**Creadores que salen** (1.ª cita | posterior | bibliografía): Autor (✓ | ✓ | ✓).  
No salen (salvo, si no hay autor, el Editor y el Traductor, que ocupan su lugar): Contribuidor, Editor, Traductor, Autor revisado.


| Campo | 1.ª | post. | bibl. | Observación |
| :--- | :-: | :-: | :-: | :--- |
| Título | ✓ | ✓ | ✓ |  |
| Tipo | ✓ | · | ✓ |  |
| Fecha | ✓ | · | ✓ |  |
| DOI | ✓ | · | ✓ |  |
| URL | ✓ | · | ✓ | solo si no hay DOI |
| Archivo | ✓ | · | ✓ |  |
| Posición en archivo | ✓ | · | ✓ |  |

### Correo electrónico (`email`, CSL `personal_communication`)

**Creadores que salen** (1.ª cita | posterior | bibliografía): Autor (✓ | ✓ | ✓).  
No salen (salvo, si no hay autor, el Editor y el Traductor, que ocupan su lugar): Traductor, Contribuidor, Receptor.


| Campo | 1.ª | post. | bibl. | Observación |
| :--- | :-: | :-: | :-: | :--- |
| Asunto | ✓ | ✓ | ✓ |  |
| Fecha | ✓ | · | ✓ |  |
| DOI | ✓ | · | ✓ |  |
| URL | ✓ | · | ✓ | solo si no hay DOI |

### Artículo de enciclopedia (`encyclopediaArticle`, CSL `entry-encyclopedia`)

**Creadores que salen** (1.ª cita | posterior | bibliografía): Autor (✓ | ✓ | ✓).  
No salen (salvo, si no hay autor, el Editor y el Traductor, que ocupan su lugar): Contribuidor, Editor, Traductor, Editor de la serie.


| Campo | 1.ª | post. | bibl. | Observación |
| :--- | :-: | :-: | :-: | :--- |
| Título | ✓ | ✓ | ✓ | en citas posteriores lo sustituye el Título corto |
| Título de la enciclopedia | ✓ | · | ✓ |  |
| Volumen | ✓ | · | ✓ |  |
| Fecha | ✓ | · | ✓ |  |
| Páginas | ✓ | · | ✓ |  |
| DOI | ✓ | · | ✓ |  |
| URL | ✓ | · | ✓ | solo si no hay DOI |
| Título corto | · | ✓ | · |  |

### Película (`film`, CSL `motion_picture`)

**Creadores que salen** (1.ª cita | posterior | bibliografía): Director (✓ | · | ✓); Entidad anfitriona (✓ | · | ✓); Traductor (✓ | ✓ | ✓).  
No salen (salvo, si no hay autor, el Editor y el Traductor, que ocupan su lugar): Productor, Guionista, Miembro del reparto, Invitado, Narrador, Contribuidor.


| Campo | 1.ª | post. | bibl. | Observación |
| :--- | :-: | :-: | :-: | :--- |
| Título | ✓ | ✓ | ✓ |  |
| Distribuidor | ✓ | · | ✓ |  |
| Fecha | ✓ | · | ✓ |  |
| Formato | ✓ | · | ✓ |  |
| DOI | ✓ | · | ✓ |  |
| URL | ✓ | · | ✓ | solo si no hay DOI |

### Mensaje en un foro (`forumPost`, CSL `post`)

**Creadores que salen** (1.ª cita | posterior | bibliografía): Autor (✓ | ✓ | ✓).  
No salen (salvo, si no hay autor, el Editor y el Traductor, que ocupan su lugar): Contribuidor.


| Campo | 1.ª | post. | bibl. | Observación |
| :--- | :-: | :-: | :-: | :--- |
| Título | ✓ | ✓ | ✓ | en citas posteriores lo sustituye el Título corto |
| Título de foro o lista de correo | ✓ | · | ✓ |  |
| Tipo de mensaje | ✓ | · | ✓ |  |
| Fecha | ✓ | · | ✓ |  |
| DOI | ✓ | · | ✓ |  |
| URL | ✓ | · | ✓ | solo si no hay DOI |
| Título corto | · | ✓ | · |  |

### Audiencia (`hearing`, CSL `hearing`)

No salen (salvo, si no hay autor, el Editor y el Traductor, que ocupan su lugar): Contribuidor.


| Campo | 1.ª | post. | bibl. | Observación |
| :--- | :-: | :-: | :-: | :--- |
| Título | ✓ | ✓ | ✓ |  |
| Comité | ✓ | · | ✓ |  |
| Número de documento | ✓ | · | ✓ |  |
| Páginas | ✓ | ✓ | ✓ |  |
| Cuerpo legislativo | ✓ | · | ✓ |  |
| Sesión | ✓ | · | ✓ |  |
| Fecha | ✓ | · | ✓ |  |
| DOI | ✓ | · | ✓ |  |
| URL | ✓ | · | ✓ | solo si no hay DOI |

### Mensaje instantáneo (`instantMessage`, CSL `personal_communication`)

**Creadores que salen** (1.ª cita | posterior | bibliografía): Autor (✓ | ✓ | ✓).  
No salen (salvo, si no hay autor, el Editor y el Traductor, que ocupan su lugar): Contribuidor, Receptor.


| Campo | 1.ª | post. | bibl. | Observación |
| :--- | :-: | :-: | :-: | :--- |
| Título | ✓ | ✓ | ✓ |  |
| Fecha | ✓ | · | ✓ |  |
| DOI | ✓ | · | ✓ |  |
| URL | ✓ | · | ✓ | solo si no hay DOI |

### Entrevista (`interview`, CSL `interview`)

**Creadores que salen** (1.ª cita | posterior | bibliografía): Entrevista con (✓ | ✓ | ✓); Entrevistador (✓ | · | ✓).  
No salen (salvo, si no hay autor, el Editor y el Traductor, que ocupan su lugar): Contribuidor, Traductor.


| Campo | 1.ª | post. | bibl. | Observación |
| :--- | :-: | :-: | :-: | :--- |
| Título | ✓ | ✓ | ✓ |  |
| Medio | ✓ | · | ✓ |  |
| Fecha | ✓ | · | ✓ |  |
| DOI | ✓ | · | ✓ |  |
| URL | ✓ | · | ✓ | solo si no hay DOI |
| Archivo | ✓ | · | ✓ |  |
| Posición en archivo | ✓ | · | ✓ |  |

### Artículo de revista académica (`journalArticle`, CSL `article-journal`)

**Creadores que salen** (1.ª cita | posterior | bibliografía): Autor (✓ | ✓ | ✓); Autor revisado (✓ | · | ✓).  
No salen (salvo, si no hay autor, el Editor y el Traductor, que ocupan su lugar): Contribuidor, Editor, Traductor.


| Campo | 1.ª | post. | bibl. | Observación |
| :--- | :-: | :-: | :-: | :--- |
| Título | ✓ | ✓ | ✓ | en citas posteriores lo sustituye el Título corto |
| Publicación | ✓ | · | ✓ | se pierde si hay Abrev. de revista |
| Fecha | ✓ | · | ✓ |  |
| Volumen | ✓ | · | ✓ |  |
| Número | ✓ | · | ✓ | se pierde si hay Volumen |
| Páginas | ✓ | ✓ | ✓ |  |
| Abrev. de revista | ✓ | · | ✓ |  |
| DOI | ✓ | · | ✓ |  |
| URL | ✓ | · | ✓ | solo si no hay DOI |
| Título corto | · | ✓ | · |  |

### Carta (`letter`, CSL `personal_communication`)

**Creadores que salen** (1.ª cita | posterior | bibliografía): Autor (✓ | ✓ | ✓).  
No salen (salvo, si no hay autor, el Editor y el Traductor, que ocupan su lugar): Receptor, Contribuidor, Traductor.


| Campo | 1.ª | post. | bibl. | Observación |
| :--- | :-: | :-: | :-: | :--- |
| Título | ✓ | ✓ | ✓ |  |
| Tipo | ✓ | · | ✓ |  |
| Fecha | ✓ | · | ✓ |  |
| DOI | ✓ | · | ✓ |  |
| URL | ✓ | · | ✓ | solo si no hay DOI |
| Archivo | ✓ | · | ✓ |  |
| Posición en archivo | ✓ | · | ✓ |  |

### Artículo de revista (`magazineArticle`, CSL `article-magazine`)

**Creadores que salen** (1.ª cita | posterior | bibliografía): Autor (✓ | ✓ | ✓).  
No salen (salvo, si no hay autor, el Editor y el Traductor, que ocupan su lugar): Contribuidor, Traductor, Autor revisado.


| Campo | 1.ª | post. | bibl. | Observación |
| :--- | :-: | :-: | :-: | :--- |
| Título | ✓ | ✓ | ✓ | en citas posteriores lo sustituye el Título corto |
| Publicación | ✓ | · | ✓ |  |
| Fecha | ✓ | · | ✓ |  |
| Número | ✓ | · | ✓ |  |
| Páginas | ✓ | ✓ | ✓ |  |
| DOI | ✓ | · | ✓ |  |
| URL | ✓ | · | ✓ | solo si no hay DOI |
| Título corto | · | ✓ | · |  |

### Manuscrito (`manuscript`, CSL `manuscript`)

**Creadores que salen** (1.ª cita | posterior | bibliografía): Autor (✓ | ✓ | ✓).  
No salen (salvo, si no hay autor, el Editor y el Traductor, que ocupan su lugar): Contribuidor, Traductor.


| Campo | 1.ª | post. | bibl. | Observación |
| :--- | :-: | :-: | :-: | :--- |
| Título | ✓ | ✓ | ✓ |  |
| Tipo | ✓ | · | ✓ |  |
| Fecha | ✓ | · | ✓ |  |
| DOI | ✓ | · | ✓ |  |
| URL | ✓ | · | ✓ | solo si no hay DOI |
| Archivo | ✓ | · | ✓ |  |
| Posición en archivo | ✓ | · | ✓ |  |

### Mapa (`map`, CSL `map`)

**Creadores que salen** (1.ª cita | posterior | bibliografía): Cartógrafo (✓ | ✓ | ✓).  
No salen (salvo, si no hay autor, el Editor y el Traductor, que ocupan su lugar): Contribuidor, Editor de la serie.


| Campo | 1.ª | post. | bibl. | Observación |
| :--- | :-: | :-: | :-: | :--- |
| Título | ✓ | ✓ | ✓ | en citas posteriores lo sustituye el Título corto |
| Tipo | ✓ | · | ✓ |  |
| Título de la serie | ✓ | · | ✓ |  |
| Edición | ✓ | · | ✓ |  |
| Editorial | ✓ | · | ✓ |  |
| Lugar | ✓ | · | ✓ |  |
| Fecha | ✓ | · | ✓ |  |
| DOI | ✓ | · | ✓ |  |
| URL | ✓ | · | ✓ | solo si no hay DOI |
| Archivo | ✓ | · | ✓ |  |
| Posición en archivo | ✓ | · | ✓ |  |
| Título corto | · | ✓ | · |  |

### Artículo de periódico (`newspaperArticle`, CSL `article-newspaper`)

**Creadores que salen** (1.ª cita | posterior | bibliografía): Autor (✓ | ✓ | ✓).  
No salen (salvo, si no hay autor, el Editor y el Traductor, que ocupan su lugar): Contribuidor, Traductor, Autor revisado.


| Campo | 1.ª | post. | bibl. | Observación |
| :--- | :-: | :-: | :-: | :--- |
| Título | ✓ | ✓ | ✓ | en citas posteriores lo sustituye el Título corto |
| Publicación | ✓ | · | ✓ |  |
| Fecha | ✓ | · | ✓ |  |
| Número | ✓ | · | ✓ |  |
| Páginas | ✓ | ✓ | ✓ |  |
| DOI | ✓ | · | ✓ |  |
| URL | ✓ | · | ✓ | solo si no hay DOI |
| Título corto | · | ✓ | · |  |

### Patente (`patent`, CSL `patent`)

**Creadores que salen** (1.ª cita | posterior | bibliografía): Inventor (✓ | ✓ | ✓).  
No salen (salvo, si no hay autor, el Editor y el Traductor, que ocupan su lugar): Contribuidor.


| Campo | 1.ª | post. | bibl. | Observación |
| :--- | :-: | :-: | :-: | :--- |
| Título | ✓ | ✓ | ✓ |  |
| Entidad emisora | ✓ | · | ✓ |  |
| Número de patente | ✓ | · | ✓ |  |
| Páginas | ✓ | ✓ | ✓ |  |
| Fecha de publicación | ✓ | · | ✓ |  |
| DOI | ✓ | · | ✓ |  |
| URL | ✓ | · | ✓ | solo si no hay DOI |

### Pódcast (`podcast`, CSL `broadcast`)

**Creadores que salen** (1.ª cita | posterior | bibliografía): Podcaster (✓ | · | ✓); Director (✓ | · | ✓); Traductor (✓ | ✓ | ✓).  
No salen (salvo, si no hay autor, el Editor y el Traductor, que ocupan su lugar): Invitado, Productor, Productor ejecutivo, Creador de la serie, Guionista, Miembro del reparto, Contribuidor.


| Campo | 1.ª | post. | bibl. | Observación |
| :--- | :-: | :-: | :-: | :--- |
| Título | ✓ | ✓ | ✓ |  |
| Número de episodio | ✓ | · | ✓ |  |
| Tipo de archivo | ✓ | · | ✓ |  |
| Fecha | ✓ | · | ✓ |  |
| Editorial | ✓ | · | ✓ |  |
| DOI | ✓ | · | ✓ |  |
| URL | ✓ | · | ✓ | solo si no hay DOI |

### Preimpresión (`preprint`, CSL `article`)

**Creadores que salen** (1.ª cita | posterior | bibliografía): Autor (✓ | ✓ | ✓).  
No salen (salvo, si no hay autor, el Editor y el Traductor, que ocupan su lugar): Contribuidor, Editor, Traductor, Autor revisado.


| Campo | 1.ª | post. | bibl. | Observación |
| :--- | :-: | :-: | :-: | :--- |
| Título | ✓ | ✓ | ✓ | en citas posteriores lo sustituye el Título corto |
| Género | ✓ | · | ✓ |  |
| Repositorio | ✓ | · | ✓ |  |
| ID de archivo | ✓ | · | ✓ |  |
| Lugar | ✓ | · | ✓ |  |
| Fecha | ✓ | · | ✓ |  |
| Serie | ✓ | · | ✓ |  |
| DOI | ✓ | · | ✓ |  |
| URL | ✓ | · | ✓ | solo si no hay DOI |
| Archivo | ✓ | · | ✓ |  |
| Posición en archivo | ✓ | · | ✓ |  |
| Título corto | · | ✓ | · |  |

### Presentación (`presentation`, CSL `speech`)

**Creadores que salen** (1.ª cita | posterior | bibliografía): Presentador (✓ | ✓ | ✓).  
No salen (salvo, si no hay autor, el Editor y el Traductor, que ocupan su lugar): Moderador, Organizador, Contribuidor, Traductor.


| Campo | 1.ª | post. | bibl. | Observación |
| :--- | :-: | :-: | :-: | :--- |
| Título | ✓ | ✓ | ✓ |  |
| Tipo | ✓ | · | ✓ |  |
| Fecha | ✓ | · | ✓ |  |
| Nombre de la reunión | ✓ | · | ✓ |  |
| Lugar | ✓ | · | ✓ |  |
| DOI | ✓ | · | ✓ |  |
| URL | ✓ | · | ✓ | solo si no hay DOI |

### Emisión de radio (`radioBroadcast`, CSL `broadcast`)

**Creadores que salen** (1.ª cita | posterior | bibliografía): Creador (✓ | ✓ | ✓); Entidad anfitriona (✓ | · | ✓); Director (✓ | · | ✓).  
No salen (salvo, si no hay autor, el Editor y el Traductor, que ocupan su lugar): Invitado, Productor, Productor ejecutivo, Creador de la serie, Guionista, Miembro del reparto, Traductor, Contribuidor.


| Campo | 1.ª | post. | bibl. | Observación |
| :--- | :-: | :-: | :-: | :--- |
| Título | ✓ | ✓ | ✓ |  |
| Título del programa | ✓ | · | ✓ |  |
| Número de episodio | ✓ | · | ✓ |  |
| Formato | ✓ | · | ✓ |  |
| Red | ✓ | · | ✓ |  |
| Fecha | ✓ | · | ✓ |  |
| DOI | ✓ | · | ✓ |  |
| URL | ✓ | · | ✓ | solo si no hay DOI |

### Informe (`report`, CSL `report`)

**Creadores que salen** (1.ª cita | posterior | bibliografía): Autor (✓ | ✓ | ✓).  
No salen (salvo, si no hay autor, el Editor y el Traductor, que ocupan su lugar): Editor, Contribuidor, Traductor, Editor de la serie.


| Campo | 1.ª | post. | bibl. | Observación |
| :--- | :-: | :-: | :-: | :--- |
| Título | ✓ | ✓ | ✓ | en citas posteriores lo sustituye el Título corto |
| Número de informe | ✓ | · | ✓ |  |
| Tipo de informe | ✓ | · | ✓ |  |
| Institución | ✓ | · | ✓ |  |
| Lugar | ✓ | · | ✓ |  |
| Fecha | ✓ | · | ✓ |  |
| Título de la serie | ✓ | · | ✓ |  |
| Páginas | ✓ | ✓ | · |  |
| DOI | ✓ | · | ✓ |  |
| URL | ✓ | · | ✓ | solo si no hay DOI |
| Archivo | ✓ | · | ✓ |  |
| Posición en archivo | ✓ | · | ✓ |  |
| Título corto | · | ✓ | · |  |

### Estándar (`standard`, CSL `standard`)

**Creadores que salen** (1.ª cita | posterior | bibliografía): Autor (✓ | ✓ | ✓).  
No salen (salvo, si no hay autor, el Editor y el Traductor, que ocupan su lugar): Editor, Contribuidor.


| Campo | 1.ª | post. | bibl. | Observación |
| :--- | :-: | :-: | :-: | :--- |
| Título | ✓ | ✓ | ✓ | en citas posteriores lo sustituye el Título corto |
| Organización | ✓ | · | ✓ |  |
| Tipo | ✓ | · | ✓ |  |
| Número | ✓ | · | ✓ |  |
| Versión | ✓ | · | ✓ |  |
| Edición | ✓ | · | ✓ |  |
| Fecha | ✓ | · | ✓ |  |
| Editorial | ✓ | · | ✓ |  |
| Lugar | ✓ | · | ✓ |  |
| DOI | ✓ | · | ✓ |  |
| URL | ✓ | · | ✓ | solo si no hay DOI |
| Archivo | ✓ | · | ✓ |  |
| Posición en archivo | ✓ | · | ✓ |  |
| Título corto | · | ✓ | · |  |

### Estatuto (`statute`, CSL `legislation`)

**Creadores que salen** (1.ª cita | posterior | bibliografía): Autor (✓ | ✓ | ✓).  
No salen (salvo, si no hay autor, el Editor y el Traductor, que ocupan su lugar): Contribuidor.


| Campo | 1.ª | post. | bibl. | Observación |
| :--- | :-: | :-: | :-: | :--- |
| Nombre de la ley | ✓ | ✓ | ✓ |  |
| Código | ✓ | · | ✓ |  |
| Número de código | ✓ | · | ✓ |  |
| Número de ley pública | ✓ | · | ✓ |  |
| Fecha de entrada en vigor | ✓ | · | ✓ |  |
| Páginas | ✓ | ✓ | ✓ |  |
| Sección | ✓ | · | ✓ |  |
| Sesión | ✓ | · | ✓ |  |
| DOI | ✓ | · | ✓ |  |
| URL | ✓ | · | ✓ | solo si no hay DOI |

### Tesis (`thesis`, CSL `thesis`)

**Creadores que salen** (1.ª cita | posterior | bibliografía): Autor (✓ | ✓ | ✓).  
No salen (salvo, si no hay autor, el Editor y el Traductor, que ocupan su lugar): Contribuidor.


| Campo | 1.ª | post. | bibl. | Observación |
| :--- | :-: | :-: | :-: | :--- |
| Título | ✓ | ✓ | ✓ | en citas posteriores lo sustituye el Título corto |
| Tipo | ✓ | · | ✓ |  |
| Universidad | ✓ | · | ✓ |  |
| Lugar | ✓ | · | ✓ |  |
| Fecha | ✓ | · | ✓ |  |
| DOI | ✓ | · | ✓ |  |
| URL | ✓ | · | ✓ | solo si no hay DOI |
| Título corto | · | ✓ | · |  |

### Emisión de TV (`tvBroadcast`, CSL `broadcast`)

**Creadores que salen** (1.ª cita | posterior | bibliografía): Director (✓ | · | ✓); Entidad anfitriona (✓ | · | ✓); Traductor (✓ | ✓ | ✓).  
No salen (salvo, si no hay autor, el Editor y el Traductor, que ocupan su lugar): Productor, Productor ejecutivo, Creador de la serie, Guionista, Miembro del reparto, Invitado, Narrador, Contribuidor.


| Campo | 1.ª | post. | bibl. | Observación |
| :--- | :-: | :-: | :-: | :--- |
| Título | ✓ | ✓ | ✓ |  |
| Título del programa | ✓ | · | ✓ |  |
| Número de episodio | ✓ | · | ✓ |  |
| Formato | ✓ | · | ✓ |  |
| Red | ✓ | · | ✓ |  |
| Fecha | ✓ | · | ✓ |  |
| DOI | ✓ | · | ✓ |  |
| URL | ✓ | · | ✓ | solo si no hay DOI |

### Grabación de vídeo (`videoRecording`, CSL `motion_picture`)

**Creadores que salen** (1.ª cita | posterior | bibliografía): Creador (✓ | ✓ | ✓); Director (✓ | · | ✓); Entidad anfitriona (✓ | · | ✓).  
No salen (salvo, si no hay autor, el Editor y el Traductor, que ocupan su lugar): Productor, Guionista, Productor ejecutivo, Miembro del reparto, Invitado, Narrador, Traductor, Contribuidor.


| Campo | 1.ª | post. | bibl. | Observación |
| :--- | :-: | :-: | :-: | :--- |
| Título | ✓ | ✓ | ✓ |  |
| Formato | ✓ | · | ✓ |  |
| Estudio | ✓ | · | ✓ |  |
| Lugar | ✓ | · | ✓ |  |
| Fecha | ✓ | · | ✓ |  |
| DOI | ✓ | · | ✓ |  |
| URL | ✓ | · | ✓ | solo si no hay DOI |

### Página web (`webpage`, CSL `webpage`)

**Creadores que salen** (1.ª cita | posterior | bibliografía): Autor (✓ | ✓ | ✓).  
No salen (salvo, si no hay autor, el Editor y el Traductor, que ocupan su lugar): Contribuidor, Traductor.


| Campo | 1.ª | post. | bibl. | Observación |
| :--- | :-: | :-: | :-: | :--- |
| Título | ✓ | ✓ | ✓ | en citas posteriores lo sustituye el Título corto |
| Título de página web | ✓ | · | ✓ |  |
| Tipo de página Web | ✓ | · | ✓ |  |
| Fecha | ✓ | · | ✓ |  |
| Editorial | ✓ | · | ✓ |  |
| DOI | ✓ | · | ✓ |  |
| URL | ✓ | · | ✓ | solo si no hay DOI |
| Título corto | · | ✓ | · |  |

## Limitaciones conocidas

* Las tablas indican **si** un campo sale, no el formato exacto (signos, orden). Para ver el formato, consulta `pruebas-tipos.md` y las tablas de `readme.md`.
* Que un campo salga en la «1.ª cita» no garantiza que lo haga con cualquier combinación de campos: las únicas anulaciones mutuas detectadas son las de las reglas generales y las que indica la columna «Observación».
* Mendeley y otros gestores: pendiente.
