# Examples

This page explains the example scripts included in the repository.

The examples are designed to be simple, transparent, and useful for engineering interpretation of advanced oxidation processes in wastewater treatment.

## Example 01 — Matrix scavenging in secondary effluent

File:

```text
examples/01_matrix_scavenging_secondary_effluent.py
```

Purpose:

This example calculates hydroxyl-radical scavenging contributions for a representative secondary-effluent matrix.

It reports:

* total hydroxyl-radical scavenging capacity,
* pseudo-first-order scavenging contribution of each matrix component,
* radical consumption fraction,
* percentage contribution of each component.

Engineering use:

This example helps identify which species dominate hydroxyl-radical consumption. In many realistic wastewater matrices, dissolved organic carbon and inorganic scavengers dominate radical consumption, while trace micropollutants receive only a small fraction of generated radicals.

## Example 02 — Apparent rate constant and treatment time

File:

```text
examples/02_kapp_and_treatment_time.py
```

Purpose:

This example connects matrix scavenging with apparent kinetic performance.

It calculates:

* total scavenging capacity,
* apparent steady-state hydroxyl-radical concentration,
* apparent first-order degradation constant `k_app`,
* treatment time required for 90% removal of a target pollutant.

Engineering use:

This example shows how higher matrix scavenging lowers apparent hydroxyl-radical concentration, reduces `k_app`, and increases treatment time.

## Example 03 — DOC sensitivity

File:

```text
examples/03_doc_sensitivity.py
```

Purpose:

This example evaluates how dissolved organic carbon, represented as a lumped pseudo-first-order scavenging contribution, affects radical utilization efficiency toward a target pollutant.

It reports:

* DOC concentration,
* DOC scavenging contribution,
* total matrix scavenging capacity,
* radical utilization efficiency toward the target pollutant,
* relative treatment-time indicator.

Engineering use:

This example helps evaluate the benefit of upstream DOC reduction before AOP treatment.

## Example 04 — Oxidant radical-yield comparison

File:

```text
examples/04_oxidant_radical_yields.py
```

Purpose:

This example compares simplified hydroxyl-radical production estimates from:

* ozone consumption,
* ideal UV/H2O2 photolysis,
* practical UV/H2O2 with an efficiency factor.

Engineering use:

This example shows why oxidant dose alone is not enough for comparing AOP systems. Useful radical production depends on oxidant activation, radical yield, process efficiency, and matrix scavenging.

## Example 05 — Plot scavenging contributions

File:

```text
examples/05_plot_scavenging_contributions.py
```

Purpose:

This example generates a horizontal bar chart showing hydroxyl-radical scavenging contributions.

Output:

```text
outputs/scavenging_contributions.png
```

Engineering use:

This example helps visualize which wastewater components dominate radical consumption.

## Example 06 — Treatment-train screening

File:

```text
examples/06_treatment_train_screening.py
```

Purpose:

This example uses the representative wastewater matrix to provide screening-level guidance for AOP readiness.

It reports:

* total scavenging capacity,
* AOP-readiness classification,
* main limitation,
* practical recommendation,
* supporting notes.

Engineering use:

This example helps decide whether AOP treatment is likely favorable, challenging, or inefficient without additional pretreatment or process integration.

## Recommended learning order

For a new user, the recommended order is:

```text
1. 01_matrix_scavenging_secondary_effluent.py
2. 02_kapp_and_treatment_time.py
3. 03_doc_sensitivity.py
4. 04_oxidant_radical_yields.py
5. 05_plot_scavenging_contributions.py
6. 06_treatment_train_screening.py
```

This order moves from radical competition chemistry to apparent kinetics, energy-related implications, oxidant comparison, visualization, and treatment-train interpretation.

## Notes

The examples are screening-level engineering tools.

They should not be interpreted as final plant-design calculations. Experimental validation, pilot testing, detailed reactor modeling, by-product assessment, and site-specific wastewater characterization remain necessary for practical implementation.
