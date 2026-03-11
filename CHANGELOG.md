# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- `scripta-definition.md` expanded with an explicit mapping from Scripta citation templates to target macro groups in `chicago2scripta.csl`.
- Defined "Micro-bloque 1" scope for presentation-only changes (terms, quotes, small caps, visual punctuation) to reduce regression risk.

### Changed
- Migration workflow now documents a concrete execution order for macro intervention before changing citation logic.
- `chicago2scripta.csl`: visual updates applied in micro-block 1 without changing citation flow logic.
- `chicago2scripta.csl`: micro-block 2 applied with Spanish localization terms and default locale set to `es-ES`.
- `chicago2scripta.csl`: micro-block 3 applied to normalize contributor name rendering as `APELLIDO` (small caps), `Nombre` in full-name outputs.
- Session diagnostic pass completed with 5 real `book` cases (`sale-deberiasalir.md`) to contrast current output vs expected Scripta output.
- Decided migration strategy for next iterations: apply global safe changes first, then macro-family adjustments by document groups (book-like, journal-like, reference-like).

### Pending (diagnosticado, pendiente de aplicar)
- **Rango de páginas**: `page-range-format="chicago"` comprime rangos (ej. `128-35`). Cambiar a `page-range-format="expanded"` para emitir rangos completos (`128-135`). Macro: atributo global en `<style>`. Riesgo mínimo.
- **Datos editoriales en notas**: en `source-book-note` y variantes, el bloque editorial sale entre paréntesis `(Editorial, año)` y sin lugar. Debe salir `Lugar: Editorial, año` sin paréntesis. Macro: `source-book-note` (y variantes para capítulo). Riesgo medio.
- **`text-case="title"` en títulos**: `title-primary` aplica capitalización estilo título en inglés (`Parochial and Plain Sermons`). Debe respetar el valor literal de Zotero. Eliminar o eliminar `text-case="title"` en esa macro. Riesgo bajo.
- **Rol `contributor` visible**: el campo `contributor` (no estándar CSL) aparece en notas como `with DRUDIS BALDRICH, Raimundo y otros`. Scripta no lo quiere. Suprimir en macros de nota. Riesgo bajo.
- **`collection-title`/`collection-number` visible en notas**: sale `Manuales de la Biblioteca del Pensamiento Actual 4`. Scripta no lo quiere en notas. Suprimir. Riesgo bajo.
- **Validaciones cruzadas pendientes (no-book)**: antes de aplicar cambios de alto impacto en macros compartidas, contrastar `article-journal`, `chapter`, `entry-dictionary` y `entry-encyclopedia` con ejemplos reales para evitar regresiones.

### Fixed
- Author display now renders surname in small caps in `author-note` and `author-bib`.
- Analytic/part titles now use angular quotes (`« »`) in `title-part`, `title-primary`, and `title-primary-short`.
- Journal serial identifier separator adjusted from `:` to space before locator in `source-serial-identifier-bib` and `source-serial-identifier-note` to align with target visual pattern.
- URL output in `source-DOI-URL` now displays as `recuperado de URL` when DOI is absent.
- Spanish term mapping added for roles and locators (`ed.`, `eds.`, `trad.`, `dir.`, `dirs.`, `p.`, `pp.`, `s. f.`, `recuperado`).
- Full-name contributor slots now use surname-first ordering with small-caps family names across author/editor/translator/container-contributor paths.
- `label-locator` page-label experiment was reverted on request to preserve current locator behavior until full locator policy is closed.

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
