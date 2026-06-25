# Changelog

All notable changes to this project will be documented in this file.

The format follows a simple version-based structure.

## [Unreleased]

No unreleased changes yet.

## [0.1.3] - 2026-06-25

### Added

- Improved Python package metadata in `pyproject.toml`.
- Added project URLs for homepage, documentation, repository, issues, and changelog.
- Added package classifiers for scientific, engineering, educational, and Python-version metadata.
- Added carbonate-system units and conventions to `docs/units_and_conventions.md`.
- Added Example 10 for evaluating pH effects on carbonate-system radical scavenging.
- Added documentation updates for the pH-sensitivity example in README, quickstart, and examples documentation.

### Notes

This patch release improves package discoverability, documentation clarity, unit consistency, and pH-sensitive carbonate-system scavenging interpretation.

## [0.1.2] - Carbonate-system scavenging update

### Added

- Carbonate-system utility module for estimating bicarbonate and carbonate concentrations from alkalinity and pH.
- `CarbonateSystemResult` dataclass.
- Carbonate-to-bicarbonate ratio calculation.
- Simplified bicarbonate/carbonate speciation from alkalinity and pH.
- Tests for carbonate-system utilities.
- Example 09 for carbonate-system scavenging estimation.
- API reference documentation for carbonate-system utilities.
- README, quickstart, and examples documentation updates for the carbonate-system module.

### Notes

These additions improve matrix-aware scavenging analysis by allowing bicarbonate and carbonate concentrations to be estimated from common wastewater parameters such as alkalinity and pH.

The carbonate-system calculation is screening-level and does not replace a full aqueous-equilibrium model.

## [0.1.1] - Usability, governance, and unit-conversion update

### Added

* Contribution guidelines through `CONTRIBUTING.md`.
* Code of conduct through `CODE_OF_CONDUCT.md`.
* GitHub issue templates for:

  * bug reports,
  * feature requests,
  * scientific and data review.
* Pull request template.
* Units and conventions documentation.
* Unit-conversion utilities for:

  * `mg/L` to `mol/L`,
  * `µg/L` to `mol/L`,
  * `mol/L` to `mg/L`,
  * `mol/L` to `µg/L`,
  * `mg C/L` to `mol C/L`,
  * alkalinity as `mg/L CaCO3` to `eq/L`.
* Tests for unit-conversion utilities.
* Example 08 for unit conversions during wastewater matrix setup.
* Documentation updates for examples, quickstart, README, and API reference.

### Notes

These additions improve usability, repository governance, documentation clarity, and practical wastewater data preparation.

## [0.1.0] - Initial framework version

### Added

* Python package structure under `src/aop_framework`.
* Hydroxyl-radical scavenging calculations.
* Radical utilization efficiency calculation.
* Apparent steady-state hydroxyl-radical concentration calculation.
* Apparent first-order degradation constant calculation.
* First-order removal and treatment-time calculations.
* Simplified energy indicators.
* Ozone radical-yield calculations.
* H2O2 radical-yield calculations.
* Reactor-scale dimensionless indicators:

  * Damköhler number,
  * Reynolds number,
  * Sherwood number,
  * optical thickness,
  * cavitation number.
* Treatment-train screening logic for AOP readiness.
* Plotting utilities for scavenging contributions and DOC sensitivity.
* Representative secondary-effluent matrix data.
* Example scripts for:

  * matrix scavenging,
  * `k_app` and treatment time,
  * DOC sensitivity,
  * oxidant radical-yield comparison,
  * scavenging contribution plotting,
  * treatment-train screening,
  * reactor-scale indicators.
* Documentation pages:

  * theory background,
  * example descriptions,
  * assumptions and limitations,
  * API reference,
  * scientific background.
* Citation metadata through `CITATION.cff`.
* Automated testing using GitHub Actions.
* Unit tests for core modules.

### Notes

Version 0.1.0 is intended for transparent screening-level engineering calculations, teaching, and research support.

It is not a validated full-scale wastewater-treatment plant design tool.
