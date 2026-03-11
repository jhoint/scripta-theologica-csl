# Scripta Definition (v1)

## Proposito
Este documento define, por escrito, el objetivo editorial minimo del estilo CSL de Scripta Theologica para guiar la migracion desde Chicago.

Se usa como referencia de aceptacion en la fase 1 (alcance) y como contrato de cambios en fases posteriores.

## Alcance
- Base tecnica: `chicago2scripta.csl`.
- Modos de salida: notas y bibliografia.
- Idioma de terminos: espanol.
- Enfoque: cambios incrementales, verificables y reversibles.

## Principios de diseno
1. Mantener la cobertura funcional de Chicago siempre que no contradiga una regla explicita de Scripta.
2. Priorizar primero forma (puntuacion/estilo), despues logica (macros/comportamiento).
3. Evitar cambios de alto impacto no validados por ejemplos reales.
4. Documentar decisiones y excepciones en `CHANGELOG.md`.

## Reglas editoriales objetivo (v1)

### 1) Presentacion tipografica
- Puntuacion y espaciado consistentes en notas y bibliografia.
- Uso consistente de mayusculas/minusculas en terminos editoriales.
- Cursiva para titulos de obra/contenedor segun tipo de fuente.
- Comillas para titulos de partes (capitulos, articulos, entradas).
- Soporte de versalitas cuando aplique (p. ej., abreviaturas de archivo).

### 2) Nombres y responsabilidades
- Separacion clara de autor, editor y traductor.
- Soporte para `dir.`/`dirs.` cuando se use `editorial-director`.
- Reglas estables para inversion de nombre en bibliografia.

### 3) Titulos y datos editoriales
- Orden estable para: titulo, edicion, volumen/tomo, serie, editorial, fecha.
- Formato coherente de volumen y tomo.
- Capitalizacion y delimitadores consistentes.

### 4) Notas al pie
- Diferenciar primera cita y citas subsecuentes.
- Controlar forma corta y `ibid` segun reglas de Scripta.
- Locators en espanol (`p.`, `pp.` y terminos aplicables).

### 5) Bibliografia
- Orden final de campos estable por tipo documental.
- Regla clara para repeticion/sustitucion de autor en entradas consecutivas.
- Puntuacion de cierre consistente.

### 6) Recursos web y acceso
- Mostrar URL o DOI con criterio consistente.
- Incluir fecha de acceso cuando exista en los datos.
- Si hay DOI valido, evitar duplicacion con URL equivalente.

### 7) Casos de archivo y manuscritos
- Soporte de documentos de archivo con formato compacto en notas.
- Conservacion de reglas actuales: no forzar inclusion automatica en bibliografia si no procede.

## Tipos de documento y plantillas (extraido de `scripta-theologica.csl`)
Esta seccion fija la forma actual del estilo para usarla como base de migracion. Las plantillas son esquemas de salida, no ejemplos literales.

### Convenciones de forma
- Autor/editor: `APELLIDO` en versalitas + `Nombre`.
- Titulo de libro/obra completa: cursiva.
- Titulo de parte (capitulo, articulo, voz): entre comillas angulares `« »`.
- Editorial: `Lugar: Editorial`.
- Revista: `Revista volumen/numero (anio)`.
- DOI: se anade al final como `https://doi.org/...`.
- URL: se introduce con `recuperado de URL`.

### 1) Libro (`book`)
- Primera nota: `APELLIDO, Nombre, Titulo en cursiva, Volumen, Edicion, Lugar: Editorial, Anio, Locator/Paginas`.
- Nota breve: `APELLIDO, Nombre, Titulo corto en cursiva, Locator/Paginas`.
- Bibliografia: `APELLIDO, Nombre, Titulo en cursiva, Volumen, Edicion, Lugar: Editorial, Anio`.

### 2) Capitulo / Ponencia (`chapter`, `paper-conference`)
- Primera nota: `APELLIDO, Nombre, "Titulo de capitulo", en APELLIDO, Nombre (autor de contenedor o editor/dir.), Titulo contenedor en cursiva, Lugar: Editorial, Anio, Locator/Paginas`.
- Nota breve: `APELLIDO, Nombre, Titulo corto, Locator/Paginas`.
- Bibliografia: `APELLIDO, Nombre, "Titulo de capitulo", en APELLIDO, Nombre (autor de contenedor o editor/dir.), Titulo contenedor en cursiva, Lugar: Editorial, Anio, Paginas`.

### 3) Articulo de revista (`article-journal`)
- Primera nota: `APELLIDO, Nombre, "Titulo de articulo", Revista en cursiva volumen/numero (Anio), Locator/Paginas`.
- Nota breve: `APELLIDO, Nombre, Titulo corto, Locator/Paginas`.
- Bibliografia: `APELLIDO, Nombre, "Titulo de articulo", Revista en cursiva volumen/numero (Anio) Paginas`.

### 4) Voz de diccionario/enciclopedia (`entry-dictionary`, `entry-encyclopedia`)
- Primera nota: `APELLIDO, Nombre, "Titulo de voz", en Obra en cursiva volumen (Anio) Locator/Paginas`.
- Nota breve: `APELLIDO, Nombre, Titulo corto`.
- Bibliografia: `APELLIDO, Nombre, "Titulo de voz", en Obra en cursiva volumen (Anio) Paginas`.

### 5) Tesis (`thesis`)
- Primera nota: `APELLIDO, Nombre, Titulo en cursiva, Genero, Lugar: Institucion, Anio, Locator/Paginas`.
- Nota breve: `APELLIDO, Nombre, Titulo corto en cursiva, Locator/Paginas`.
- Bibliografia: `APELLIDO, Nombre, Titulo en cursiva, Genero, Lugar: Institucion, Anio`.

### 6) Partitura (`musical_score`)
- Primera nota: `APELLIDO, Nombre, Titulo en cursiva, Numero, Genero, Lugar: Editorial, Anio, Locator/Paginas`.
- Nota breve: `APELLIDO, Nombre, Titulo corto, Locator/Paginas`.
- Bibliografia: `APELLIDO, Nombre, Titulo en cursiva, Numero, Genero, Lugar: Editorial, Anio`.

### 7) Grabacion de sonido (`song`)
- Primera nota: `APELLIDO, Nombre, "Titulo de pieza", en Titulo contenedor en cursiva, Numero, Medio, Genero, Lugar: Editorial, Anio, Locator/Paginas`.
- Nota breve: `APELLIDO, Nombre, Titulo corto, Locator/Paginas`.
- Bibliografia: `APELLIDO, Nombre, "Titulo de pieza", en Titulo contenedor en cursiva, Numero, Medio, Genero, Lugar: Editorial, Anio`.

### 8) Obra clasica (`classic`)
- Primera nota: `APELLIDO, Nombre, Titulo en cursiva, Locator: Coleccion Volumen`.
- Nota breve: `APELLIDO, Nombre, Titulo corto en cursiva, Locator: Coleccion-abreviada Volumen`.
- Bibliografia: `APELLIDO, Nombre, Titulo/Contenedor en cursiva, Locator: en Nombre Apellido (ed.), Coleccion Volumen, Lugar, Anio, Paginas`.

### 9) Otros tipos no especificos (`else`)
- Primera nota: `APELLIDO, Nombre, Titulo, Lugar: Editorial, Anio, Locator/Paginas`.
- Nota breve: `APELLIDO, Nombre, Titulo corto, Locator/Paginas`.
- Bibliografia: `APELLIDO, Nombre, Titulo, Lugar: Editorial, Anio`.

### Notas de implementacion observadas en el estilo actual
- El estilo actual no aplica `ibid`; en citas subsiguientes usa autor + titulo corto (+ locator si procede).
- En voces de diccionario/enciclopedia no se anade locator/paginas en nota breve.
- DOI y URL pueden coexistir en la salida (URL como `recuperado de ...` y DOI al final).

## Reglas funcionales minimas por tipo (conjunto de validacion)
Se consideran obligatorios para v1:
1. Libro (1 autor, multiples autores, con editor).
2. Capitulo en libro colectivo.
3. Articulo de revista (con y sin DOI).
4. Tesis.
5. Pagina web.
6. Manuscrito/documento de archivo.

## Criterios de aceptacion (Definition of Done v1)
Un cambio se acepta cuando:
1. Incluye justificacion breve del ajuste realizado.
2. Declara impacto esperado (que salidas cambian y cuales no).
3. Se valida con ejemplos de `pruebas-scripta.json`.
4. No introduce regresiones evidentes en notas ni bibliografia.
5. Se registra decision relevante en `CHANGELOG.md`.

## Fuentes de verdad para validacion
- `pruebas-scripta.json`: casos de prueba.
- `zotero-outputs.md`: comparacion de salidas esperadas.
- `CHANGELOG.md`: decisiones y cambios aprobados.

## Decision log (pendientes de cierre)
Estas decisiones deben cerrarse explicitamente para consolidar v1:
1. Politica exacta de comillas en titulos con comillas internas.
2. Regla final de DOI vs URL cuando ambos existen.
3. Traduccion/terminologia final de tesis doctoral.
4. Comportamiento exacto cuando falta fecha (`s.f.`) en todos los tipos relevantes.
5. Cobertura y formato final de tipos documentales pendientes listados en `cambios-a-realizar.md`.

## Ajustes contra norma oficial (2026-03-11)
Contraste realizado con: `https://revistas.unav.edu/index.php/scripta-theologica/information/authors`.

1. Repeticion de autor en bibliografia:
	En entradas consecutivas del mismo autor, se repite apellido y nombre en cada referencia (sin sustitucion por raya).

2. Patron de articulo en revista:
	Formato objetivo: `Revista volumen (anio) paginas`.

3. Obras clasicas y patristicas:
	Patron objetivo: `Autor, Obra, pasaje: serie/edicion volumen, pagina`.

4. Ciudad de edicion:
	La ciudad se mantiene en el idioma original de la edicion.

5. Politica de identificadores/enlace:
	Se prioriza DOI cuando existe; si no existe DOI, se incluye URL.

## Mapeo operativo: plantillas -> macros en `chicago2scripta.csl`
Este mapeo define donde tocar en la base Chicago para implementar Scripta sin refactor masivo.

### Bloque de nombres
- `APELLIDO, Nombre` en notas: `author-note`.
- `APELLIDO, Nombre` en bibliografia: `author-bib`.
- Forma corta de citas subsiguientes: `author-short`.
- Sustituciones cuando falta autor: `author-title-substitute-*`.

### Bloque de titulos
- Titulo principal (cursiva/comillas segun tipo): `title-primary`.
- Titulo en nota/bibliografia (envoltorio): `title-note`, `title-bib`.
- Titulo abreviado para notas breves: `title-short`, `title-primary-short`.
- Titulo de parte (capitulo/articulo/voz): `title-part`.

### Bloque fuente/editorial
- Fuente serial (revistas): `source-serial-*`.
- Fuente monografica (libros/capitulos): `source-monographic-*`.
- Datos editoriales (lugar/editorial): `source-publication-publisher-*`.
- Fecha y estado de publicacion: `source-date-*`.
- DOI/URL/acceso: `source-date-accessed-DOI-URL-*`, `source-DOI-URL`.

### Bloque de localizadores
- Etiquetas de localizador (`p.`, `pp.`, etc.): `label-locator`, `label-page`.
- Localizador en notas subsiguientes: `source-locator-subsequent-*`.
- Localizador en fuentes serial/monografica: `source-serial-locator`, `source-monographic-locator`.

### Bloque de orquestacion final
- Cita (primera vs subsiguiente): `citation-notes-full`, `citation-notes-shortened-author-title`, bloque `<citation>`.
- Bibliografia (orden y filtros): `bibliography-notes`, bloque `<bibliography>`.

## Micro-bloque 1 (solo forma, sin logica)
Objetivo: adaptar presentacion sin alterar el flujo funcional de Chicago.

### Alcance
1. Terminos en espanol para roles y localizadores habituales.
2. Comillas angulares en titulos de parte (`« »`) donde Chicago usa comillas inglesas.
3. Versalitas en apellido de autor/editor para salida visible en notas y bibliografia.
4. Ajuste visual del patron de revista hacia `Revista volumen (anio) paginas`.

### Macros candidatas para tocar en este orden
1. `author-note`, `author-bib` (solo estilo de nombre).
2. `title-primary`, `title-part`, `title-primary-short` (solo delimitadores de comillas).
3. `source-serial-identifier-bib`, `source-serial-identifier-note` (solo puntuacion/espaciado).
4. `source-date-accessed-DOI-URL-*` y `source-DOI-URL` (solo presentacion DOI/URL segun decision v1).

### Criterio de salida para cerrar micro-bloque 1
- No cambia la seleccion de campos ni el flujo primera/subsiguiente.
- Solo cambian puntuacion, comillas, terminos y estilo visual.
- Validado con un set minimo: `book`, `chapter`, `article-journal`, `entry-dictionary`, `thesis`, `classic`.

## Modo de uso del documento
- Antes de editar macros: revisar esta definicion.
- Al proponer un cambio: citar la seccion afectada.
- Al cerrar una fase: actualizar pendientes y criterios cumplidos.
