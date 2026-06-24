# Changelog

All notable changes to this project will be documented in this file.

The format follows a simple version-based structure.

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
