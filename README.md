# AOP Kinetic Process Framework

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20841383.svg)](https://doi.org/10.5281/zenodo.20841383)
[![Python tests](https://github.com/saylamah/aop-kinetic-process-framework/actions/workflows/python-tests.yml/badge.svg)](https://github.com/saylamah/aop-kinetic-process-framework/actions/workflows/python-tests.yml)

A Python framework for matrix-aware kinetic and process-level assessment of advanced oxidation processes in wastewater treatment.

---

## Purpose

Advanced oxidation processes are often compared using pollutant-removal percentages or apparent first-order rate constants.

These indicators can be misleading when wastewater-matrix constituents consume a substantial fraction of the generated reactive species.

This repository provides transparent calculation tools for examining how:

- hydroxyl-radical generation;
- dissolved organic matter;
- bicarbonate and carbonate;
- inorganic scavengers;
- pollutant concentration;
- radical competition;
- reactor conditions;
- oxidant utilization;
- treatment time;
- simplified energy indicators

interact to determine apparent AOP performance.

The objective is not to identify one universally superior AOP. It is to improve engineering interpretation, comparison, screening, and validation planning for specific water matrices and treatment objectives.

---

## Practical Engineering Questions

The framework is intended to support questions such as:

- Which matrix constituents dominate hydroxyl-radical consumption?
- What fraction of generated radicals is used toward the target pollutant?
- Why can two waters show different degradation rates under similar operating conditions?
- How does dissolved organic carbon affect apparent treatment performance?
- How do alkalinity and pH influence bicarbonate and carbonate scavenging?
- What treatment time follows from an assumed apparent first-order rate constant?
- Is poor performance associated primarily with radical generation or non-productive scavenging?
- Which measurements are required before comparing AOP alternatives?
- When might pretreatment or a treatment train be preferable to increasing oxidant or energy input?
- Which assumptions must be validated before pilot- or plant-scale use?

---

## Scientific Concept

The initial framework uses a simplified competition-kinetics and apparent steady-state representation.

The total hydroxyl-radical scavenging capacity is expressed as:

```text
k_scav = sum(kOH_i * C_i)
```

The apparent hydroxyl-radical concentration is approximated as:

```text
[OH]_app = R_gen / k_scav
```

The apparent first-order degradation constant for target pollutant `j` is:

```text
k_app,j = kOH,j * [OH]_app
```

The fraction of hydroxyl-radical consumption directed toward pollutant `j` is:

```text
eta_j = (kOH,j * C_j) / k_scav
```

where:

```text
k_scav   = total hydroxyl-radical scavenging capacity
kOH_i    = second-order rate constant for reaction of species i with OH
C_i      = concentration of species i
R_gen    = assumed hydroxyl-radical generation rate
[OH]_app = apparent steady-state hydroxyl-radical concentration
k_app,j  = apparent first-order degradation constant for pollutant j
eta_j    = radical-utilization fraction toward pollutant j
```

These relationships are intended for transparent screening and interpretation. They do not replace a complete radical-reaction mechanism, validated reactor model, or site-specific experimental programme.

---

## Current Capabilities

The current implementation includes:

- matrix scavenging-capacity calculations;
- scavenging contributions by individual matrix components;
- radical-utilization fractions;
- apparent first-order kinetic calculations;
- treatment-time calculations;
- simplified energy-related indicators;
- ozone radical-yield calculations;
- hydrogen-peroxide radical-yield calculations;
- reactor-scale dimensionless indicators;
- treatment-train screening logic;
- unit conversions for:
  - mg/L;
  - µg/L;
  - mol/L;
  - dissolved organic carbon;
  - alkalinity;
- carbonate-system calculations for bicarbonate and carbonate estimation from pH and alkalinity;
- sensitivity-analysis examples;
- plotting utilities;
- representative wastewater-matrix data;
- executable example scripts;
- automated Python tests using GitHub Actions.

---

## Application Scope

The framework is intended primarily for:

- secondary-effluent and wastewater-matrix screening;
- micropollutant-degradation interpretation;
- hydroxyl-radical competition analysis;
- oxidant-utilization assessment;
- comparison of matrix scenarios;
- treatment-time estimation;
- simplified AOP energy interpretation;
- treatment-train screening;
- educational and research applications;
- preparation of experimental and pilot-validation programmes.

Potential AOP applications may include:

- UV/H₂O₂;
- ozonation and ozone-based AOPs;
- Fenton and Fenton-like processes;
- electrochemical oxidation;
- photocatalytic processes;
- cavitation-assisted oxidation;
- combined and sequential treatment processes.

Not every process listed above is represented by a complete process-specific model in the current version.

---

## Engineering Interpretation

Wastewater-matrix effects can substantially influence apparent AOP performance.

A pollutant may react rapidly with hydroxyl radicals while still receiving only a small fraction of the radicals generated in the reactor. Dissolved organic matter, bicarbonate, carbonate, nitrite, and other constituents may dominate radical consumption.

Accordingly, increasing oxidant concentration, irradiation, power input, or nominal radical generation does not automatically improve useful contaminant degradation proportionally.

A technically meaningful assessment should distinguish between:

- radical generation;
- radical availability;
- target-pollutant competition;
- background scavenging;
- mass-transfer and reactor effects;
- oxidant decomposition;
- transformation-product formation;
- mineralization;
- downstream treatment requirements;
- energy and chemical consumption.

The framework currently addresses selected parts of this broader assessment.

---

## Quick Example

The first example evaluates hydroxyl-radical scavenging contributions in a representative secondary-effluent matrix.

```bash
python examples/01_matrix_scavenging_secondary_effluent.py
```

The output includes:

- total scavenging capacity;
- pseudo-first-order contribution of each component;
- radical-consumption fraction;
- percentage contribution of each matrix constituent.

Additional examples are available in the `examples/` directory.

---

## Documentation

- [Quickstart](docs/quickstart.md)
- [Theory Background](docs/theory.md)
- [Examples](docs/examples.md)
- [API Reference](docs/api_reference.md)
- [Scientific Background](docs/scientific_background.md)
- [Assumptions and Limitations](docs/assumptions_and_limitations.md)
- [Units and Conventions](docs/units_and_conventions.md)
- [Roadmap](ROADMAP.md)
- [Changelog](CHANGELOG.md)

---

## Repository Structure

```text
aop-kinetic-process-framework/
│
├── README.md
├── CITATION.cff
├── pyproject.toml
├── ROADMAP.md
├── CHANGELOG.md
│
├── .github/
│   └── workflows/
│       └── python-tests.yml
│
├── data/
│   └── representative_effluent_matrix.csv
│
├── docs/
│   ├── quickstart.md
│   ├── theory.md
│   ├── examples.md
│   ├── api_reference.md
│   ├── scientific_background.md
│   ├── assumptions_and_limitations.md
│   └── units_and_conventions.md
│
├── examples/
│   ├── 01_matrix_scavenging_secondary_effluent.py
│   ├── 02_kapp_and_treatment_time.py
│   ├── 03_doc_sensitivity.py
│   ├── 04_oxidant_radical_yields.py
│   ├── 05_plot_scavenging_contributions.py
│   ├── 06_treatment_train_screening.py
│   ├── 07_reactor_scale_indicators.py
│   ├── 08_unit_conversions_for_matrix_setup.py
│   ├── 09_carbonate_system_scavenging.py
│   └── 10_pH_effect_on_carbonate_scavenging.py
│
├── src/
│   └── aop_framework/
│       ├── __init__.py
│       ├── carbonate.py
│       ├── conversions.py
│       ├── scavenging.py
│       ├── kinetics.py
│       ├── energy.py
│       ├── ozonation.py
│       ├── h2o2.py
│       ├── reactor.py
│       ├── treatment_train.py
│       └── plotting.py
│
└── tests/
    ├── test_carbonate.py
    ├── test_conversions.py
    ├── test_scavenging.py
    ├── test_kinetics.py
    ├── test_energy.py
    ├── test_ozonation.py
    ├── test_h2o2.py
    ├── test_reactor.py
    ├── test_imports.py
    └── test_treatment_train.py
```

---

## Evidence and Maturity

**Current status:** Tested research and engineering screening framework.

The repository currently provides:

- transparent equations and assumptions;
- modular Python calculations;
- representative demonstration data;
- reproducible examples;
- automated software tests;
- engineering interpretation guidance.

Automated tests verify expected software behavior for the implemented cases. They do not by themselves establish predictive validity for real wastewater systems.

The repository does not currently provide:

- a complete elementary radical-reaction mechanism;
- a universally validated hydroxyl-radical generation model;
- detailed reactor hydrodynamics;
- full radiation-field modelling;
- transformation-product prediction;
- toxicity assessment;
- complete mineralization prediction;
- equipment sizing;
- plant-level cost estimation;
- guaranteed full-scale treatment performance.

---

## Responsible Use and Limitations

Results should be treated as screening- or interpretation-level outputs unless validated for the specific:

- water matrix;
- pollutant mixture;
- temperature;
- pH;
- alkalinity;
- dissolved organic matter;
- oxidant;
- irradiation source;
- catalyst;
- reactor configuration;
- hydraulic conditions;
- residence time;
- analytical method;
- treatment objective.

Real-system application requires appropriate experimental measurements, mass balances, kinetic validation, reactor characterization, energy assessment, transformation-product analysis, toxicity evaluation, materials review, process-safety assessment, and scale-up verification.

This repository does not constitute a final treatment-process design, regulatory recommendation, environmental-compliance assessment, or guarantee of contaminant removal.

---

## Development Priorities

Further development may include:

- validation against published experimental datasets;
- uncertainty and parameter-sensitivity analysis;
- explicit comparison of selected AOP configurations;
- expanded radical and scavenger chemistry;
- treatment-train optimization logic;
- improved energy-normalized performance indicators;
- transformation-product considerations;
- additional reactor and transport descriptors;
- structured reporting of applicability limits.

The roadmap should be interpreted as a development direction rather than a commitment that every listed feature will be implemented.

---

## DOI and Citation

Repository DOI:

[10.5281/zenodo.20841383](https://doi.org/10.5281/zenodo.20841383)

Users should cite the repository version and any associated scientific documentation relevant to the calculations applied.

---

## License

The software is released under the MIT License.

Scientific documentation, conceptual descriptions, and example data should be cited appropriately when reused.

---

## Author

**Ahmad Saylam**

R&D & Technology Development Leader  
Scientific & Engineering Consultant
