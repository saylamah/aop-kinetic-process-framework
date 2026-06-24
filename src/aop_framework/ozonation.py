from __future__ import annotations


def hydroxyl_radical_production_from_ozone(
    ozone_consumed_mol_L: float,
    hydroxyl_yield_mol_per_mol_ozone: float = 0.21,
) -> float:
    """
    Estimate cumulative hydroxyl-radical production from consumed ozone.

    [OH]_produced = Y_OH * O3_consumed

    This is a lumped empirical estimate. It does not represent a detailed
    ozone decomposition chain mechanism.

    Parameters
    ----------
    ozone_consumed_mol_L:
        Consumed ozone concentration in mol/L.
    hydroxyl_yield_mol_per_mol_ozone:
        Molar hydroxyl-radical yield per mole of ozone consumed.
        Default value is 0.21 mol OH per mol O3 consumed.

    Returns
    -------
    float
        Estimated cumulative hydroxyl-radical production in mol/L.
    """
    if ozone_consumed_mol_L < 0:
        raise ValueError("Ozone consumed cannot be negative.")

    if hydroxyl_yield_mol_per_mol_ozone < 0:
        raise ValueError("Hydroxyl-radical yield cannot be negative.")

    return hydroxyl_yield_mol_per_mol_ozone * ozone_consumed_mol_L


def hydroxyl_radical_generation_rate_from_ozone_rate(
    ozone_consumption_rate_mol_L_s: float,
    hydroxyl_yield_mol_per_mol_ozone: float = 0.21,
) -> float:
    """
    Estimate hydroxyl-radical generation rate from ozone consumption rate.

    R_OH = Y_OH * R_O3

    Parameters
    ----------
    ozone_consumption_rate_mol_L_s:
        Ozone consumption rate in mol/(L s).
    hydroxyl_yield_mol_per_mol_ozone:
        Molar hydroxyl-radical yield per mole of ozone consumed.

    Returns
    -------
    float
        Estimated hydroxyl-radical generation rate in mol/(L s).
    """
    if ozone_consumption_rate_mol_L_s < 0:
        raise ValueError("Ozone consumption rate cannot be negative.")

    if hydroxyl_yield_mol_per_mol_ozone < 0:
        raise ValueError("Hydroxyl-radical yield cannot be negative.")

    return hydroxyl_yield_mol_per_mol_ozone * ozone_consumption_rate_mol_L_s
