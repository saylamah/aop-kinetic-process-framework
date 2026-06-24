# AOP Kinetic Process Framework

Python framework for matrix-aware kinetic and process-level evaluation of advanced oxidation processes in wastewater treatment.

## Purpose

This repository provides transparent engineering calculations for advanced oxidation processes (AOPs), especially where radical chemistry, wastewater matrix effects, and apparent process performance need to be interpreted together.

The framework focuses on:

* hydroxyl-radical scavenging capacity,
* radical utilization efficiency,
* apparent first-order degradation kinetics,
* treatment-time estimation,
* simplified energy-related indicators,
* matrix-aware interpretation of AOP performance.

## Scientific concept

Advanced oxidation processes are often evaluated using apparent first-order degradation constants. In realistic wastewater matrices, these apparent constants are not controlled by intrinsic pollutant reactivity alone.

They emerge from the combined effects of:

* radical generation,
* radical scavenging by dissolved organic carbon and inorganic species,
* target-pollutant concentration,
* reactor and transport limitations,
* operating conditions.

The starting framework follows the competition-kinetics interpretation:

```text
k_scav = sum(kOH_i * C_i)

[OH]_app = R_gen / k_scav

k_app,j = kOH,j * [OH]_app

eta_j = (kOH,j * C_j) / k_scav
```

where:

```text
k_scav   = total hydroxyl-radical scavenging capacity
R_gen    = hydroxyl-radical generation rate
[OH]_app = apparent steady-state hydroxyl-radical concentration
k_app,j  = apparent first-order degradation constant for pollutant j
eta_j    = radical utilization efficiency toward pollutant j
```

## Initial scope

Version 0.1 focuses on screening-level calculations for representative secondary-effluent matrices.

The current implementation includes:

* matrix scavenging calculations,
* radical utilization fractions,
* apparent first-order kinetic calculations,
* treatment-time calculations,
* simplified energy indicators,
* ozone radical-yield calculations,
* H2O2 radical-yield calculations,
* reactor-scale dimensionless indicators,
* treatment-train screening logic,
* plotting utilities,
* representative wastewater matrix data,
* working example scripts,
* automated tests using GitHub Actions.

## Repository structure

```text
```text
aop-kinetic-process-framework/
│
├── README.md
├── CITATION.cff
├── pyproject.toml
│
├── .github/
│   └── workflows/
│       └── python-tests.yml
│
├── data/
│   └── representative_effluent_matrix.csv
│
├── docs/
│   ├── theory.md
│   ├── examples.md
│   └── assumptions_and_limitations.md
│
├── examples/
│   ├── 01_matrix_scavenging_secondary_effluent.py
│   ├── 02_kapp_and_treatment_time.py
│   ├── 03_doc_sensitivity.py
│   ├── 04_oxidant_radical_yields.py
│   ├── 05_plot_scavenging_contributions.py
│   ├── 06_treatment_train_screening.py
│   └── 07_reactor_scale_indicators.py
│
├── src/
│   └── aop_framework/
│       ├── __init__.py
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
    ├── test_scavenging.py
    ├── test_kinetics.py
    ├── test_energy.py
    ├── test_ozonation.py
    ├── test_h2o2.py
    ├── test_reactor.py
    └── test_treatment_train.py
```

## Example

The first example calculates hydroxyl-radical scavenging contributions in a representative secondary-effluent matrix.

```bash
python examples/01_matrix_scavenging_secondary_effluent.py
```

The output reports:

* total scavenging capacity,
* pseudo-first-order scavenging contribution of each component,
* radical consumption fraction,
* percentage contribution of each matrix component.

## Engineering interpretation

The framework is based on the idea that AOP performance in real wastewater is usually matrix-controlled.

Even highly reactive micropollutants may receive only a small fraction of generated hydroxyl radicals when dissolved organic carbon, bicarbonate, carbonate, nitrite, and other background constituents dominate radical consumption.

Therefore, efficient AOP design should not maximize radical generation alone. It should improve useful radical utilization toward target contaminants while minimizing non-productive scavenging.

## Status

Early development.

The current version is intended for:

* research screening,
* engineering interpretation,
* education,
* reproducible examples,
* preparation for future model extensions.

It is not yet a validated full-scale plant-design simulator.

## Planned extensions

Planned additions include:

* DOC sensitivity example,
* k_app and treatment-time example,
* ozone radical-yield calculation,
* plotting functions,
* treatment-train screening logic,
* comparison of UV/H2O2, ozonation, Fenton, hydrodynamic cavitation, and electrochemical AOPs,
* documentation of assumptions and limitations,
* validation examples from literature and experimental data.

## License

Code is released under the MIT License.

Scientific documentation, conceptual descriptions, and example data should be cited appropriately when reused.

## Author

Ahmad Saylam
R&D and Technology Development
Applied physical-chemical sciences, thermochemical processes, and sustainable industrial innovation
