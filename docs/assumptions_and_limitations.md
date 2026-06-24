# Assumptions and Limitations

## 1. Purpose

This repository provides transparent, screening-level calculations for advanced oxidation processes in wastewater treatment.

The framework is intended to support:

* engineering interpretation,
* early process screening,
* teaching and training,
* comparison of wastewater matrices,
* preliminary kinetic reasoning,
* preparation for more detailed experimental or modeling work.

It is not intended to replace experimental validation, pilot-scale testing, or final engineering design.

## 2. Main assumptions

The current framework uses simplified kinetic relationships based on hydroxyl-radical competition.

The main assumptions are:

* hydroxyl radicals are represented using an apparent steady-state concentration,
* the wastewater matrix is represented through lumped scavenging capacity,
* degradation of target pollutants follows apparent first-order behavior,
* radical utilization efficiency is calculated from competition kinetics,
* reactor-scale effects are not yet explicitly resolved,
* oxidant radical yields are represented using simplified lumped parameters.

## 3. Scavenging-capacity assumption

The total radical scavenging capacity is calculated as:

```text
k_scav = sum(kOH_i * C_i)
```

This is useful for identifying which species dominate hydroxyl-radical consumption.

However, in real wastewater, the matrix is complex. Dissolved organic carbon, effluent organic matter, colloids, inorganic species, intermediate products, and site-specific contaminants may all contribute to radical loss.

Therefore, calculated values should be interpreted as engineering estimates, not exact universal constants.

## 4. DOC representation

Dissolved organic carbon is represented as a lumped pseudo-first-order scavenging term.

This is a simplification because DOC is not a single chemical species. It is a complex mixture with distributed molecular structures, functional groups, and reaction rates.

The current DOC term is useful for sensitivity analysis, but it should be calibrated with experimental data when possible.

## 5. Apparent first-order kinetics

The framework uses apparent first-order degradation behavior:

```text
C / C0 = exp(-k_app * t)
```

This is widely useful for interpreting AOP removal curves, but it may not describe all systems.

Deviations may occur due to:

* changing oxidant concentration,
* radical-chain effects,
* mass-transfer limitations,
* radiation attenuation,
* pH changes,
* scavenger depletion,
* intermediate formation,
* by-product reactions,
* non-ideal reactor hydraulics.

## 6. Ozone module limitation

The ozonation module uses a lumped hydroxyl-radical yield:

```text
OH_produced = Y_OH * O3_consumed
```

This is a simplified estimate.

It does not include:

* detailed ozone decomposition chain chemistry,
* pH-dependent ozone reactions,
* carbonate and bicarbonate radical chemistry,
* direct ozone reactions with pollutants,
* gas-liquid ozone transfer,
* ozone off-gas losses,
* bromate or other by-product formation.

## 7. H2O2 module limitation

The H2O2 module uses the ideal UV/H2O2 stoichiometric relationship:

```text
H2O2 + UV -> 2 OH
```

with an optional efficiency factor.

This does not explicitly model:

* UV fluence distribution,
* lamp spectrum,
* H2O2 absorption,
* water transmittance,
* reactor optical path length,
* radical recombination,
* H2O2 residuals,
* UV shielding by turbidity or color.

## 8. Energy indicators

The energy indicators are simplified.

They are intended for relative interpretation, such as comparing scenarios where treatment time is proportional to:

```text
1 / k_app
```

They do not yet represent full process energy balances.

A complete energy analysis would require:

* pump power,
* oxidant generation or delivery energy,
* UV lamp efficiency,
* ozone mass-transfer efficiency,
* hydraulic residence time,
* reactor geometry,
* mixing power,
* off-gas treatment,
* sludge or concentrate handling,
* plant-level integration.

## 9. Treatment-train screening

The treatment-train screening module provides heuristic guidance.

It should be interpreted as an early-stage decision-support tool, not a final design or regulatory tool.

Site-specific design should consider:

* influent and effluent characterization,
* micropollutant identity and concentration,
* target removal requirements,
* toxicity and transformation products,
* disinfection by-products,
* sludge and concentrate management,
* operational reliability,
* CAPEX and OPEX,
* local regulatory requirements.

## 10. Appropriate use

The current framework is appropriate for:

* comparing clean water and wastewater matrices,
* estimating scavenging dominance,
* evaluating DOC sensitivity,
* interpreting apparent kinetic constants,
* estimating treatment-time trends,
* demonstrating why pretreatment improves AOP efficiency,
* teaching matrix-aware AOP design principles.

## 11. Inappropriate use

The current framework should not be used alone for:

* full-scale plant design,
* regulatory compliance claims,
* safety-critical decisions,
* by-product risk assessment,
* final oxidant-dose selection,
* guaranteed micropollutant removal prediction,
* replacement of laboratory or pilot data.

## 12. Recommended engineering workflow

A practical workflow is:

```text
1. Characterize wastewater matrix.
2. Estimate scavenging capacity.
3. Identify dominant radical sinks.
4. Estimate radical utilization efficiency.
5. Estimate apparent k_app.
6. Estimate treatment time.
7. Compare pretreatment scenarios.
8. Validate with laboratory experiments.
9. Calibrate model parameters.
10. Proceed to pilot testing and engineering design.
```

## 13. Summary

The framework is a transparent engineering-science tool.

Its value lies in making assumptions explicit, connecting radical chemistry with process interpretation, and supporting disciplined early-stage evaluation of advanced oxidation processes in wastewater treatment.
