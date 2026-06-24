from aop_framework.ozonation import (
    hydroxyl_radical_generation_rate_from_ozone_rate,
    hydroxyl_radical_production_from_ozone,
)


def test_hydroxyl_radical_production_from_ozone():
    ozone_consumed = 1.0e-5
    yield_oh = 0.21

    oh_produced = hydroxyl_radical_production_from_ozone(
        ozone_consumed_mol_L=ozone_consumed,
        hydroxyl_yield_mol_per_mol_ozone=yield_oh,
    )

    assert oh_produced == 2.1e-6


def test_hydroxyl_radical_generation_rate_from_ozone_rate():
    ozone_rate = 1.0e-8
    yield_oh = 0.21

    oh_rate = hydroxyl_radical_generation_rate_from_ozone_rate(
        ozone_consumption_rate_mol_L_s=ozone_rate,
        hydroxyl_yield_mol_per_mol_ozone=yield_oh,
    )

    assert oh_rate == 2.1e-9
