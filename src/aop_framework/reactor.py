from __future__ import annotations


def damkohler_number(
    reaction_rate_constant_s: float,
    residence_time_s: float,
) -> float:
    """
    Calculate first-order Damköhler number.

    Da = k * tau

    Parameters
    ----------
    reaction_rate_constant_s:
        Apparent first-order rate constant in s^-1.
    residence_time_s:
        Hydraulic residence time in seconds.

    Returns
    -------
    float
        Dimensionless Damköhler number.
    """
    if reaction_rate_constant_s < 0:
        raise ValueError("Reaction rate constant cannot be negative.")

    if residence_time_s < 0:
        raise ValueError("Residence time cannot be negative.")

    return reaction_rate_constant_s * residence_time_s


def reynolds_number(
    density_kg_m3: float,
    velocity_m_s: float,
    characteristic_length_m: float,
    dynamic_viscosity_Pa_s: float,
) -> float:
    """
    Calculate Reynolds number.

    Re = rho * u * L / mu

    Parameters
    ----------
    density_kg_m3:
        Fluid density in kg/m3.
    velocity_m_s:
        Characteristic velocity in m/s.
    characteristic_length_m:
        Characteristic length in m.
    dynamic_viscosity_Pa_s:
        Dynamic viscosity in Pa s.

    Returns
    -------
    float
        Dimensionless Reynolds number.
    """
    if density_kg_m3 <= 0:
        raise ValueError("Density must be positive.")

    if velocity_m_s < 0:
        raise ValueError("Velocity cannot be negative.")

    if characteristic_length_m <= 0:
        raise ValueError("Characteristic length must be positive.")

    if dynamic_viscosity_Pa_s <= 0:
        raise ValueError("Dynamic viscosity must be positive.")

    return (
        density_kg_m3
        * velocity_m_s
        * characteristic_length_m
        / dynamic_viscosity_Pa_s
    )


def sherwood_number(
    mass_transfer_coefficient_m_s: float,
    characteristic_length_m: float,
    diffusion_coefficient_m2_s: float,
) -> float:
    """
    Calculate Sherwood number.

    Sh = k_L * L / D

    Parameters
    ----------
    mass_transfer_coefficient_m_s:
        Mass-transfer coefficient in m/s.
    characteristic_length_m:
        Characteristic length in m.
    diffusion_coefficient_m2_s:
        Diffusion coefficient in m2/s.

    Returns
    -------
    float
        Dimensionless Sherwood number.
    """
    if mass_transfer_coefficient_m_s < 0:
        raise ValueError("Mass-transfer coefficient cannot be negative.")

    if characteristic_length_m <= 0:
        raise ValueError("Characteristic length must be positive.")

    if diffusion_coefficient_m2_s <= 0:
        raise ValueError("Diffusion coefficient must be positive.")

    return (
        mass_transfer_coefficient_m_s
        * characteristic_length_m
        / diffusion_coefficient_m2_s
    )


def optical_thickness(
    absorption_coefficient_1_m: float,
    path_length_m: float,
) -> float:
    """
    Calculate optical thickness.

    tau_opt = alpha * L

    Parameters
    ----------
    absorption_coefficient_1_m:
        Optical absorption coefficient in 1/m.
    path_length_m:
        Optical path length in m.

    Returns
    -------
    float
        Dimensionless optical thickness.
    """
    if absorption_coefficient_1_m < 0:
        raise ValueError("Absorption coefficient cannot be negative.")

    if path_length_m < 0:
        raise ValueError("Path length cannot be negative.")

    return absorption_coefficient_1_m * path_length_m


def cavitation_number(
    pressure_Pa: float,
    vapor_pressure_Pa: float,
    density_kg_m3: float,
    velocity_m_s: float,
) -> float:
    """
    Calculate cavitation number.

    sigma = (p - p_v) / (0.5 * rho * u^2)

    Parameters
    ----------
    pressure_Pa:
        Local or downstream pressure in Pa.
    vapor_pressure_Pa:
        Vapor pressure of the liquid in Pa.
    density_kg_m3:
        Liquid density in kg/m3.
    velocity_m_s:
        Characteristic velocity in m/s.

    Returns
    -------
    float
        Dimensionless cavitation number.
    """
    if density_kg_m3 <= 0:
        raise ValueError("Density must be positive.")

    if velocity_m_s <= 0:
        raise ValueError("Velocity must be positive.")

    dynamic_pressure = 0.5 * density_kg_m3 * velocity_m_s**2

    return (pressure_Pa - vapor_pressure_Pa) / dynamic_pressure
