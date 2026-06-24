from __future__ import annotations


def volumetric_energy_consumption(
    power_kW: float,
    treatment_time_h: float,
    volume_m3: float,
) -> float:
    """
    Calculate volumetric energy consumption.

    E_v = P * t / V

    Parameters
    ----------
    power_kW:
        Electrical or process power input in kW.
    treatment_time_h:
        Treatment time in hours.
    volume_m3:
        Treated water volume in m3.

    Returns
    -------
    float
        Volumetric energy consumption in kWh/m3.
    """
    if power_kW < 0:
        raise ValueError("Power cannot be negative.")

    if treatment_time_h < 0:
        raise ValueError("Treatment time cannot be negative.")

    if volume_m3 <= 0:
        raise ValueError("Volume must be positive.")

    return power_kW * treatment_time_h / volume_m3


def energy_per_mass_removed(
    power_kW: float,
    treatment_time_h: float,
    volume_m3: float,
    c_initial_kg_m3: float,
    c_final_kg_m3: float,
) -> float:
    """
    Calculate energy demand per mass of pollutant removed.

    E_m = P * t / [V * (C0 - C)]

    Parameters
    ----------
    power_kW:
        Electrical or process power input in kW.
    treatment_time_h:
        Treatment time in hours.
    volume_m3:
        Treated water volume in m3.
    c_initial_kg_m3:
        Initial pollutant concentration in kg/m3.
    c_final_kg_m3:
        Final pollutant concentration in kg/m3.

    Returns
    -------
    float
        Energy demand in kWh/kg removed.
    """
    if power_kW < 0:
        raise ValueError("Power cannot be negative.")

    if treatment_time_h < 0:
        raise ValueError("Treatment time cannot be negative.")

    if volume_m3 <= 0:
        raise ValueError("Volume must be positive.")

    if c_initial_kg_m3 <= c_final_kg_m3:
        raise ValueError("Initial concentration must be greater than final concentration.")

    mass_removed_kg = volume_m3 * (c_initial_kg_m3 - c_final_kg_m3)

    return power_kW * treatment_time_h / mass_removed_kg


def inverse_kapp_indicator(k_app_s: float) -> float:
    """
    Calculate a simple indicator proportional to treatment time or energy demand.

    For first-order treatment behavior:

    treatment time is proportional to 1 / k_app

    This function is useful for comparing scenarios under otherwise similar
    process assumptions.

    Parameters
    ----------
    k_app_s:
        Apparent first-order degradation rate constant in s^-1.

    Returns
    -------
    float
        Inverse k_app indicator in seconds.
    """
    if k_app_s <= 0:
        raise ValueError("k_app must be positive.")

    return 1.0 / k_app_s
