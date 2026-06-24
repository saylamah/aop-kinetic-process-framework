from __future__ import annotations

import math


def hydroxyl_radical_steady_state(
    radical_generation_rate_mol_L_s: float,
    scavenging_capacity_s: float,
) -> float:
    """
    Estimate apparent steady-state hydroxyl-radical concentration.

    [OH]_app = R_gen / k_scav

    Parameters
    ----------
    radical_generation_rate_mol_L_s:
        Volumetric hydroxyl-radical generation rate in mol/(L s).
    scavenging_capacity_s:
        Total matrix scavenging capacity in s^-1.

    Returns
    -------
    float
        Apparent steady-state hydroxyl-radical concentration in mol/L.
    """
    if radical_generation_rate_mol_L_s < 0:
        raise ValueError("Radical generation rate cannot be negative.")

    if scavenging_capacity_s <= 0:
        raise ValueError("Scavenging capacity must be positive.")

    return radical_generation_rate_mol_L_s / scavenging_capacity_s


def apparent_first_order_rate_constant(
    k_oh_target_L_mol_s: float,
    oh_concentration_mol_L: float,
) -> float:
    """
    Calculate apparent first-order degradation rate constant.

    k_app = kOH,target * [OH]_app

    Parameters
    ----------
    k_oh_target_L_mol_s:
        Second-order rate constant of the target pollutant with hydroxyl radical
        in L/(mol s).
    oh_concentration_mol_L:
        Apparent hydroxyl-radical concentration in mol/L.

    Returns
    -------
    float
        Apparent first-order degradation rate constant in s^-1.
    """
    if k_oh_target_L_mol_s < 0:
        raise ValueError("Target rate constant cannot be negative.")

    if oh_concentration_mol_L < 0:
        raise ValueError("Hydroxyl-radical concentration cannot be negative.")

    return k_oh_target_L_mol_s * oh_concentration_mol_L


def first_order_remaining_fraction(
    k_app_s: float,
    treatment_time_s: float,
) -> float:
    """
    Calculate remaining concentration fraction for first-order degradation.

    C / C0 = exp(-k_app * t)

    Parameters
    ----------
    k_app_s:
        Apparent first-order degradation rate constant in s^-1.
    treatment_time_s:
        Treatment time in seconds.

    Returns
    -------
    float
        Remaining fraction C/C0.
    """
    if k_app_s < 0:
        raise ValueError("k_app cannot be negative.")

    if treatment_time_s < 0:
        raise ValueError("Treatment time cannot be negative.")

    return math.exp(-k_app_s * treatment_time_s)


def first_order_removal_fraction(
    k_app_s: float,
    treatment_time_s: float,
) -> float:
    """
    Calculate removal fraction for first-order degradation.

    removal = 1 - exp(-k_app * t)

    Parameters
    ----------
    k_app_s:
        Apparent first-order degradation rate constant in s^-1.
    treatment_time_s:
        Treatment time in seconds.

    Returns
    -------
    float
        Removal fraction between 0 and 1.
    """
    return 1.0 - first_order_remaining_fraction(k_app_s, treatment_time_s)


def treatment_time_required(
    k_app_s: float,
    removal_fraction: float,
) -> float:
    """
    Calculate treatment time required to reach a target removal fraction.

    t = -ln(1 - removal) / k_app

    Parameters
    ----------
    k_app_s:
        Apparent first-order degradation rate constant in s^-1.
    removal_fraction:
        Target removal fraction between 0 and 1.

    Returns
    -------
    float
        Required treatment time in seconds.
    """
    if k_app_s <= 0:
        raise ValueError("k_app must be positive.")

    if not 0 < removal_fraction < 1:
        raise ValueError("Removal fraction must be between 0 and 1.")

    return -math.log(1.0 - removal_fraction) / k_app_s
