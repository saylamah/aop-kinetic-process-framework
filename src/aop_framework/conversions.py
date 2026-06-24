from __future__ import annotations


def mg_L_to_mol_L(
    concentration_mg_L: float,
    molar_mass_g_mol: float,
) -> float:
    """
    Convert concentration from mg/L to mol/L.

    mol/L = (mg/L * 1e-3 g/mg) / molar_mass_g_mol
    """
    if concentration_mg_L < 0:
        raise ValueError("Concentration cannot be negative.")

    if molar_mass_g_mol <= 0:
        raise ValueError("Molar mass must be positive.")

    return concentration_mg_L * 1.0e-3 / molar_mass_g_mol


def ug_L_to_mol_L(
    concentration_ug_L: float,
    molar_mass_g_mol: float,
) -> float:
    """
    Convert concentration from microgram/L to mol/L.

    mol/L = (ug/L * 1e-6 g/ug) / molar_mass_g_mol
    """
    if concentration_ug_L < 0:
        raise ValueError("Concentration cannot be negative.")

    if molar_mass_g_mol <= 0:
        raise ValueError("Molar mass must be positive.")

    return concentration_ug_L * 1.0e-6 / molar_mass_g_mol


def mol_L_to_mg_L(
    concentration_mol_L: float,
    molar_mass_g_mol: float,
) -> float:
    """
    Convert concentration from mol/L to mg/L.

    mg/L = mol/L * molar_mass_g_mol * 1000 mg/g
    """
    if concentration_mol_L < 0:
        raise ValueError("Concentration cannot be negative.")

    if molar_mass_g_mol <= 0:
        raise ValueError("Molar mass must be positive.")

    return concentration_mol_L * molar_mass_g_mol * 1.0e3


def mol_L_to_ug_L(
    concentration_mol_L: float,
    molar_mass_g_mol: float,
) -> float:
    """
    Convert concentration from mol/L to microgram/L.

    ug/L = mol/L * molar_mass_g_mol * 1e6 ug/g
    """
    if concentration_mol_L < 0:
        raise ValueError("Concentration cannot be negative.")

    if molar_mass_g_mol <= 0:
        raise ValueError("Molar mass must be positive.")

    return concentration_mol_L * molar_mass_g_mol * 1.0e6


def mg_C_L_to_mol_C_L(
    concentration_mg_C_L: float,
    carbon_molar_mass_g_mol: float = 12.011,
) -> float:
    """
    Convert dissolved organic carbon from mg C/L to mol C/L.

    This converts carbon mass concentration only. It does not convert DOC
    into a molecular concentration of organic matter.
    """
    if concentration_mg_C_L < 0:
        raise ValueError("DOC concentration cannot be negative.")

    if carbon_molar_mass_g_mol <= 0:
        raise ValueError("Carbon molar mass must be positive.")

    return concentration_mg_C_L * 1.0e-3 / carbon_molar_mass_g_mol


def alkalinity_mg_CaCO3_L_to_eq_L(
    alkalinity_mg_CaCO3_L: float,
) -> float:
    """
    Convert alkalinity from mg/L as CaCO3 to equivalents/L.

    The equivalent weight of CaCO3 is approximately 50.043 g/eq.
    """
    if alkalinity_mg_CaCO3_L < 0:
        raise ValueError("Alkalinity cannot be negative.")

    equivalent_weight_CaCO3_g_eq = 50.043

    return alkalinity_mg_CaCO3_L * 1.0e-3 / equivalent_weight_CaCO3_g_eq
