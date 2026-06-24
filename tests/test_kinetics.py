import math

from aop_framework.kinetics import (
    apparent_first_order_rate_constant,
    first_order_remaining_fraction,
    first_order_removal_fraction,
    hydroxyl_radical_steady_state,
    treatment_time_required,
)


def test_hydroxyl_radical_steady_state():
    r_gen = 1.0e-10
    k_scav = 1.0e5

    oh = hydroxyl_radical_steady_state(r_gen, k_scav)

    assert oh == 1.0e-15


def test_apparent_first_order_rate_constant():
    k_oh = 1.0e9
    oh = 1.0e-15

    k_app = apparent_first_order_rate_constant(k_oh, oh)

    assert abs(k_app - 1.0e-6) < 1.0e-18


def test_first_order_remaining_fraction():
    k_app = 1.0e-3
    t = 1000.0

    remaining = first_order_remaining_fraction(k_app, t)

    assert abs(remaining - math.exp(-1.0)) < 1.0e-12


def test_first_order_removal_fraction():
    k_app = 1.0e-3
    t = 1000.0

    removal = first_order_removal_fraction(k_app, t)

    assert abs(removal - (1.0 - math.exp(-1.0))) < 1.0e-12


def test_treatment_time_required():
    k_app = 1.0e-3
    removal = 0.90

    t_required = treatment_time_required(k_app, removal)

    assert abs(t_required - (-math.log(0.10) / k_app)) < 1.0e-12
