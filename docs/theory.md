# Theory Background

## 1. Purpose of the framework

Advanced oxidation processes are used to degrade persistent organic contaminants in water and wastewater. Their performance depends not only on the intrinsic reactivity of the target pollutant, but also on the wastewater matrix, radical generation rate, reactor conditions, and process configuration.

This framework provides screening-level calculations for connecting radical chemistry with observable treatment performance.

The central idea is that the apparent first-order degradation constant, `k_app`, is a system-level parameter. It reflects the combined influence of:

* radical generation,
* radical scavenging,
* pollutant reactivity,
* matrix composition,
* reactor and transport constraints,
* operating conditions.

## 2. Hydroxyl-radical scavenging capacity

In a wastewater matrix, hydroxyl radicals react with many species at the same time. These include target pollutants, dissolved organic carbon, bicarbonate, carbonate, nitrite, and other background constituents.

For each species `i`, the pseudo-first-order hydroxyl-radical scavenging contribution is:

```text
k_scav,i = kOH,i * C_i
```

where:

```text
kOH,i = second-order rate constant between hydroxyl radical and species i
C_i   = concentration of species i
```

The total scavenging capacity of the matrix is:

```text
k_scav = sum(kOH,i * C_i)
```

This quantity has units of `s^-1`.

## 3. Apparent steady-state hydroxyl-radical concentration

Under a simplified steady-state assumption, the apparent hydroxyl-radical concentration is estimated as:

```text
[OH]_app = R_gen / k_scav
```

where:

```text
[OH]_app = apparent steady-state hydroxyl-radical concentration
R_gen    = volumetric hydroxyl-radical generation rate
k_scav   = total radical scavenging capacity
```

This equation shows why two waters treated with the same oxidant or energy dose can behave very differently. A matrix with high scavenging capacity gives a lower effective radical concentration.

## 4. Apparent first-order degradation constant

For a target pollutant `j`, the apparent first-order degradation constant is:

```text
k_app,j = kOH,j * [OH]_app
```

or, after substituting the steady-state expression:

```text
k_app,j = kOH,j * R_gen / k_scav
```

This means that `k_app` increases when radical generation increases, but decreases when the matrix scavenging capacity increases.

## 5. Radical utilization efficiency

The fraction of hydroxyl radicals reacting with a target pollutant `j` can be expressed as:

```text
eta_j = (kOH,j * C_j) / k_scav
```

where `eta_j` is the radical utilization efficiency toward the target pollutant.

In realistic wastewater, `eta_j` is often very small because dissolved organic carbon and inorganic scavengers are usually present at much higher concentrations than trace micropollutants.

## 6. First-order removal

If the degradation follows apparent first-order behavior:

```text
C / C0 = exp(-k_app * t)
```

The removal fraction is:

```text
removal = 1 - exp(-k_app * t)
```

The required treatment time for a target removal fraction is:

```text
t = -ln(1 - removal) / k_app
```

This relationship shows why small changes in `k_app` can strongly affect reactor residence time and energy demand.

## 7. Energy interpretation

For otherwise similar process conditions, treatment time and energy demand are often proportional to:

```text
1 / k_app
```

Therefore, improving useful radical utilization can reduce treatment time and energy intensity.

However, increasing oxidant dose or energy input alone is not always efficient. If the water matrix has high scavenging capacity, much of the additional radical production may be consumed non-productively by background constituents.

## 8. Ozone radical-yield estimate

For ozone-based systems, hydroxyl-radical production can be estimated using a lumped radical yield:

```text
OH_produced = Y_OH * O3_consumed
```

where a representative value used in this framework is:

```text
Y_OH = 0.21 mol OH per mol O3 consumed
```

This is an empirical lumped estimate. It does not replace detailed ozone decomposition chemistry.

## 9. Hydrogen peroxide radical-yield estimate

For ideal UV/H2O2 photolysis:

```text
H2O2 + UV -> 2 OH
```

The ideal stoichiometric yield is:

```text
Y_OH = 2 mol OH per mol H2O2
```

In practical systems, an efficiency factor is included:

```text
OH_produced = efficiency * Y_OH * H2O2_consumed
```

The efficiency factor accounts for incomplete photolysis, radical recombination, optical attenuation, reactor limitations, and other process losses.

## 10. Engineering use

The framework can be used for:

* comparing wastewater matrices,
* estimating scavenging dominance,
* interpreting apparent degradation constants,
* estimating treatment time,
* comparing simplified oxidant radical yields,
* screening whether AOP treatment is favorable or matrix-limited,
* supporting early-stage process design and teaching.

## 11. Limitations

The current version is intended for screening-level interpretation.

It does not replace:

* laboratory kinetic testing,
* pilot-scale validation,
* detailed ozone-chain chemistry,
* full UV radiation-field modeling,
* CFD or reactor hydrodynamic modeling,
* by-product and transformation-product assessment,
* full-scale plant design,
* regulatory compliance evaluation.

The calculations should be interpreted as transparent engineering estimates, not final design guarantees.
