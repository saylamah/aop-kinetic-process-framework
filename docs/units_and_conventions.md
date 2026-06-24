# Units and Conventions

## Purpose

This page defines the main units, symbols, and naming conventions used in the AOP Kinetic Process Framework.

Clear unit handling is essential because advanced oxidation process calculations combine chemical kinetics, wastewater characterization, reactor indicators, and engineering performance metrics.

## General convention

The framework uses SI-compatible units where practical.

Concentrations for kinetic calculations are generally expressed in:

```text
mol/L
```

Rate constants are generally expressed as:

```text
L/(mol s)
```

Pseudo-first-order rates are expressed as:

```text
s^-1
```

## Core kinetic quantities

| Symbol     | Meaning                                                   | Unit          |
| ---------- | --------------------------------------------------------- | ------------- |
| `C_i`      | concentration of species `i`                              | mol/L         |
| `kOH_i`    | second-order rate constant with hydroxyl radical          | L/(mol s)     |
| `k_scav,i` | pseudo-first-order scavenging contribution of species `i` | s^-1          |
| `k_scav`   | total matrix scavenging capacity                          | s^-1          |
| `R_gen`    | hydroxyl-radical generation rate                          | mol/(L s)     |
| `[OH]_app` | apparent steady-state hydroxyl-radical concentration      | mol/L         |
| `k_app`    | apparent first-order degradation constant                 | s^-1          |
| `eta`      | radical utilization efficiency                            | dimensionless |
| `t`        | treatment time                                            | s             |

## Scavenging calculation

For each species:

```text
k_scav,i = kOH_i * C_i
```

For the full matrix:

```text
k_scav = sum(kOH_i * C_i)
```

## Radical utilization efficiency

For target pollutant `j`:

```text
eta_j = (kOH_j * C_j) / k_scav
```

This is dimensionless.

When reported as a percentage:

```text
eta_percent = 100 * eta_j
```

## Apparent hydroxyl-radical concentration

The simplified steady-state estimate is:

```text
[OH]_app = R_gen / k_scav
```

where:

```text
R_gen: mol/(L s)
k_scav: s^-1
[OH]_app: mol/L
```

## Apparent first-order degradation constant

For target pollutant `j`:

```text
k_app,j = kOH,j * [OH]_app
```

where:

```text
kOH,j: L/(mol s)
[OH]_app: mol/L
k_app,j: s^-1
```

## First-order treatment time

For apparent first-order degradation:

```text
C / C0 = exp(-k_app * t)
```

Removal fraction:

```text
removal = 1 - exp(-k_app * t)
```

Required treatment time:

```text
t = -ln(1 - removal) / k_app
```

## Energy quantities

| Quantity           | Meaning                       | Unit   |
| ------------------ | ----------------------------- | ------ |
| `power_kW`         | process power input           | kW     |
| `treatment_time_h` | treatment time                | h      |
| `volume_m3`        | treated volume                | m3     |
| `E_v`              | volumetric energy consumption | kWh/m3 |
| `E_m`              | energy per mass removed       | kWh/kg |

Volumetric energy consumption:

```text
E_v = P * t / V
```

Energy per mass removed:

```text
E_m = P * t / [V * (C0 - C)]
```

## Reactor-scale quantities

| Quantity  | Meaning           | Unit          |
| --------- | ----------------- | ------------- |
| `Da`      | Damköhler number  | dimensionless |
| `Re`      | Reynolds number   | dimensionless |
| `Sh`      | Sherwood number   | dimensionless |
| `tau_opt` | optical thickness | dimensionless |
| `sigma`   | cavitation number | dimensionless |

## Recommended naming convention

Use clear variable names with units included where possible.

Recommended examples:

```python
concentration_mol_L
k_oh_L_mol_s
scavenging_capacity_s
radical_generation_rate_mol_L_s
k_app_s
treatment_time_s
power_kW
volume_m3
```

Avoid ambiguous names such as:

```python
C
k
rate
energy
time
```

unless they are used only in local equations with clear documentation.

## DOC convention

Dissolved organic carbon is represented as a lumped pseudo-first-order scavenging term in the current framework.

For DOC, the representative data file may use:

```text
concentration_mol_L = 1.0
k_oh_L_mol_s = effective pseudo-first-order DOC scavenging contribution
```

This is a modeling convention, not a true molecular second-order rate constant.

## Important caution

Always check units before interpreting results.

A common source of error is mixing:

```text
mg/L
microgram/L
mol/L
s^-1
min^-1
h^-1
```

The current framework expects kinetic calculations primarily in `mol/L` and `s^-1`.

Unit conversion should be performed before using the functions.
