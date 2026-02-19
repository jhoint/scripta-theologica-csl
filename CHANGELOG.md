# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
