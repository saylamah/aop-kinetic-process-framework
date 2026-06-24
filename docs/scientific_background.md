# Scientific Background

## Purpose

This repository translates a unified kinetic-process interpretation of advanced oxidation processes into reusable Python tools.

The framework is intended to connect:

* radical chemistry,
* wastewater matrix composition,
* radical scavenging,
* apparent first-order degradation kinetics,
* oxidant utilization,
* reactor-scale indicators,
* treatment-train interpretation,
* energy-related process performance.

## Conceptual basis

Advanced oxidation processes are often studied under ideal or simplified laboratory conditions. However, practical wastewater treatment is governed by the interaction between reaction kinetics and process conditions.

The apparent first-order rate constant, `k_app`, is interpreted here as a system-level quantity. It is not only a property of the target pollutant. It emerges from the combined effects of:

* hydroxyl-radical generation,
* radical scavenging by dissolved organic carbon and inorganic species,
* intrinsic pollutant reactivity,
* target-pollutant concentration,
* reactor hydrodynamics,
* mass transfer,
* radiation attenuation,
* operating conditions.

## Competition kinetics

For a wastewater matrix containing multiple radical scavengers, the total hydroxyl-radical scavenging capacity is:

```text
k_scav = sum(kOH_i * C_i)
```

The apparent steady-state hydroxyl-radical concentration is estimated as:

```text
[OH]_app = R_gen / k_scav
```

For a target pollutant `j`, the apparent first-order degradation rate constant is:

```text
k_app,j = kOH,j * [OH]_app
```

The radical utilization efficiency toward the target pollutant is:

```text
eta_j = (kOH,j * C_j) / k_scav
```

This formulation explains why high intrinsic second-order reactivity does not guarantee high removal performance in real wastewater.

## Wastewater matrix effect

In realistic wastewater systems, trace micropollutants are usually present at very low concentrations, while dissolved organic carbon, bicarbonate, carbonate, nitrite, and other background constituents are present at much higher concentrations.

As a result, most generated hydroxyl radicals may be consumed by background matrix constituents rather than by the target micropollutants.

This is why AOP performance is often matrix-controlled.

## Engineering implication

Efficient AOP design should not focus only on increasing oxidant dose or energy input.

A more useful engineering objective is to improve the fraction of generated radicals that react with target contaminants.

This can be achieved by:

* applying AOPs after biological treatment,
* removing suspended solids before oxidation,
* reducing DOC before AOP treatment,
* controlling nitrite and alkalinity where possible,
* improving reactor hydrodynamics,
* reducing optical attenuation in UV-based systems,
* combining AOPs with adsorption, membranes, or biological polishing.

## Repository interpretation

This software repository converts the framework into a practical calculation structure.

The current version provides tools for:

* estimating matrix scavenging capacity,
* calculating radical utilization efficiency,
* estimating apparent hydroxyl-radical concentration,
* calculating `k_app`,
* estimating treatment time,
* comparing simplified ozone and H2O2 radical yields,
* calculating reactor-scale dimensionless indicators,
* screening AOP readiness in treatment trains.

## Related scientific work

This repository is associated with the following scientific works by Ahmad Saylam:

1. **A Unified Kinetic–Process Framework for Advanced Oxidation Processes: From Radical Chemistry to Reactor-Scale Performance in Wastewater Treatment**
   Zenodo, 2026.
   DOI: `10.5281/zenodo.19732394`

2. **Advances in Wastewater Treatment: Energy Efficiency, Micropollutants, and Circular Resource Recovery**
   Zenodo, 2026.
   DOI: `10.5281/zenodo.19438613`

## Recommended citation

If you use this repository, please cite the repository and the related scientific work.

The preferred citation is provided in:

```text
CITATION.cff
```

## Development philosophy

The framework is designed to be:

* transparent,
* modular,
* scientifically conservative,
* engineering-oriented,
* easy to extend,
* suitable for teaching and research screening.

The objective is not to replace experimental work, but to make the kinetic-process reasoning explicit, reproducible, and practically useful.
