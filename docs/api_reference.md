# API Reference

This page summarizes the main modules and functions in the AOP Kinetic Process Framework.

## Package import

The main package can be imported as:

```python
import aop_framework
```

Common functions can also be imported directly:

```python
from aop_framework import Species, total_scavenging_capacity
```

## `scavenging.py`

This module contains functions for hydroxyl-radical scavenging calculations.

### `Species`

Represents a chemical species or lumped wastewater-matrix component.

Main parameters:

```text
name
concentration_mol_L
k_oh_L_mol_s
group
```

### `total_scavenging_capacity(species)`

Calculates total hydroxyl-radical scavenging capacity:

```text
k_scav = sum(kOH_i * C_i)
```

### `radical_utilization_efficiency(target, species)`

Calculates the fraction of hydroxyl radicals reacting with a target component:

```text
eta_j = (kOH_j * C_j) / k_scav
```

### `scavenging_table(species)`

Returns a table containing scavenging rates, fractions, and percentage contributions.

## `kinetics.py`

This module contains apparent kinetic performance calculations.

### `hydroxyl_radical_steady_state(radical_generation_rate_mol_L_s, scavenging_capacity_s)`

Calculates apparent steady-state hydroxyl-radical concentration:

```text
[OH]_app = R_gen / k_scav
```

### `apparent_first_order_rate_constant(k_oh_target_L_mol_s, oh_concentration_mol_L)`

Calculates apparent first-order degradation rate constant:

```text
k_app = kOH,target * [OH]_app
```

### `first_order_remaining_fraction(k_app_s, treatment_time_s)`

Calculates remaining concentration fraction:

```text
C / C0 = exp(-k_app * t)
```

### `first_order_removal_fraction(k_app_s, treatment_time_s)`

Calculates removal fraction:

```text
removal = 1 - exp(-k_app * t)
```

### `treatment_time_required(k_app_s, removal_fraction)`

Calculates treatment time required for a target removal fraction:

```text
t = -ln(1 - removal) / k_app
```

## `energy.py`

This module contains simplified energy indicators.

### `volumetric_energy_consumption(power_kW, treatment_time_h, volume_m3)`

Calculates volumetric energy consumption:

```text
E_v = P * t / V
```

### `energy_per_mass_removed(power_kW, treatment_time_h, volume_m3, c_initial_kg_m3, c_final_kg_m3)`

Calculates energy demand per mass of pollutant removed:

```text
E_m = P * t / [V * (C0 - C)]
```

### `inverse_kapp_indicator(k_app_s)`

Returns a simple indicator proportional to treatment time or energy demand:

```text
indicator = 1 / k_app
```

## `ozonation.py`

This module contains simplified ozone radical-yield calculations.

### `hydroxyl_radical_production_from_ozone(ozone_consumed_mol_L, hydroxyl_yield_mol_per_mol_ozone=0.21)`

Estimates cumulative hydroxyl-radical production from consumed ozone:

```text
OH_produced = Y_OH * O3_consumed
```

### `hydroxyl_radical_generation_rate_from_ozone_rate(ozone_consumption_rate_mol_L_s, hydroxyl_yield_mol_per_mol_ozone=0.21)`

Estimates hydroxyl-radical generation rate from ozone consumption rate:

```text
R_OH = Y_OH * R_O3
```

## `h2o2.py`

This module contains simplified H2O2 radical-yield calculations.

### `hydroxyl_radical_production_from_h2o2(h2o2_consumed_mol_L, hydroxyl_yield_mol_per_mol_h2o2=2.0, efficiency=1.0)`

Estimates cumulative hydroxyl-radical production from consumed or photolyzed H2O2:

```text
OH_produced = efficiency * Y_OH * H2O2_consumed
```

### `hydroxyl_radical_generation_rate_from_h2o2_rate(h2o2_consumption_rate_mol_L_s, hydroxyl_yield_mol_per_mol_h2o2=2.0, efficiency=1.0)`

Estimates hydroxyl-radical generation rate from H2O2 consumption or photolysis rate:

```text
R_OH = efficiency * Y_OH * R_H2O2
```

## `reactor.py`

This module contains simplified reactor-scale dimensionless indicators.

### `damkohler_number(reaction_rate_constant_s, residence_time_s)`

Calculates first-order Damköhler number:

```text
Da = k * tau
```

### `reynolds_number(density_kg_m3, velocity_m_s, characteristic_length_m, dynamic_viscosity_Pa_s)`

Calculates Reynolds number:

```text
Re = rho * u * L / mu
```

### `sherwood_number(mass_transfer_coefficient_m_s, characteristic_length_m, diffusion_coefficient_m2_s)`

Calculates Sherwood number:

```text
Sh = k_L * L / D
```

### `optical_thickness(absorption_coefficient_1_m, path_length_m)`

Calculates optical thickness:

```text
tau_opt = alpha * L
```

### `cavitation_number(pressure_Pa, vapor_pressure_Pa, density_kg_m3, velocity_m_s)`

Calculates cavitation number:

```text
sigma = (p - p_v) / (0.5 * rho * u^2)
```

## `treatment_train.py`

This module contains screening-level treatment-train interpretation.

### `classify_scavenging_capacity(k_scav_s)`

Classifies scavenging capacity as:

```text
low
moderate
high
very_high
```

### `screen_aop_readiness(k_scav_s, doc_mg_C_L=None, turbidity_NTU=None, nitrite_mg_L=None, target="micropollutants")`

Provides screening-level AOP readiness guidance.

The output includes:

```text
classification
main_limitation
recommendation
notes
```

## `plotting.py`

This module contains plotting utilities.

### `plot_scavenging_contributions(table, value_column="percent", label_column="species", title=..., output_file=None)`

Creates a horizontal bar chart of scavenging contributions.

### `plot_doc_sensitivity(results, x_column="DOC_mg_C_L", y_column="eta_percent", title=..., output_file=None)`

Creates a plot showing the effect of DOC on radical utilization efficiency.

## Notes

This API is intended for transparent, screening-level engineering calculations.

The functions are not a replacement for experimental validation, pilot testing, detailed reactor modeling, or final plant design.
