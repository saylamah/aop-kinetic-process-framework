"""
Import tests for the public package interface.
"""

import aop_framework


def test_package_version() -> None:
    """
    Test package version string.
    """
    assert aop_framework.__version__ == "0.1.3"


def test_core_public_imports() -> None:
    """
    Test that core public functions and classes are exposed at package level.
    """
    assert hasattr(aop_framework, "Species")
    assert hasattr(aop_framework, "total_scavenging_capacity")
    assert hasattr(aop_framework, "radical_utilization_efficiency")
    assert hasattr(aop_framework, "scavenging_table")

    assert hasattr(aop_framework, "hydroxyl_radical_steady_state")
    assert hasattr(aop_framework, "apparent_first_order_rate_constant")
    assert hasattr(aop_framework, "first_order_removal_fraction")
    assert hasattr(aop_framework, "first_order_remaining_fraction")
    assert hasattr(aop_framework, "treatment_time_required")

    assert hasattr(aop_framework, "volumetric_energy_consumption")
    assert hasattr(aop_framework, "energy_per_mass_removed")
    assert hasattr(aop_framework, "inverse_kapp_indicator")

    assert hasattr(aop_framework, "hydroxyl_radical_production_from_ozone")
    assert hasattr(aop_framework, "hydroxyl_radical_generation_rate_from_ozone_rate")

    assert hasattr(aop_framework, "hydroxyl_radical_production_from_h2o2")
    assert hasattr(aop_framework, "hydroxyl_radical_generation_rate_from_h2o2_rate")


def test_reactor_public_imports() -> None:
    """
    Test that reactor-scale indicators are exposed at package level.
    """
    assert hasattr(aop_framework, "damkohler_number")
    assert hasattr(aop_framework, "reynolds_number")
    assert hasattr(aop_framework, "sherwood_number")
    assert hasattr(aop_framework, "optical_thickness")
    assert hasattr(aop_framework, "cavitation_number")


def test_treatment_train_public_imports() -> None:
    """
    Test that treatment-train screening utilities are exposed at package level.
    """
    assert hasattr(aop_framework, "AOPScreeningResult")
    assert hasattr(aop_framework, "classify_scavenging_capacity")
    assert hasattr(aop_framework, "screen_aop_readiness")


def test_conversion_public_imports() -> None:
    """
    Test that unit-conversion utilities are exposed at package level.
    """
    assert hasattr(aop_framework, "mg_L_to_mol_L")
    assert hasattr(aop_framework, "ug_L_to_mol_L")
    assert hasattr(aop_framework, "mol_L_to_mg_L")
    assert hasattr(aop_framework, "mol_L_to_ug_L")
    assert hasattr(aop_framework, "mg_C_L_to_mol_C_L")
    assert hasattr(aop_framework, "alkalinity_mg_CaCO3_L_to_eq_L")


def test_carbonate_public_imports() -> None:
    """
    Test that carbonate-system utilities are exposed at package level.
    """
    assert hasattr(aop_framework, "CarbonateSystemResult")
    assert hasattr(aop_framework, "carbonate_bicarbonate_ratio")
    assert hasattr(aop_framework, "estimate_bicarbonate_carbonate_from_alkalinity")
