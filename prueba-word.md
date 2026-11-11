---
title: Prueba del estilo Scripta Theologica en Word
lang: es-ES
---

Documento de prueba del estilo `scripta-theologica.csl` con el complemento de Zotero para Word, y su comparación con Pandoc. Usa solo obras de `pruebas-scripta.json` y `pruebas-cmos18.json`. Cada frase lleva una cita, escrita en el texto y sin espacio delante (`texto[@clave, 20].`); el complemento de Zotero la convierte en nota al pie. Debajo de cada bloque se indica qué hay que mirar. Resultados de la primera prueba (11-11-2026): `cambios-a-realizar.md`, «Prueba en Word con el complemento de Zotero».

**Versión de Zotero (Word).** Requisitos: las obras de los dos JSON en Zotero con las mismas claves de cita (Better BibTeX), Zotero abierto y el filtro `zotero.lua` de Better BibTeX (https://retorque.re/zotero-better-bibtex/exporting/pandoc/) en esta carpeta. Comando: `pandoc prueba-word.md --lua-filter=zotero.lua -o prueba-word.docx`. En Word: Zotero → Document Preferences → Scripta Theologica, notas al pie, **sin** abreviatura automática de revistas → OK → Refresh. Después, con el cursor bajo el título «Bibliografía», Add/Edit Bibliography. El filtro no reconoce etiquetas de localizador en español («cap.») y parte los localizadores con punto («14.28»): para probar esos casos, insertar las citas con el cuadro de Zotero.

**Versión de Pandoc (referencia).** `pandoc prueba-word.md --citeproc --bibliography=pruebas-scripta.json --bibliography=pruebas-cmos18.json --csl=scripta-theologica.csl -M notes-after-punctuation=false -o prueba-word-pandoc.docx` (Pandoc 3.8.2 o posterior).

# 1. Posiciones de la cita

Primera cita de un libro[@Schmaus1961, 20]. Primera cita de un artículo[@Merino1985, 230]. Cita posterior no seguida del libro[@Schmaus1961, 22]. Cita seguida, misma página[@Schmaus1961, 22]. Cita seguida, otra página[@Schmaus1961, 25]. Cita posterior sin página[@Schmaus1961]. Dos obras en una nota, con texto delante[véase @Merino1985, 231; @Lavenia2017, 600]. Texto detrás de la cita[@Lavenia2017, 601, con matices]. Sin el autor, porque se nombra en el texto: Morales[-@Morales1998, 10].

Qué mirar: forma breve en las posteriores (el estilo no usa *ibid.*); que la cita sin página no deje «, .»; el orden de las dos obras de la misma nota; «véase» delante y «con matices» detrás; la nota sin autor.

# 2. Localizadores

Página[@Newman1887, p. 45]. Capítulo[@Newman1887, cap. 3]. Columna[@Congar1946, col. 345]. Nota[@Newman1887, n. 5]. Párrafo[@Newman1887, § 4]. Folio de un manuscrito que ya tiene el folio en Páginas[@1616, fol. 466r].

Qué mirar: si sale la etiqueta (cap., col., n., §, fol.) delante del número. En Pandoc el estilo imprime solo el número, sin etiqueta, y no se distingue de una página (problema nuevo, 11-11-2026); comprobar si en Word pasa lo mismo. En el manuscrito, Pandoc repite el folio («fol. 466r, fol. 466r»).

# 3. Revistas, obras de consulta y abreviaturas

Revista con abreviatura propia[@Merino1985, 227]. Revista sin abreviatura[@Lavenia2017, 599]. Diccionario con sigla[@Congar1946, col. 400]. Enciclopedia[@Illanes1975, 660]. Revista con serie («n.s.»)[@Kosambi1945a, 20]. Revista electrónica con número de artículo[@Dror2022]. Número monográfico con editor[@Yeh2017, S60].

Qué mirar: *ScrTh* y *DTC* abreviadas; en el diccionario, la cita posterior pierde la columna (pendiente conocido); *Journal of Jesuit Studies* entera (si sale abreviada, la abreviatura automática sigue activa); volumen (año) páginas. Pendientes conocidos: se pierden la serie «n.s.», el número de artículo y el editor del número.

# 4. Libros

Libro en alemán[@Scheffczyk1978, 12]. Libro en una serie[@Jimenez2008, 30]. Libro con autor y editor[@Adams2008, 100]. Libro traducido[@Adorno1999, 50]. Volumen de una obra en varios volúmenes[@Newman1887, 10]. Otro volumen, con título propio[@Lach1977a, 15]. Obra dentro de un volumen recopilatorio[@Baldwin2015, 450]. Prólogo de otro autor[@Wilkerson2022, xv]. Capítulo en prensa[@Contributor].

Qué mirar: pendientes conocidos del bloque A (serie, editor, traductor, título del volumen, «en prensa», volumen recopilatorio, prólogo); anotar si algo más se pierde o sale distinto que en la versión de Pandoc.

# 5. Capítulos y obras colectivas

Capítulo de obra colectiva[@Aranda1998, 421]. La obra colectiva entera[@Morales1998, 15]. Capítulo de un libro en una serie[@Rodriguez1984, 226]. Capítulo con comillas en el título[@Pellitero2007, 120]. Capítulo de una obra en varios volúmenes[@Ekbladh2021, 620]. Cita posterior del capítulo[@Aranda1998, 425].

Qué mirar: «título» en … (ed.); comillas interiores como “ ”; el volumen del capítulo (pendiente); la forma breve del capítulo.

# 6. Obras clásicas

Clásico traducido, citado por libro y capítulo[@Augustine1931, 14.28]. Clásico en edición crítica[@Epictetus1916, 1.1]. Clásico en varios volúmenes[@Dindorf1962, 2:15]. Cita posterior[@Augustine1931, 19.17].

Qué mirar: título en cursiva y sin comillas; las divisiones tal cual; la cita posterior.

# 7. Otros tipos de documento

Tesis[@Stout2021, 40]. Página web[@Brown2014]. Entrada de blog[@Saller2020]. Publicación en redes[@ChicagoManualofStyle2015]. Reseña en un periódico[@Szalai2022]. Reseña en una revista[@Ratliff1999, B13]. Manuscrito[@1616]. Carta publicada en un epistolario[@Adams1930a, 133]. Entrevista publicada[@Davis2015, 172]. Discurso[@Truman2025]. Informe[@1996, 5]. Conjunto de datos[@Zou2023]. Mapa[@SamueldeChamplain2007]. Película[@Cuaron2014]. Episodio de televisión[@Pevney1967]. Canción[@Holiday1997]. Partitura[@Verdi1998, 12]. Obra de arte[@Dali1931]. Ley[@2007]. Sentencia[@1995, 520]. Tratado[@U.K.1963, 45]. Reglamento[@2021]. Norma técnica[@Bray2006]. Folleto[@Clark1957, 3]. Fondo de archivo[@Kallen]. Documento oficial[@HMTreasury1968, 2]. Preprint[@Bodish2022]. Número entero de una revista[@Chumley2017]. Proyecto de ley[@2001].

Citas posteriores: tesis[@Stout2021, 41], carta[@Adams1930a, 134], partitura[@Verdi1998, 13], reseña[@Szalai2022], discurso[@Truman2025].

Qué mirar: que cada tipo salga completo y coherente; en la partitura, la cursiva del título en la cita posterior (pendiente conocido); en la carta, los datos del epistolario (pendiente).

# Bibliografía

::: {#refs}
:::
