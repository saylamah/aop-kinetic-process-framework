from __future__ import annotations


def hydroxyl_radical_production_from_h2o2(
    h2o2_consumed_mol_L: float,
    hydroxyl_yield_mol_per_mol_h2o2: float = 2.0,
    efficiency: float = 1.0,
) -> float:
    """
    Estimate cumulative hydroxyl-radical production from consumed H2O2.

    For ideal UV/H2O2 photolysis:

        H2O2 + UV -> 2 OH

    Therefore, the ideal stoichiometric yield is 2 mol OH per mol H2O2.

    This function includes an efficiency factor to represent non-ideal operation,
    incomplete photolysis, recombination, optical limitations, or process losses.

    OH_produced = efficiency * Y_OH * H2O2_consumed

    Parameters
    ----------
    h2o2_consumed_mol_L:
        Consumed or photolyzed hydrogen peroxide concentration in mol/L.
    hydroxyl_yield_mol_per_mol_h2o2:
        Hydroxyl-radical yield per mole of H2O2 consumed.
        Default is 2.0 for ideal UV/H2O2 photolysis.
    efficiency:
        Dimensionless efficiency factor between 0 and 1.

    Returns
    -------
    float
        Estimated cumulative hydroxyl-radical production in mol/L.
    """
    if h2o2_consumed_mol_L < 0:
        raise ValueError("H2O2 consumed cannot be negative.")

    if hydroxyl_yield_mol_per_mol_h2o2 < 0:
        raise ValueError("Hydroxyl-radical yield cannot be negative.")

    if not 0 <= efficiency <= 1:
        raise ValueError("Efficiency must be between 0 and 1.")

    return (
        efficiency
        * hydroxyl_yield_mol_per_mol_h2o2
        * h2o2_consumed_mol_L
    )


def hydroxyl_radical_generation_rate_from_h2o2_rate(
    h2o2_consumption_rate_mol_L_s: float,
    hydroxyl_yield_mol_per_mol_h2o2: float = 2.0,
    efficiency: float = 1.0,
) -> float:
    """
    Estimate hydroxyl-radical generation rate from H2O2 consumption rate.

    R_OH = efficiency * Y_OH * R_H2O2

    Parameters
    ----------
    h2o2_consumption_rate_mol_L_s:
        H2O2 consumption or photolysis rate in mol/(L s).
    hydroxyl_yield_mol_per_mol_h2o2:
        Hydroxyl-radical yield per mole of H2O2 consumed.
    efficiency:
        Dimensionless efficiency factor between 0 and 1.

    Returns
    -------
    float
        Estimated hydroxyl-radical generation rate in mol/(L s).
    """
    if h2o2_consumption_rate_mol_L_s < 0:
        raise ValueError("H2O2 consumption rate cannot be negative.")

    if hydroxyl_yield_mol_per_mol_h2o2 < 0:
        raise ValueError("Hydroxyl-radical yield cannot be negative.")

    if not 0 <= efficiency <= 1:
        raise ValueError("Efficiency must be between 0 and 1.")

    return (
        efficiency
        * hydroxyl_yield_mol_per_mol_h2o2
        * h2o2_consumption_rate_mol_L_s
    )
