from aop_framework.h2o2 import (
    hydroxyl_radical_generation_rate_from_h2o2_rate,
    hydroxyl_radical_production_from_h2o2,
)


def test_hydroxyl_radical_production_from_h2o2_ideal():
    h2o2_consumed = 1.0e-5

    oh_produced = hydroxyl_radical_production_from_h2o2(
        h2o2_consumed_mol_L=h2o2_consumed,
    )

    assert abs(oh_produced - 2.0e-5) < 1.0e-18


def test_hydroxyl_radical_production_from_h2o2_with_efficiency():
    h2o2_consumed = 1.0e-5
    efficiency = 0.40

    oh_produced = hydroxyl_radical_production_from_h2o2(
        h2o2_consumed_mol_L=h2o2_consumed,
        efficiency=efficiency,
    )

    assert abs(oh_produced - 8.0e-6) < 1.0e-18


def test_hydroxyl_radical_generation_rate_from_h2o2_rate_ideal():
    h2o2_rate = 1.0e-8

    oh_rate = hydroxyl_radical_generation_rate_from_h2o2_rate(
        h2o2_consumption_rate_mol_L_s=h2o2_rate,
    )

    assert abs(oh_rate - 2.0e-8) < 1.0e-21


def test_hydroxyl_radical_generation_rate_from_h2o2_rate_with_efficiency():
    h2o2_rate = 1.0e-8
    efficiency = 0.25

    oh_rate = hydroxyl_radical_generation_rate_from_h2o2_rate(
        h2o2_consumption_rate_mol_L_s=h2o2_rate,
        efficiency=efficiency,
    )

    assert abs(oh_rate - 5.0e-9) < 1.0e-21
