from aop_framework.conversions import (
    alkalinity_mg_CaCO3_L_to_eq_L,
    mg_C_L_to_mol_C_L,
    mg_L_to_mol_L,
    mol_L_to_mg_L,
    mol_L_to_ug_L,
    ug_L_to_mol_L,
)


def test_mg_L_to_mol_L():
    concentration = mg_L_to_mol_L(
        concentration_mg_L=100.0,
        molar_mass_g_mol=100.0,
    )

    assert abs(concentration - 1.0e-3) < 1.0e-15


def test_ug_L_to_mol_L():
    concentration = ug_L_to_mol_L(
        concentration_ug_L=100.0,
        molar_mass_g_mol=100.0,
    )

    assert abs(concentration - 1.0e-6) < 1.0e-18


def test_mol_L_to_mg_L():
    concentration = mol_L_to_mg_L(
        concentration_mol_L=1.0e-3,
        molar_mass_g_mol=100.0,
    )

    assert abs(concentration - 100.0) < 1.0e-12


def test_mol_L_to_ug_L():
    concentration = mol_L_to_ug_L(
        concentration_mol_L=1.0e-6,
        molar_mass_g_mol=100.0,
    )

    assert abs(concentration - 100.0) < 1.0e-12


def test_mg_C_L_to_mol_C_L():
    concentration = mg_C_L_to_mol_C_L(
        concentration_mg_C_L=12.011,
    )

    assert abs(concentration - 1.0e-3) < 1.0e-15


def test_alkalinity_mg_CaCO3_L_to_eq_L():
    alkalinity = alkalinity_mg_CaCO3_L_to_eq_L(
        alkalinity_mg_CaCO3_L=50.043,
    )

    assert abs(alkalinity - 1.0e-3) < 1.0e-15
