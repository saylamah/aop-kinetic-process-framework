# Roadmap

This roadmap describes planned development directions for the AOP Kinetic Process Framework.

The current release, `v0.1.0`, provides a transparent screening-level Python framework for matrix-aware interpretation of advanced oxidation processes in wastewater treatment.

## v0.1.0 — Initial framework

Status: released

Main capabilities:

- hydroxyl-radical scavenging calculations,
- radical utilization efficiency,
- apparent first-order kinetic calculations,
- treatment-time estimation,
- simplified energy indicators,
- ozone radical-yield estimates,
- H2O2 radical-yield estimates,
- reactor-scale dimensionless indicators,
- treatment-train screening logic,
- plotting utilities,
- representative secondary-effluent matrix data,
- documentation and automated tests.

## v0.2.0 — Expanded AOP process modules

Planned additions:

- UV/H2O2 process-screening module,
- ozone/direct oxidation and radical oxidation separation,
- Fenton and photo-Fenton simplified calculations,
- hydrodynamic cavitation screening metrics,
- electrochemical oxidation screening indicators,
- oxidant-dose comparison examples,
- additional tests for new modules.

## v0.3.0 — Matrix and contaminant database expansion

Planned additions:

- expanded micropollutant dataset,
- representative matrices for municipal secondary effluent, industrial wastewater, and reuse water,
- additional inorganic scavengers,
- pH-dependent carbonate/bicarbonate interpretation,
- optional user-defined matrix input templates,
- uncertainty ranges for selected rate constants.

## v0.4.0 — Treatment-train decision support

Planned additions:

- improved AOP-readiness screening,
- pretreatment benefit estimator,
- activated carbon plus AOP comparison logic,
- membrane plus AOP screening logic,
- biological polishing plus AOP integration logic,
- engineering decision tables for treatment-train selection.

## v0.5.0 — Validation and benchmarking

Planned additions:

- literature-based benchmark cases,
- reproducibility notebooks,
- comparison of calculated and reported apparent rate constants,
- sensitivity analysis examples,
- uncertainty and parameter-range exploration.

## Long-term direction

Possible long-term development directions include:

- Jupyter notebooks for teaching and applied engineering use,
- interactive dashboards,
- integration with wastewater characterization datasets,
- support for pilot-scale data calibration,
- simplified cost and energy comparison modules,
- publication-ready figures,
- Zenodo archiving of stable releases.

## Development philosophy

The framework will remain:

- transparent,
- modular,
- scientifically conservative,
- engineering-oriented,
- easy to inspect,
- easy to extend.

The goal is to support disciplined early-stage interpretation of AOP performance, not to replace laboratory testing, pilot validation, or final engineering design.
