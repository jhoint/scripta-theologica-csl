# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.0] - 2026-11-03

Primera versión que reúne el estilo del repositorio con el del vault de trabajo (una tesis doctoral con Zotero, Obsidian y Pandoc). Los cambios de febrero y octubre de 2026 no se habían registrado antes; se incluyen aquí con su fecha.

### Added
- Obras clásicas y patrísticas (`type: classic`) con la sigla de la colección (`collection-title-short`); ver `OBRAS-CLASICAS.md` (2026-02-20).
- Partituras (`musical_score`) y canciones o grabaciones (`song`), según Chicago (2026-02-19).
- **Estilo completo:** rama propia para los 45 tipos de CSL 1.0.2 (los 44 del Chicago oficial, 18.ª ed., más `classic`), organizados en macros por familia. Para lo que las normas de la revista no regulan: elementos y orden de Chicago, forma de *Scripta* (versalitas, cursiva para las obras, «» para las partes) (2026-11-03).
  - Archivo e inéditos (cartas, manuscritos, documentos, entrevistas, discursos): autor siempre, título, fecha numérica (`23-3-1962`), colección, archivo y signatura, lugar. Formato provisional.
  - Web (páginas, entradas de blog, publicaciones en redes): título en cursiva, sitio, fecha y enlace.
  - Obras independientes (informes, datos, mapas, obras gráficas, folletos, normas, colecciones, software), audiovisuales, jurídicos, voces genéricas y reseñas.
- `pruebas-tipos.json` y `pruebas-tipos.md`: 51 casos con datos ficticios, uno por tipo más casos límite.

### Changed
- Revistas: solo el volumen, sin número de fascículo (salvo que no haya volumen) y sin coma antes de la página, como en «*Scripta Theologica* 17 (1985) 227-243» (2026-11-02).
- Edición: «2 ed. Aschaffenburg: …», como en el ejemplo de las normas; sustituye a «2.ª ed.» (2026-11-02).
- Enlace solo si no hay DOI; en las notas, después de la página (2026-11-02).
- Artículos de revistas no académicas y de periódicos: se muestra el título de la publicación, que antes se perdía (2026-11-02).
- Autor del libro (`container-author`) con nombre completo, como el autor (2026-11-03).
- Comillas de los títulos: las pone CSL (`quotes="true"`), con «» por fuera y “” por dentro, definidas en el locale del estilo. Antes se ponían con `prefix`/`suffix` y un título que ya llevaba comillas salía con «« »» (2026-11-03).
- Citas posteriores de artículos: título corto entre «», sin DOI (2026-10-22).
- Limpieza interna del estilo, sin cambios en el resultado (2026-11-03).

### Fixed
- Obras clásicas: el locator salía duplicado en la primera cita («I, 6: BAC 756, I, 6, p. 188») (2026-10-28).
- Partituras y grabaciones perdían la editorial o el sello (2026-11-03).
- Coma antes de «recuperado de» (2026-02-19).

### Documentation
- `readme.md` reescrito: uso con Zotero y Pandoc, tipos cubiertos, convenciones de datos, criterios del estilo y pruebas.
- `cambios-a-realizar.md` actualizado con lo resuelto y lo pendiente.
- `OBRAS-CLASICAS.md`: resultados esperados corregidos.
- Eliminada del readme la referencia a un documento de Word de prueba que no está en el repositorio.

## [0.1.0] - 2026-02-12

### Added
- Initial CSL style implementation for Scripta Theologica journal
- Spanish language localization with ecclesiastical terminology
- Support for main citation types:
  - Books (single and multiple authors)
  - Book chapters and conference papers
  - Journal articles
  - Dictionary and encyclopedia entries
  - Theses
- Custom `editorial-director` field support for collective works with directors instead of editors
- Footnote-based citation format
- Bibliography generation with hanging indent
- DOI support
- Short cite form for subsequent citations
- Bibliography sorting by author, date, and title

### Fixed
- Initial release, no breaking changes from previous versions

## Guidelines for Updating This Changelog

### When to Update
- **Bug Fixes**: Document any corrections to existing functionality
- **New Features**: Document new citation types or formatting options
- **Improvements**: Document enhancements to existing features
- **Breaking Changes**: Document any changes that affect how users need to format their bibliographies
- **Documentation**: Document significant documentation updates

### Section Types
- **Added**: New features or functionality
- **Changed**: Changes to existing functionality
- **Deprecated**: Features that will be removed in a future version
- **Removed**: Removed features
- **Fixed**: Bug fixes
- **Security**: Security-related fixes

### Version Format
This project uses **Semantic Versioning**:
- **MAJOR** version when you make incompatible API changes (e.g., changing how to format a citation type)
- **MINOR** version when you add functionality in a backwards compatible manner (e.g., adding support for a new document type)
- **PATCH** version when you make backwards compatible bug fixes (e.g., fixing spacing in citations)

Example: `1.2.3`
- `1` = MAJOR
- `2` = MINOR
- `3` = PATCH

### Release Process
1. Update the `[Unreleased]` section with all changes made
2. Create a new version section with the date (YYYY-MM-DD format)
3. Update the CSL file's `<updated>` tag with the release date
4. Create a GitHub release with the version number and changelog

### Example Entry
```markdown
## [0.2.0] - 2026-03-15

### Added
- Support for papal documents (Encyclicals, Apostolic Exhortations)
- English language localization

### Fixed
- Issue with multiple editors formatting in some cases
```
