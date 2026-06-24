from aop_framework.energy import (
    energy_per_mass_removed,
    inverse_kapp_indicator,
    volumetric_energy_consumption,
)


def test_volumetric_energy_consumption():
    power_kW = 10.0
    treatment_time_h = 2.0
    volume_m3 = 5.0

    energy = volumetric_energy_consumption(
        power_kW,
        treatment_time_h,
        volume_m3,
    )

    assert energy == 4.0


def test_energy_per_mass_removed():
    power_kW = 10.0
    treatment_time_h = 2.0
    volume_m3 = 5.0
    c_initial_kg_m3 = 0.010
    c_final_kg_m3 = 0.002

    energy = energy_per_mass_removed(
        power_kW,
        treatment_time_h,
        volume_m3,
        c_initial_kg_m3,
        c_final_kg_m3,
    )

    expected = 20.0 / (5.0 * (0.010 - 0.002))

    assert energy == expected


def test_inverse_kapp_indicator():
    k_app_s = 2.0e-3

    indicator = inverse_kapp_indicator(k_app_s)

    assert indicator == 500.0
