# Campos que el estilo ignora: prueba con el CMOS18 test

Fecha: 2026-11-11. Estilo: `scripta-theologica.csl` (commit `b80bc67`).

Datos: 230 obras de la colección «CMOS18 test» (los ejemplos de pruebas del estilo Chicago 18 en Zotero; ver `cambios-a-realizar.md`) y 19 de las pruebas del propio estilo (`pruebas-scripta.json`, `pruebas-tipos.json`), exportadas desde Zotero en Better CSL JSON.

Método: para cada obra y cada campo relleno, se quita el campo y se vuelve a generar con citeproc-js (el motor de Zotero) la primera cita, una cita posterior y la bibliografía. Si nada cambia, el estilo ignora ese campo en esa obra. Se excluyen los campos que no se imprimen en un estilo de notas (resumen, ISBN, ISSN, idioma, signatura, licencia, fuente, Extra / Adicional, DOI y formas cortas).

«Ignorado» puede ser una decisión documentada (Accedido, Número de páginas, URL cuando hay DOI, fascículo cuando hay volumen, título completo de la revista cuando hay abreviatura) o una pérdida real. Ver `CAMPOS.md` y `cambios-a-realizar.md`.

## Resumen

| Campo (variable CSL) | CMOS18 test | Pruebas del estilo |
|---|---|---|
| `accessed` | 87 | 2 |
| `number-of-pages` | 43 | 8 |
| `container-title` | 36 | 2 |
| `URL` | 34 | 1 |
| `collection-title` | 20 | 10 |
| `issue` | 24 | 3 |
| `editor` | 21 | 0 |
| `publisher` | 16 | 3 |
| `collection-number` | 8 | 8 |
| `dimensions` | 15 | 0 |
| `number-of-volumes` | 14 | 0 |
| `contributor` | 12 | 1 |
| `collection-editor` | 12 | 0 |
| `status` | 11 | 0 |
| `section` | 11 | 0 |
| `volume-title` | 11 | 0 |
| `event-date` | 10 | 0 |
| `translator` | 10 | 0 |
| `volume` | 7 | 1 |
| `medium` | 8 | 0 |
| `page` | 7 | 0 |
| `available-date` | 6 | 0 |
| `archive` | 5 | 0 |
| `number` | 5 | 0 |
| `publisher-place` | 2 | 3 |
| `genre` | 5 | 0 |
| `original-date` | 4 | 0 |
| `chapter-number` | 4 | 0 |
| `reviewed-author` | 4 | 0 |
| `edition` | 3 | 0 |
| `references` | 3 | 0 |
| `composer` | 3 | 0 |
| `reviewed-title` | 3 | 0 |
| `compiler` | 2 | 0 |
| `supplement-number` | 2 | 0 |
| `part-number` | 2 | 0 |
| `event-place` | 2 | 0 |
| `event-title` | 2 | 0 |
| `narrator` | 1 | 0 |
| `illustrator` | 1 | 0 |
| `interviewer` | 1 | 0 |
| `container-author` | 1 | 0 |
| `part-title` | 1 | 0 |
| `producer` | 1 | 0 |
| `chair` | 1 | 0 |
| `reviewed-genre` | 1 | 0 |
| `scale` | 1 | 0 |

## Detalle por campo

### `accessed` (89)

| Grupo | Clave | Tipo CSL | Valor |
|---|---|---|---|
| CMOS18 test | Bodish2022 | article | {"date-parts":[["2025",2,25]]} |
| CMOS18 test | Fiallo2022 | article | {"date-parts":[["2025",4,25]]} |
| CMOS18 test | Acharya2022 | article-journal | {"date-parts":[["2025",3,31]]} |
| CMOS18 test | Ahmad2022 | article-journal | {"date-parts":[["2025",3,17]]} |
| CMOS18 test | Arterburn2022 | article-journal | {"date-parts":[["2025",3,31]]} |
| CMOS18 test | Aucejo2022 | article-journal | {"date-parts":[["2025",3,7]]} |
| CMOS18 test | Beattie1974 | article-journal | {"date-parts":[["2025",2,5]]} |
| CMOS18 test | Brown1978 | article-journal | {"date-parts":[["2025",3,16]]} |
| CMOS18 test | Brown1978a | article-journal | {"date-parts":[["2025",3,16]]} |
| CMOS18 test | Chan2025 | article-journal | {"date-parts":[["2025",3,7]]} |
| CMOS18 test | Dittmar2023 | article-journal | {"date-parts":[["2025",2,24]]} |
| CMOS18 test | Dong2022 | article-journal | {"date-parts":[["2025",3,18]]} |
| CMOS18 test | Dror2022 | article-journal | {"date-parts":[["2025",4,17]]} |
| CMOS18 test | Duan2022 | article-journal | {"date-parts":[["2025",3,2]]} |
| CMOS18 test | Fogel2004a | article-journal | {"date-parts":[["2025",3,3]]} |
| CMOS18 test | Friedkin2025 | article-journal | {"date-parts":[["2025",3,31]]} |
| CMOS18 test | Garaud1967 | article-journal | {"date-parts":[["2025",3,3]]} |
| CMOS18 test | Garrett1975 | article-journal | {"date-parts":[["2025",3,16]]} |
| CMOS18 test | Lee1896 | article-journal | {"date-parts":[["2025",3,17]]} |
| CMOS18 test | Ma2022a | article-journal | {"date-parts":[["2025",4,13]]} |
| CMOS18 test | Palmatary1949 | article-journal | {"date-parts":[["2025",4,14]]} |
| CMOS18 test | Riedener2022 | article-journal | {"date-parts":[["2025",3,7]]} |
| CMOS18 test | Snyder2025 | article-journal | {"date-parts":[["2026",1,28]]} |
| CMOS18 test | Stoffle2000 | article-journal | {"date-parts":[["2025",3,17]]} |
| CMOS18 test | Takimoto2022 | article-journal | {"date-parts":[["2025",3,17]]} |
| CMOS18 test | Tessler2014 | article-journal | {"date-parts":[["2025",4,18]]} |
| CMOS18 test | Wilder2013 | article-journal | {"date-parts":[["2025",3,7]]} |
| CMOS18 test | Yeh2017 | article-journal | {"date-parts":[["2025",3,16]]} |
| CMOS18 test | Zhao2023 | article-journal | {"date-parts":[["2025",3,7]]} |
| CMOS18 test | Davis2015a | article-magazine | {"date-parts":[["2025",3,18]]} |
| CMOS18 test | Mead2023a | article-magazine | {"date-parts":[["2025",4,25]]} |
| CMOS18 test | Ratliff1999 | article-magazine | {"date-parts":[["2025",3,18]]} |
| CMOS18 test | Ratliff1999a | article-magazine | {"date-parts":[["2025",3,18]]} |
| CMOS18 test | St.Felix2022 | article-magazine | {"date-parts":[["2025",3,18]]} |
| CMOS18 test | Wallraff2025 | article-magazine | {"date-parts":[["2025",3,18]]} |
| CMOS18 test | Apple1974 | article-newspaper | {"date-parts":[["2025",3,14]]} |
| CMOS18 test | Belson2022 | article-newspaper | {"date-parts":[["2025",3,31]]} |
| CMOS18 test | Bergner2022 | article-newspaper | {"date-parts":[["2025",3,18]]} |
| CMOS18 test | Blum2023 | article-newspaper | {"date-parts":[["2025",2,24]]} |
| CMOS18 test | Chang2022 | article-newspaper | {"date-parts":[["2025",3,18]]} |
| CMOS18 test | Laffin2022 | article-newspaper | {"date-parts":[["2025",2,26]]} |
| CMOS18 test | Samenow2016 | article-newspaper | {"date-parts":[["2025",3,14]]} |
| CMOS18 test | Szalai2022 | article-newspaper | {"date-parts":[["2025",3,18]]} |
| CMOS18 test | Tommasini2021 | article-newspaper | {"date-parts":[["2025",3,30]]} |
| CMOS18 test | Viren2022 | article-newspaper | {"date-parts":[["2025",3,18]]} |
| CMOS18 test | Armstrong2014 | book | {"date-parts":[["2025",3,6]]} |
| CMOS18 test | Austen1811 | book | {"date-parts":[["2025",4,24]]} |
| CMOS18 test | Eliot1968 | book | {"date-parts":[["2025",3,3]]} |
| CMOS18 test | Fogel2004 | book | {"date-parts":[["2025",3,3]]} |
| CMOS18 test | Palmatary1950 | book | {"date-parts":[["2025",4,14]]} |
| CMOS18 test | Schweitzer1966 | book | {"date-parts":[["2025",2,26]]} |
| CMOS18 test | Sterling2021 | book | {"date-parts":[["2025",3,3]]} |
| CMOS18 test | Sunya2022 | book | {"date-parts":[["2025",3,30]]} |
| CMOS18 test | Whitman1855 | book | {"date-parts":[["2025",3,6]]} |
| CMOS18 test | Wilde2022 | book | {"date-parts":[["2025",7,8]]} |
| CMOS18 test | Thomas2022 | broadcast | {"date-parts":[["2025",3,11]]} |
| CMOS18 test | Vallier2021 | chapter | {"date-parts":[["2025",3,5]]} |
| CMOS18 test | Augustine1931 | classic | {"date-parts":[["2025",7,1]]} |
| CMOS18 test | MITElectionDataandScienceLab2022 | dataset | {"date-parts":[["2025",4,30]]} |
| CMOS18 test | USBureauofLaborStatistics2023 | dataset | {"date-parts":[["2023",6,9]]} |
| CMOS18 test | Zou2023 | dataset | {"date-parts":[["2025",4,30]]} |
| CMOS18 test | 2025a | entry-dictionary | {"date-parts":[["2025",4,29]]} |
| CMOS18 test | 2025 | entry-encyclopedia | {"date-parts":[["2025",3,13]]} |
| CMOS18 test | Piras2013 | entry-encyclopedia | {"date-parts":[["2025",3,13]]} |
| CMOS18 test | Dali1931 | graphic | {"date-parts":[["2025",2,26]]} |
| CMOS18 test | Picasso1942 | graphic | {"date-parts":[["2025",4,30]]} |
| CMOS18 test | Buolamwini2023 | interview | {"date-parts":[["2025",2,24]]} |
| CMOS18 test | Davis2015 | interview | {"date-parts":[["2025",3,18]]} |
| CMOS18 test | O2022 | interview | {"date-parts":[["2025",3,18]]} |
| CMOS18 test | USGeologicalSurvey1951 | map | {"date-parts":[["2025",3,31]]} |
| CMOS18 test | Chumley2017 | periodical | {"date-parts":[["2025",3,16]]} |
| CMOS18 test | ChicagoManualofStyle2015 | post | {"date-parts":[["2025",2,24]]} |
| CMOS18 test | Souza2022 | post | {"date-parts":[["2025",2,25]]} |
| CMOS18 test | Saller2020 | post-weblog | {"date-parts":[["2025",2,26]]} |
| CMOS18 test | Holiday1997 | song | {"date-parts":[["2025",5,1]]} |
| CMOS18 test | OrchestraandChorusoftheRoyalOperaHouseCoventGarden1991 | song | {"date-parts":[["2025",4,14]]} |
| CMOS18 test | Cowan2022 | speech | {"date-parts":[["2025",2,24]]} |
| CMOS18 test | Oliver2022 | speech | {"date-parts":[["2025",2,24]]} |
| CMOS18 test | Truman2025 | speech | {"date-parts":[["2025",4,11]]} |
| CMOS18 test | Bray2006 | standard | {"date-parts":[["2025",4,11]]} |
| CMOS18 test | BlajerdelaGarza2019 | thesis | {"date-parts":[["2025",2,24]]} |
| CMOS18 test | Stout2021 | thesis | {"date-parts":[["2025",3,18]]} |
| CMOS18 test | Tauber1958 | thesis | {"date-parts":[["2025",3,5]]} |
| CMOS18 test | Vedrashko2006 | thesis | {"date-parts":[["2025",2,25]]} |
| CMOS18 test | 2023a | webpage | {"date-parts":[["2025",8,31]]} |
| CMOS18 test | Brown2014 | webpage | {"date-parts":[["2025",5,25]]} |
| CMOS18 test | USGovernmentPublishingOffice2022 | webpage | {"date-parts":[["2025",3,18]]} |
| pruebas del estilo | Lavenia2017 | article-journal | {"date-parts":[["2026",2,12]]} |
| pruebas del estilo | Parenti2012 | post-weblog | {"date-parts":[["2026",2,12]]} |

### `number-of-pages` (51)

| Grupo | Clave | Tipo CSL | Valor |
|---|---|---|---|
| CMOS18 test | 2017 | book | 384 |
| CMOS18 test | Adorno1999 | book | 383 |
| CMOS18 test | Aristotle1984 | book | 1 |
| CMOS18 test | Aubrecht2020 | book | 286 |
| CMOS18 test | Austen2012 | book | 560 |
| CMOS18 test | Bernhard1990 | book | 282 |
| CMOS18 test | Borel2023 | book | 239 |
| CMOS18 test | Boxer1953 | book | xci+388 |
| CMOS18 test | Braverman2020 | book | 342 |
| CMOS18 test | Carson1962 | book | x+368 |
| CMOS18 test | Child2020 | book | 351 |
| CMOS18 test | Cochrane1987 | book | 608 |
| CMOS18 test | Conway2013 | book | 1 |
| CMOS18 test | Costello1981 | book | 281 |
| CMOS18 test | Derrida2016 | book | 1 |
| CMOS18 test | Devesa2022 | book | 188 |
| CMOS18 test | Einsohn2019 | book | 545 |
| CMOS18 test | Eliot1968 | book | 490 |
| CMOS18 test | Ellison1995 | book | 581 |
| CMOS18 test | Emerson1985 | book | 66 |
| CMOS18 test | Errington2002 | book | 32 |
| CMOS18 test | Euripides2013 | book | 5 |
| CMOS18 test | Ferrer2022 | book | 560 |
| CMOS18 test | Ferreras2022 | book | 133 |
| CMOS18 test | Fitzgerald1992 | book | 216 |
| CMOS18 test | GarciaMarquez1988 | book | 348 |
| CMOS18 test | Goldman2008 | book | 470 |
| CMOS18 test | Jovin2022a | book | 374 |
| CMOS18 test | Lach1977a | book | 442 |
| CMOS18 test | Pirumova1977 | book | 285 |
| CMOS18 test | Roy2008 | book | 333 |
| CMOS18 test | Schweitzer1966 | book | 554 |
| CMOS18 test | Shakespeare1988 | book | 182 |
| CMOS18 test | Shakespeare2005 | book | 1344 |
| CMOS18 test | Shakespeare2005a | book | 1344 |
| CMOS18 test | Silverstein1974 | book | 121 |
| CMOS18 test | Solinger2019 | book | 1 |
| CMOS18 test | Soyinka2021 | book | 321 |
| CMOS18 test | Turabian2018 | book | 462 |
| CMOS18 test | Wereszycki2010 | book | 1 |
| CMOS18 test | Winther2020 | book | 318 |
| CMOS18 test | Augustine1931 | classic | 458 |
| CMOS18 test | Propertius1990 | classic | 440 |
| pruebas del estilo | Fernandez1979a | book | 261 |
| pruebas del estilo | Jimenez2008 | book | 279 |
| pruebas del estilo | Morales1998 | book | 651 |
| pruebas del estilo | Pellitero2007a | book | 186 |
| pruebas del estilo | Rodriguez1982 | book | 498 |
| pruebas del estilo | Saranyana1984 | book | 443 |
| pruebas del estilo | Scheffczyk1978 | book | 381 |
| pruebas del estilo | Schmaus1961 | book | 894 |

### `container-title` (38)

| Grupo | Clave | Tipo CSL | Valor |
|---|---|---|---|
| CMOS18 test | Acharya2022 | article-journal | Economic Development and Cultural Change |
| CMOS18 test | Ahmad2022 | article-journal | Journal of Geology |
| CMOS18 test | Arterburn2022 | article-journal | Biological Bulletin |
| CMOS18 test | Aucejo2022 | article-journal | Journal of Human Capital |
| CMOS18 test | Author2023 | article-journal | Journal Title |
| CMOS18 test | Beattie1974 | article-journal | Past and Present |
| CMOS18 test | Brown1978 | article-journal | Wisconsin Magazine of History |
| CMOS18 test | Brown1978a | article-journal | Wisconsin Magazine of History |
| CMOS18 test | Chan2025 | article-journal | Journal of Labor Economics |
| CMOS18 test | Dittmar2023 | article-journal | American Naturalist |
| CMOS18 test | Dong2022 | article-journal | Critical Inquiry |
| CMOS18 test | Dror2022 | article-journal | PLOS ONE |
| CMOS18 test | Duan2022 | article-journal | Environmental History |
| CMOS18 test | Fogel2004a | article-journal | Journal of Evolutionary Economics |
| CMOS18 test | Friedkin2025 | article-journal | Social Networks |
| CMOS18 test | Garaud1967 | article-journal | Bulletin de la Société des antiquaires de l’Ouest |
| CMOS18 test | Garrett1975 | article-journal | Victorian Poetry |
| CMOS18 test | Kosambi1945a | article-journal | Journal of the Bombay Branch of the Royal Asiatic Society |
| CMOS18 test | Lee1896 | article-journal | Proceedings of the Massachusetts Historical Society |
| CMOS18 test | Ma2022a | article-journal | Critical Inquiry |
| CMOS18 test | Palmatary1949 | article-journal | Transactions of the American Philosophical Society |
| CMOS18 test | Riedener2022 | article-journal | Ethics |
| CMOS18 test | Smitha | article-journal | Journal Title |
| CMOS18 test | Snyder2025 | article-journal | PLOS ONE |
| CMOS18 test | Stoffle2000 | article-journal | Current Anthropology |
| CMOS18 test | Takimoto2022 | article-journal | American Naturalist |
| CMOS18 test | Tessler2014 | article-journal | Freshwater Science |
| CMOS18 test | Wilder2013 | article-journal | Renaissance Drama |
| CMOS18 test | Yeh2017 | article-journal | Signs and Society |
| CMOS18 test | Zhao2023 | article-journal | China Journal |
| CMOS18 test | Baldwin2015 | book | James Baldwin: Later novels |
| CMOS18 test | Bernhard1990 | book | Histrionics: three plays |
| CMOS18 test | Euripides2013 | book | Euripides IV |
| CMOS18 test | Shakespeare2005a | book | The complete works |
| CMOS18 test | Adams1930a | personal_communication | Letters of Henry Adams (1858–1918) |
| CMOS18 test | White1975 | personal_communication | Letters of E. B. White |
| pruebas del estilo | Merino1985 | article-journal | Scripta theologica |
| pruebas del estilo | Congar1946 | entry-dictionary | Dictionnaire de théologie catholique |

### `URL` (35)

| Grupo | Clave | Tipo CSL | Valor |
|---|---|---|---|
| CMOS18 test | Bodish2022 | article | https://arxiv.org/abs/2209.01672 |
| CMOS18 test | Fiallo2022 | article | https://osf.io/p723u_v1 |
| CMOS18 test | Acharya2022 | article-journal | https://www.journals.uchicago.edu/doi/10.1086/713883 |
| CMOS18 test | Ahmad2022 | article-journal | https://www.journals.uchicago.edu/doi/10.1086/719333 |
| CMOS18 test | Arterburn2022 | article-journal | https://www.journals.uchicago.edu/doi/10.1086/720151 |
| CMOS18 test | Aucejo2022 | article-journal | https://www.journals.uchicago.edu/doi/10.1086/719731 |
| CMOS18 test | Beattie1974 | article-journal | https://www.jstor.org/stable/650463 |
| CMOS18 test | Chan2025 | article-journal | https://www.journals.uchicago.edu/doi/10.1086/724157 |
| CMOS18 test | Dittmar2023 | article-journal | https://www.journals.uchicago.edu/doi/10.1086/725865 |
| CMOS18 test | Dong2022 | article-journal | https://www.journals.uchicago.edu/doi/10.1086/719895 |
| CMOS18 test | Dror2022 | article-journal | https://dx.plos.org/10.1371/journal.pone.0263069 |
| CMOS18 test | Duan2022 | article-journal | https://www.journals.uchicago.edu/doi/10.1086/719781 |
| CMOS18 test | Fogel2004a | article-journal | https://doi.org/10.1007/s00191-004-0188-x |
| CMOS18 test | Friedkin2025 | article-journal | https://linkinghub.elsevier.com/retrieve/pii/037887339290002O |
| CMOS18 test | Ma2022a | article-journal | https://www.journals.uchicago.edu/doi/10.1086/721173 |
| CMOS18 test | Palmatary1949 | article-journal | https://www.jstor.org/stable/1005648 |
| CMOS18 test | Riedener2022 | article-journal | https://www.journals.uchicago.edu/doi/10.1086/718080 |
| CMOS18 test | Snyder2025 | article-journal | https://dx.plos.org/10.1371/journal.pone.0318239 |
| CMOS18 test | Stoffle2000 | article-journal | http://www.journals.uchicago.edu/doi/10.1086/300101 |
| CMOS18 test | Takimoto2022 | article-journal | https://www.journals.uchicago.edu/doi/10.1086/720403 |
| CMOS18 test | Tessler2014 | article-journal | https://www.journals.uchicago.edu/doi/10.1086/676996 |
| CMOS18 test | Wilder2013 | article-journal | https://www.journals.uchicago.edu/doi/10.1086/673907 |
| CMOS18 test | Yeh2017 | article-journal | https://www.cambridge.org/core/product/identifier/S2326448900001021/type/journal |
| CMOS18 test | Zhao2023 | article-journal | https://www.journals.uchicago.edu/doi/10.1086/722215 |
| CMOS18 test | Fogel2004 | book | https://www.cambridge.org/core/books/escape-from-hunger-and-premature-death-1700 |
| CMOS18 test | Palmatary1950 | book | https://www.jstor.org/stable/1005648 |
| CMOS18 test | Sterling2021 | book | https://www.jstor.org/stable/10.2307/j.ctv1h9dkgt |
| CMOS18 test | Sunya2022 | book | https://luminosoa.org/site/books/m/10.1525/luminos.130/ |
| CMOS18 test | Wilde2022 | book | http://www.jstor.org/stable/10.2307/j.ctv310vj6p |
| CMOS18 test | Vallier2021 | chapter | https://doi.org/10.1093/oso/9780190887223.005.0002 |
| CMOS18 test | MITElectionDataandScienceLab2022 | dataset | https://dataverse.harvard.edu/citation?persistentId=doi:10.7910/DVN/ER9XTV |
| CMOS18 test | Zou2023 | dataset | https://datadryad.org/dataset/doi:10.5061/dryad.sbcc2frb4 |
| CMOS18 test | 2025a | entry-dictionary | https://oed.com/dictionary/hootenanny_n |
| CMOS18 test | Piras2013 | entry-encyclopedia | https://www.oxfordmusiconline.com/grovemusic/documentID/omo-9781561592630-e-1002 |
| pruebas del estilo | Lavenia2017 | article-journal | https://brill.com/view/journals/jjs/4/4/article-p599_599.xml |

### `collection-title` (30)

| Grupo | Clave | Tipo CSL | Valor |
|---|---|---|---|
| CMOS18 test | Garaud1967 | article-journal | 4th ser. |
| CMOS18 test | Kosambi1945a | article-journal | n.s. |
| CMOS18 test | Lee1896 | article-journal | 2nd ser. |
| CMOS18 test | Palmatary1949 | article-journal | n.s. |
| CMOS18 test | 1803 | book | 1st series |
| CMOS18 test | Allen2009 | book | Women in culture and society |
| CMOS18 test | Aristotle1984 | book | Bollingen Series |
| CMOS18 test | Aubrecht2020 | book | Disability culture and politics |
| CMOS18 test | Boxer1953 | book | Hakluyt Society Publications |
| CMOS18 test | Cochrane1987 | book | Readings in Western civilization |
| CMOS18 test | Derrida2016 | book | The Seminars of Jacques Derrida |
| CMOS18 test | Devesa2022 | book | L'un et l'autre en français |
| CMOS18 test | Euripides2013 | book | The complete Greek tragedies |
| CMOS18 test | FerrerBenimeli1976 | book | Publicaciones de la Fundación universitaria española |
| CMOS18 test | Fogel2004 | book | Cambridge Studies in Population, Economy and Society in Past Time |
| CMOS18 test | Goldman2008 | book | Oxford world's classics |
| CMOS18 test | Palmatary1950 | book | Transactions of the American Philosophical Society |
| CMOS18 test | Wauchope1950 | book | Middle American Research Records |
| CMOS18 test | Wereszycki2010 | book | Klasyka Polskiej Historiografii |
| CMOS18 test | Verdi1998 | musical_score | The Works of Giuseppe Verdi |
| pruebas del estilo | Jimenez2008 | book | Monografías |
| pruebas del estilo | Morales1998 | book | Simposios Internacionales de Teología de la Universidad de Navarra |
| pruebas del estilo | Pellitero2007a | book | Cuestiones fundamentales |
| pruebas del estilo | Rodriguez1982 | book | Colección Teológica de la Universidad de Navarra |
| pruebas del estilo | Saranyana1984 | book | Colección Teológica de la Universidad de Navarra |
| pruebas del estilo | Schmaus1961 | book | Manuales de la Biblioteca del Pensamiento Actual |
| pruebas del estilo | Aranda1998 | chapter | Simposios Internacionales de Teología de la Universidad de Navarra |
| pruebas del estilo | MartinezCamino2008 | chapter | Monografías |
| pruebas del estilo | Pellitero2007 | chapter | Cuestiones fundamentales |
| pruebas del estilo | Rodriguez1984 | chapter | Colección Teológica de la Universidad de Navarra |

### `issue` (27)

| Grupo | Clave | Tipo CSL | Valor |
|---|---|---|---|
| CMOS18 test | Acharya2022 | article-journal | 2 |
| CMOS18 test | Ahmad2022 | article-journal | 3 |
| CMOS18 test | Arterburn2022 | article-journal | 3 |
| CMOS18 test | Aucejo2022 | article-journal | 3 |
| CMOS18 test | Author2023 | article-journal | 3 |
| CMOS18 test | Brown1978 | article-journal | 4 |
| CMOS18 test | Brown1978a | article-journal | 1 |
| CMOS18 test | Dittmar2023 | article-journal | 4 |
| CMOS18 test | Dong2022 | article-journal | 4 |
| CMOS18 test | Dror2022 | article-journal | 2 |
| CMOS18 test | Duan2022 | article-journal | 3 |
| CMOS18 test | Fogel2004a | article-journal | 2 |
| CMOS18 test | Friedkin2025 | article-journal | 3–4 |
| CMOS18 test | Garrett1975 | article-journal | 1 |
| CMOS18 test | Ma2022a | article-journal | 1 |
| CMOS18 test | Palmatary1949 | article-journal | 3 |
| CMOS18 test | Riedener2022 | article-journal | 3 |
| CMOS18 test | Snyder2025 | article-journal | 3 |
| CMOS18 test | Stoffle2000 | article-journal | 1 |
| CMOS18 test | Takimoto2022 | article-journal | 3 |
| CMOS18 test | Tessler2014 | article-journal | 3 |
| CMOS18 test | Wilder2013 | article-journal | 1–2 |
| CMOS18 test | Wauchope1950 | book | 14 |
| CMOS18 test | Davis2015 | interview | 212 |
| pruebas del estilo | Brady1951 | article-journal | 3/4 |
| pruebas del estilo | Lavenia2017 | article-journal | 4 |
| pruebas del estilo | Merino1985 | article-journal | 1 |

### `editor` (21)

| Grupo | Clave | Tipo CSL | Valor |
|---|---|---|---|
| CMOS18 test | Dror2022 | article-journal | [{"family":"Jin","given":"Dong-Yan"}] |
| CMOS18 test | Friedkin2025 | article-journal | [{"family":"Willer","given":"David"}] |
| CMOS18 test | Snyder2025 | article-journal | [{"family":"Schubert","given":"Michael"}] |
| CMOS18 test | Yeh2017 | article-journal | [{"family":"Chumley","given":"Lily"}] |
| CMOS18 test | Adams1930 | book | [{"family":"Ford","given":"Worthington Chauncey"}] |
| CMOS18 test | Adams2008 | book | [{"family":"Chalfant","given":"Edward"},{"family":"Wright","given":"Conrad Edick |
| CMOS18 test | Adorno1999 | book | [{"family":"Lonitz","given":"Henri"}] |
| CMOS18 test | Aristotle1984 | book | [{"family":"Barnes","given":"Jonathan"}] |
| CMOS18 test | Austen2012 | book | [{"family":"Tandon","given":"Bharat"}] |
| CMOS18 test | Baldwin2015 | book | [{"family":"Pinckney","given":"Darryl"}] |
| CMOS18 test | Derrida2016 | book | [{"family":"Dutoit","given":"Thomas"}] |
| CMOS18 test | Donne1995 | book | [{"family":"Stringer","given":"Gary A."},{"family":"Pebworth","given":"Ted-Larry |
| CMOS18 test | Euripides2013 | book | [{"family":"Grene","given":"David"},{"family":"Lattimore","given":"Richmond"}] |
| CMOS18 test | Shakespeare1988 | book | [{"family":"Bevington","given":"David M."}] |
| CMOS18 test | Shakespeare2005 | book | [{"family":"Wells","given":"Stanley"},{"family":"Taylor","given":"Gary"},{"famil |
| CMOS18 test | Shakespeare2005a | book | [{"family":"Wells","given":"Stanley"},{"family":"Taylor","given":"Gary"},{"famil |
| CMOS18 test | Turabian2018 | book | [{"family":"Booth","given":"Wayne C."},{"family":"Colomb","given":"Gregory G."}, |
| CMOS18 test | White1976 | book | [{"family":"Guth","given":"Dorothy Lobrano"}] |
| CMOS18 test | Wilde2022 | book | [{"family":"Frankel","given":"Nicholas"}] |
| CMOS18 test | Verdi1998 | musical_score | [{"family":"Hudson","given":"Elizabeth"}] |
| CMOS18 test | White1975 | personal_communication | [{"family":"Guth","given":"Dorothy Lobrano"}] |

### `publisher` (19)

| Grupo | Clave | Tipo CSL | Valor |
|---|---|---|---|
| CMOS18 test | Brown1978 | article-journal | Wisconsin Historical Society |
| CMOS18 test | Brown1978a | article-journal | Wisconsin Historical Society |
| CMOS18 test | Garrett1975 | article-journal | West Virginia University Press |
| CMOS18 test | Lee1896 | article-journal | Massachusetts Historical Society |
| CMOS18 test | Ma2022a | article-journal | The University of Chicago Press |
| CMOS18 test | Palmatary1949 | article-journal | American Philosophical Society |
| CMOS18 test | Davis2015a | article-magazine | The Paris Review Writing and Editing |
| CMOS18 test | Augustine1931 | classic | Dutton |
| CMOS18 test | Epictetus1916 | classic | Teubner |
| CMOS18 test | Propertius1990 | classic | Harvard University Press |
| CMOS18 test | Piras2013 | entry-encyclopedia | Oxford University Press |
| CMOS18 test | Bundy1990 | interview | PBS |
| CMOS18 test | Buolamwini2023 | interview | NPR |
| CMOS18 test | Adams1930a | personal_communication | Houghton Mifflin |
| CMOS18 test | White1975 | personal_communication | Harper and Row |
| CMOS18 test | Truman2025 | speech | Miller Center of Public Affairs, University of Virginia |
| pruebas del estilo | Brady1951 | article-journal | Franciscan Institute |
| pruebas del estilo | Merino1985 | article-journal | University of Navarre |
| pruebas del estilo | Illanes1975 | entry-encyclopedia | Rialp |

### `collection-number` (16)

| Grupo | Clave | Tipo CSL | Valor |
|---|---|---|---|
| CMOS18 test | Aristotle1984 | book | 192 |
| CMOS18 test | Boxer1953 | book | 2nd ser., vol. 106 |
| CMOS18 test | Cochrane1987 | book | 6 |
| CMOS18 test | FerrerBenimeli1976 | book | Monografías 17 |
| CMOS18 test | Palmatary1950 | book | n.s., vol. 39, pt. 3 (1949) |
| CMOS18 test | Wauchope1950 | book | 1 |
| CMOS18 test | Propertius1990 | classic | 18 |
| CMOS18 test | Verdi1998 | musical_score | Series I: Operas |
| pruebas del estilo | Jimenez2008 | book | 119 |
| pruebas del estilo | Morales1998 | book | 18 |
| pruebas del estilo | Rodriguez1982 | book | 35 |
| pruebas del estilo | Saranyana1984 | book | 40 |
| pruebas del estilo | Schmaus1961 | book | 4 |
| pruebas del estilo | Aranda1998 | chapter | 18 |
| pruebas del estilo | MartinezCamino2008 | chapter | 119 |
| pruebas del estilo | Rodriguez1984 | chapter | 40 |

### `dimensions` (15)

| Grupo | Clave | Tipo CSL | Valor |
|---|---|---|---|
| CMOS18 test | Laffin2022 | article-newspaper | 4 min., 15 sec. |
| CMOS18 test | Mayberry1971 | broadcast | 26m |
| CMOS18 test | Pevney1967 | broadcast | 50m |
| CMOS18 test | Zou2023 | dataset | 562778999 bytes |
| CMOS18 test | Dali1931 | graphic | 9½ × 13 in. (24.1 × 33 cm) |
| CMOS18 test | Picasso1942 | graphic | 33.5 × 43.5 × 19 cm |
| CMOS18 test | Buolamwini2023 | interview | 37:58 |
| CMOS18 test | SamueldeChamplain2007 | map | 43 × 76 cm |
| CMOS18 test | Cuaron2014 | motion_picture | 1h31m |
| CMOS18 test | AtlantaSymphonyOrchestraandChamberChorus1988 | song | 141 min |
| CMOS18 test | Coolidge | speech | 4 min., 40 sec. |
| CMOS18 test | Cowan2022 | speech | 9 min., 15 sec. |
| CMOS18 test | Oliver2022 | speech | 1:01:45 |
| CMOS18 test | Roosevelt1959 | speech | 1:12:49 |
| CMOS18 test | Truman2025 | speech | 18:13 |

### `number-of-volumes` (14)

| Grupo | Clave | Tipo CSL | Valor |
|---|---|---|---|
| CMOS18 test | Adams1930 | book | 2 |
| CMOS18 test | Aristotle1984 | book | 2 |
| CMOS18 test | Austen1811 | book | 3 |
| CMOS18 test | Blower2021 | book | 4 |
| CMOS18 test | Byrne1981 | book | 6 |
| CMOS18 test | FerrerBenimeli1976 | book | 4 |
| CMOS18 test | Lach1977a | book | 3 vols. in 9 bks. |
| CMOS18 test | Schweitzer1966 | book | 2 |
| CMOS18 test | Tillich1961 | book | 3 |
| CMOS18 test | deCervantesSaavedra1605 | book | 2 |
| CMOS18 test | Ekbladh2021 | chapter | 4 |
| CMOS18 test | Dindorf1962 | classic | 2 |
| CMOS18 test | Verdi1998 | musical_score | 2 |
| CMOS18 test | Adams1930a | personal_communication | 2 |

### `contributor` (13)

| Grupo | Clave | Tipo CSL | Valor |
|---|---|---|---|
| CMOS18 test | Angle1968 | book | [{"family":"Burnett","given":"Virgil"},{"family":"Long","given":"Barbara"}] |
| CMOS18 test | Cacchione2017 | book | [{"family":"Li","given":"Pi"},{"family":"Farrell","given":"Robyn"},{"family":"Gr |
| CMOS18 test | Conway2013 | book | [{"family":"Scovell","given":"Jane"},{"family":"Burnett","given":"Carol"}] |
| CMOS18 test | Derrida2016 | book | [{"family":"Derrida","given":"Marguerite"}] |
| CMOS18 test | Schweitzer1966 | book | [{"family":"Widor","given":"C. M."}] |
| CMOS18 test | Mayberry1971 | broadcast | [{"family":"Reed","given":"Robert"},{"family":"Henderson","given":"Florence"},{" |
| CMOS18 test | Pevney1967 | broadcast | [{"family":"Shatner","given":"William"},{"family":"Nimoy","given":"Leonard"},{"f |
| CMOS18 test | MITElectionDataandScienceLab2022 | dataset | [{"family":"Baltz","given":"Samuel"},{"family":"Chin","given":"Declan"},{"family |
| CMOS18 test | Verdi1998 | musical_score | [{"family":"Gossett","given":"Philip"}] |
| CMOS18 test | Holiday1997 | song | [{"family":"Herron","given":"Joel"},{"family":"Sinatra","given":"Frank"},{"famil |
| CMOS18 test | OrchestraandChorusoftheRoyalOperaHouseCoventGarden1991 | song | [{"family":"Wixell","given":"Ingvar"},{"family":"Roni","given":"Luigi"},{"family |
| CMOS18 test | Rihanna2007 | song | [{"literal":"Jay-Z"}] |
| pruebas del estilo | Schmaus1961 | book | [{"family":"Drudis Baldrich","given":"Raimundo"},{"family":"Caballero Cuesta","g |

### `collection-editor` (12)

| Grupo | Clave | Tipo CSL | Valor |
|---|---|---|---|
| CMOS18 test | Allen2009 | book | [{"family":"Stimpson","given":"Catharine R."}] |
| CMOS18 test | Armstrong2014 | book | [{"family":"Carson","given":"Clayborne"}] |
| CMOS18 test | Blower2021 | book | [{"family":"Bradley","given":"Mark Philip"}] |
| CMOS18 test | Byrne1981 | book | [{"family":"Byrne","given":"Muriel St. Clare"}] |
| CMOS18 test | Cochrane1987 | book | [{"family":"Kirshner","given":"Julius"},{"family":"Boyer","given":"John W."}] |
| CMOS18 test | Donne1995 | book | [{"family":"Stringer","given":"Gary A."},{"family":"Johnson","given":"Jeffrey S. |
| CMOS18 test | Euripides2013 | book | [{"family":"Griffith","given":"Mark"},{"family":"Most","given":"Glenn W."}] |
| CMOS18 test | Woodward2007 | book | [{"family":"Harley","given":"J. B."},{"family":"Woodward","given":"David"}] |
| CMOS18 test | Ekbladh2021 | chapter | [{"family":"Bradley","given":"Mark Philip"}] |
| CMOS18 test | Migne1844 | chapter | [{"family":"Migne","given":"Jacques-Paul"}] |
| CMOS18 test | SamueldeChamplain2007 | map | [{"family":"Woodward","given":"David"}] |
| CMOS18 test | Adams1930a | personal_communication | [{"family":"Ford","given":"Worthington Chauncey"}] |

### `status` (11)

| Grupo | Clave | Tipo CSL | Valor |
|---|---|---|---|
| CMOS18 test | Smitha | article-journal | forthcoming |
| CMOS18 test | Author | book | forthcoming |
| CMOS18 test | Contributor | chapter | forthcoming |
| CMOS18 test | Faraday | chapter | forthcoming |
| CMOS18 test | 2025a | entry-dictionary | last modified |
| CMOS18 test | 2025 | entry-encyclopedia | last modified |
| CMOS18 test | Sanders2019 | interview | posted |
| CMOS18 test | 1616 | manuscript | after |
| CMOS18 test | Coolidge | speech | recorded |
| CMOS18 test | Oliver2022 | speech | posted |
| CMOS18 test | 2023a | webpage | archived |

### `section` (11)

| Grupo | Clave | Tipo CSL | Valor |
|---|---|---|---|
| CMOS18 test | 2000a | article-magazine | Kitchen notebook |
| CMOS18 test | Davis2015a | article-magazine | Interviews |
| CMOS18 test | Singer1973 | article-magazine | fiction |
| CMOS18 test | St.Felix2022 | article-magazine | on television |
| CMOS18 test | Wallraff2025 | article-magazine | Word fugitives |
| CMOS18 test | Belson2022 | article-newspaper | Sports |
| CMOS18 test | Bergner2022 | article-newspaper | Magazine |
| CMOS18 test | Chang2022 | article-newspaper | Modern love |
| CMOS18 test | Szalai2022 | article-newspaper | Books |
| CMOS18 test | Tommasini2021 | article-newspaper | Arts |
| CMOS18 test | Davis2015 | interview | Interviews |

### `volume-title` (11)

| Grupo | Clave | Tipo CSL | Valor |
|---|---|---|---|
| CMOS18 test | Friedkin2025 | article-journal | Location of power in exchange networks |
| CMOS18 test | Yeh2017 | article-journal | Qualia and ontology: language, semiotics, and materiality |
| CMOS18 test | Armstrong2014 | book | To Save the Soul of America, January 1961–August 1962 |
| CMOS18 test | Blower2021 | book | 1900–1945 |
| CMOS18 test | Donne1995 | book | The "Anniversaries" and the "Epicedes and obsequies" |
| CMOS18 test | FerrerBenimeli1976 | book | Las bases de un conflicto (1700–1739) |
| CMOS18 test | Lach1977a | book | A century of wonder |
| CMOS18 test | Woodward2007 | book | Cartography in the European Renaissance |
| CMOS18 test | Ekbladh2021 | chapter | 1900–1945 |
| CMOS18 test | SamueldeChamplain2007 | map | Cartography in the European Renaissance |
| CMOS18 test | Adams1930a | personal_communication | 1858–1891 |

### `event-date` (10)

| Grupo | Clave | Tipo CSL | Valor |
|---|---|---|---|
| CMOS18 test | Sanders2019 | interview | {"date-parts":[["2019",7,29]]} |
| CMOS18 test | Adams1930a | personal_communication | {"date-parts":[["1867",9,22]]} |
| CMOS18 test | White1975 | personal_communication | {"date-parts":[["1946",5,2]]} |
| CMOS18 test | AtlantaSymphonyOrchestraandChamberChorus1988 | song | {"date-parts":[["1987",12,19]]} |
| CMOS18 test | Holiday1997 | song | {"date-parts":[["1958",2,20]]} |
| CMOS18 test | OrchestraandChorusoftheRoyalOperaHouseCoventGarden1991 | song | {"date-parts":[["1973",5]]} |
| CMOS18 test | Weingartner1992 | song | {"date-parts":[["1936"]]} |
| CMOS18 test | Coolidge | speech | {"date-parts":[["1920",3,2]]} |
| CMOS18 test | Oliver2022 | speech | {"date-parts":[["2022",2,23]]} |
| CMOS18 test | Truman2025 | speech | {"date-parts":[["1945",4,16]]} |

### `translator` (10)

| Grupo | Clave | Tipo CSL | Valor |
|---|---|---|---|
| CMOS18 test | Singer1973 | article-magazine | [{"family":"Nevel","given":"Blanche"},{"family":"Nevel","given":"Joseph"}] |
| CMOS18 test | Adorno1999 | book | [{"family":"Walker","given":"Nicholas"}] |
| CMOS18 test | Bernhard1990 | book | [{"family":"Jansen","given":"Peter"},{"family":"Northcott","given":"Kenneth J."} |
| CMOS18 test | Derrida2016 | book | [{"family":"Bennington","given":"Geoffrey"}] |
| CMOS18 test | Euripides2013 | book | [{"family":"Arrowsmith","given":"William"}] |
| CMOS18 test | Ferreras2022 | book | [{"family":"Richmond Mouillot","given":"Miranda"}] |
| CMOS18 test | GarciaMarquez1988 | book | [{"family":"Grossman","given":"Edith"}] |
| CMOS18 test | Schweitzer1966 | book | [{"family":"Newman","given":"Ernest"}] |
| CMOS18 test | Augustine1931 | classic | [{"family":"Healey","given":"John"}] |
| CMOS18 test | Propertius1990 | classic | [{"family":"Goold","given":"G. P."}] |

### `volume` (8)

| Grupo | Clave | Tipo CSL | Valor |
|---|---|---|---|
| CMOS18 test | Ratliff1999 | article-magazine | 9 |
| CMOS18 test | Ratliff1999a | article-magazine | 9 |
| CMOS18 test | Ekbladh2021 | chapter | 3 |
| CMOS18 test | Migne1844 | chapter | 36 |
| CMOS18 test | SamueldeChamplain2007 | map | 3 |
| CMOS18 test | Chumley2017 | periodical | 5 |
| CMOS18 test | Adams1930a | personal_communication | 1 |
| pruebas del estilo | Lavenia2017 | article-journal | 4 |

### `medium` (8)

| Grupo | Clave | Tipo CSL | Valor |
|---|---|---|---|
| CMOS18 test | Laffin2022 | article-newspaper | video |
| CMOS18 test | Bashford2022 | book | EPUB |
| CMOS18 test | Jovin2022a | book | Kindle |
| CMOS18 test | Roy2008 | book | Kindle |
| CMOS18 test | Whitman1855 | book | printed by the author |
| CMOS18 test | Pulak2008 | chapter | exhibition catalog |
| CMOS18 test | HMTreasury1968 | document | Cmnd. 3787 |
| CMOS18 test | Tauber1958 | thesis | microfilm |

### `page` (7)

| Grupo | Clave | Tipo CSL | Valor |
|---|---|---|---|
| CMOS18 test | Baldwin2015 | book | 445–506 |
| CMOS18 test | Shakespeare2005a | book | 873–1058 |
| CMOS18 test | Davis2015 | interview | 172 |
| CMOS18 test | 1616 | manuscript | fol. 466r |
| CMOS18 test | SamueldeChamplain2007 | map | fig. 51.3 |
| CMOS18 test | Adams1930a | personal_communication | 133–134 |
| CMOS18 test | White1975 | personal_communication | 273 |

### `available-date` (6)

| Grupo | Clave | Tipo CSL | Valor |
|---|---|---|---|
| CMOS18 test | Chan2025 | article-journal | {"date-parts":[["2023",1,6]]} |
| CMOS18 test | Armstrong2014 | book | {"literal":"1992/.."} |
| CMOS18 test | Donne1995 | book | {"date-parts":[["1995"],["2022"]]} |
| CMOS18 test | Lach1977a | book | {"date-parts":[["1965"],["1993"]]} |
| CMOS18 test | Woodward2007 | book | {"literal":"1987/.."} |
| CMOS18 test | Adams1930a | personal_communication | {"date-parts":[["1930"],["1938"]]} |

### `archive` (5)

| Grupo | Clave | Tipo CSL | Valor |
|---|---|---|---|
| CMOS18 test | Pegoraro2007 | article-newspaper | LexisNexis Academic |
| CMOS18 test | Ferreras2022 | book | EBSCOhost |
| CMOS18 test | BlajerdelaGarza2019 | thesis | ProQuest |
| CMOS18 test | Stout2021 | thesis | ProQuest |
| CMOS18 test | Tauber1958 | thesis | ProQuest Dissertations & Theses |

### `number` (5)

| Grupo | Clave | Tipo CSL | Valor |
|---|---|---|---|
| CMOS18 test | Dror2022 | article-journal | e0263069 |
| CMOS18 test | Snyder2025 | article-journal | e0318239 |
| CMOS18 test | BlajerdelaGarza2019 | thesis | 13865986 |
| CMOS18 test | Stout2021 | thesis | 28490261 |
| CMOS18 test | Tauber1958 | thesis | 5802717 |

### `publisher-place` (5)

| Grupo | Clave | Tipo CSL | Valor |
|---|---|---|---|
| CMOS18 test | Garrett1975 | article-journal | West Virginia University |
| CMOS18 test | Hitchcock2000a | motion_picture | United States |
| pruebas del estilo | Brady1951 | article-journal | St. Bonaventure, N.Y |
| pruebas del estilo | Merino1985 | article-journal | Pamplona |
| pruebas del estilo | Congar1946 | entry-dictionary | París |

### `genre` (5)

| Grupo | Clave | Tipo CSL | Valor |
|---|---|---|---|
| CMOS18 test | Public2024 | article-newspaper | letter to the editor |
| CMOS18 test | Vallier2021 | chapter | online appendix |
| CMOS18 test | Wilkerson2022 | chapter | foreword |
| CMOS18 test | Wilson2019 | chapter | foreword |
| CMOS18 test | Empedocles | classic | frag. 115 Diels-Kranz |

### `original-date` (4)

| Grupo | Clave | Tipo CSL | Valor |
|---|---|---|---|
| CMOS18 test | SamueldeChamplain2007 | map | {"date-parts":[["1612"]]} |
| CMOS18 test | USGeologicalSurvey1951 | map | {"date-parts":[["1909"]]} |
| CMOS18 test | Cuaron2014 | motion_picture | {"date-parts":[["2013"]]} |
| CMOS18 test | Hitchcock2000a | motion_picture | {"date-parts":[["1959",11,20]]} |

### `chapter-number` (4)

| Grupo | Clave | Tipo CSL | Valor |
|---|---|---|---|
| CMOS18 test | Ekbladh2021 | chapter | 26 |
| CMOS18 test | Sanneh2021 | chapter | 5 |
| CMOS18 test | Holiday1997 | song | 1 |
| CMOS18 test | Rihanna2007 | song | 1 |

### `reviewed-author` (4)

| Grupo | Clave | Tipo CSL | Valor |
|---|---|---|---|
| CMOS18 test | Ratliff1999 | article-magazine | [{"family":"Vianna","given":"Hermano"}] |
| CMOS18 test | Ratliff1999a | article-magazine | [{"family":"Vianna","given":"Hermano"}] |
| CMOS18 test | Szalai2022 | article-newspaper | [{"family":"Aviv","given":"Rachel"}] |
| CMOS18 test | Tommasini2021 | article-newspaper | [{"literal":"Zhu Wang (piano)"}] |

### `edition` (3)

| Grupo | Clave | Tipo CSL | Valor |
|---|---|---|---|
| CMOS18 test | Apple1974 | article-newspaper | late city |
| CMOS18 test | Wilkerson2022 | chapter | 2 |
| CMOS18 test | 2022 | legislation | West |

### `references` (3)

| Grupo | Clave | Tipo CSL | Valor |
|---|---|---|---|
| CMOS18 test | Adams2008 | book | Distributed by the University of Virginia Press |
| CMOS18 test | Cacchione2017 | book | Distributed by Yale University Press. Published in conjunction with an exhibitio |
| CMOS18 test | Weingartner1992 | song | Includes Beethoven’s Symphony No. 3 in E-flat Major and Symphony No. 8 in F Majo |

### `composer` (3)

| Grupo | Clave | Tipo CSL | Valor |
|---|---|---|---|
| CMOS18 test | AtlantaSymphonyOrchestraandChamberChorus1988 | song | [{"family":"Handel","given":"George Frideric"}] |
| CMOS18 test | OrchestraandChorusoftheRoyalOperaHouseCoventGarden1991 | song | [{"family":"Mozart","given":"Wolfgang Amadeus"}] |
| CMOS18 test | Thomas1953 | song | [{"family":"Thomas","given":"Dylan"}] |

### `reviewed-title` (3)

| Grupo | Clave | Tipo CSL | Valor |
|---|---|---|---|
| CMOS18 test | Ratliff1999 | article-magazine | The Mystery of Samba: Popular Music and National Identity in Brazil |
| CMOS18 test | St.Felix2022 | article-magazine | Katrina Babies |
| CMOS18 test | Szalai2022 | article-newspaper | Strangers to Ourselves: Unsettled Minds and the Stories That Make Us |

### `compiler` (2)

| Grupo | Clave | Tipo CSL | Valor |
|---|---|---|---|
| CMOS18 test | 2003 | book | [{"family":"Austin","given":"Tim"}] |
| CMOS18 test | 2017 | book | [{"family":"Gray","given":"Rosemary"}] |

### `supplement-number` (2)

| Grupo | Clave | Tipo CSL | Valor |
|---|---|---|---|
| CMOS18 test | Yeh2017 | article-journal | S1 |
| CMOS18 test | Chumley2017 | periodical | S1 |

### `part-number` (2)

| Grupo | Clave | Tipo CSL | Valor |
|---|---|---|---|
| CMOS18 test | Lach1977a | book | bk. 3 |
| CMOS18 test | Woodward2007 | book | 1 |

### `event-place` (2)

| Grupo | Clave | Tipo CSL | Valor |
|---|---|---|---|
| CMOS18 test | Tommasini2021 | article-newspaper | New York |
| CMOS18 test | Sanders2019 | interview | TEN Nail Bar, Detroit, MI |

### `event-title` (2)

| Grupo | Clave | Tipo CSL | Valor |
|---|---|---|---|
| CMOS18 test | St.Felix2022 | article-magazine | HBO Max |
| CMOS18 test | Tommasini2021 | article-newspaper | Zankel Hall |

### `narrator` (1)

| Grupo | Clave | Tipo CSL | Valor |
|---|---|---|---|
| CMOS18 test | Cain2022 | book | [{"family":"Vance","given":"Simon"}] |

### `illustrator` (1)

| Grupo | Clave | Tipo CSL | Valor |
|---|---|---|---|
| CMOS18 test | Carson1962 | book | [{"family":"Darling","given":"Lois"},{"family":"Darling","given":"Louis"}] |

### `interviewer` (1)

| Grupo | Clave | Tipo CSL | Valor |
|---|---|---|---|
| CMOS18 test | Davis2015a | article-magazine | [{"family":"Aguilar","given":"Andrea"},{"family":"Fronth-Nygren","given":"Johann |

### `container-author` (1)

| Grupo | Clave | Tipo CSL | Valor |
|---|---|---|---|
| CMOS18 test | Eliot1968 | book | [{"family":"Pound","given":"Ezra"}] |

### `part-title` (1)

| Grupo | Clave | Tipo CSL | Valor |
|---|---|---|---|
| CMOS18 test | Lach1977a | book | The scholarly disciplines |

### `producer` (1)

| Grupo | Clave | Tipo CSL | Valor |
|---|---|---|---|
| CMOS18 test | Laffin2022 | article-newspaper | [{"family":"Cott","given":"Emma"},{"family":"Laffin","given":"Ben"}] |

### `chair` (1)

| Grupo | Clave | Tipo CSL | Valor |
|---|---|---|---|
| CMOS18 test | Oliver2022 | speech | [{"family":"McCall","given":"Andrew"}] |

### `reviewed-genre` (1)

| Grupo | Clave | Tipo CSL | Valor |
|---|---|---|---|
| CMOS18 test | Tommasini2021 | article-newspaper | recital |

### `scale` (1)

| Grupo | Clave | Tipo CSL | Valor |
|---|---|---|---|
| CMOS18 test | USGeologicalSurvey1951 | map | 1:125,000 scale |

