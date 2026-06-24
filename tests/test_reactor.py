from aop_framework.reactor import (
    cavitation_number,
    damkohler_number,
    optical_thickness,
    reynolds_number,
    sherwood_number,
)


def test_damkohler_number():
    da = damkohler_number(
        reaction_rate_constant_s=2.0e-3,
        residence_time_s=500.0,
    )

    assert da == 1.0


def test_reynolds_number():
    re = reynolds_number(
        density_kg_m3=1000.0,
        velocity_m_s=1.0,
        characteristic_length_m=0.1,
        dynamic_viscosity_Pa_s=1.0e-3,
    )

    assert re == 100000.0


def test_sherwood_number():
    sh = sherwood_number(
        mass_transfer_coefficient_m_s=1.0e-5,
        characteristic_length_m=0.01,
        diffusion_coefficient_m2_s=1.0e-9,
    )

    assert sh == 100.0


def test_optical_thickness():
    tau = optical_thickness(
        absorption_coefficient_1_m=20.0,
        path_length_m=0.05,
    )

    assert tau == 1.0


def test_cavitation_number():
    sigma = cavitation_number(
        pressure_Pa=101325.0,
        vapor_pressure_Pa=2330.0,
        density_kg_m3=1000.0,
        velocity_m_s=10.0,
    )

    expected = (101325.0 - 2330.0) / (0.5 * 1000.0 * 10.0**2)

    assert abs(sigma - expected) < 1.0e-12
