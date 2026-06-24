import aop_framework


def test_package_version_exists():
    assert aop_framework.__version__ == "0.1.1"


def test_main_functions_are_exposed():
    assert hasattr(aop_framework, "Species")
    assert hasattr(aop_framework, "total_scavenging_capacity")
    assert hasattr(aop_framework, "hydroxyl_radical_steady_state")
    assert hasattr(aop_framework, "apparent_first_order_rate_constant")
    assert hasattr(aop_framework, "hydroxyl_radical_production_from_ozone")
    assert hasattr(aop_framework, "hydroxyl_radical_production_from_h2o2")
    assert hasattr(aop_framework, "damkohler_number")
    assert hasattr(aop_framework, "screen_aop_readiness")


def test_conversion_functions_are_exposed():
    assert hasattr(aop_framework, "mg_L_to_mol_L")
    assert hasattr(aop_framework, "ug_L_to_mol_L")
    assert hasattr(aop_framework, "mol_L_to_mg_L")
    assert hasattr(aop_framework, "mol_L_to_ug_L")
    assert hasattr(aop_framework, "mg_C_L_to_mol_C_L")
    assert hasattr(aop_framework, "alkalinity_mg_CaCO3_L_to_eq_L")
