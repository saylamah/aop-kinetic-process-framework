from aop_framework.scavenging import (
    Species,
    radical_utilization_efficiency,
    total_scavenging_capacity,
)


def test_total_scavenging_capacity():
    species = [
        Species("target", 1.0e-6, 1.0e9),
        Species("background", 2.0e-3, 1.0e6),
    ]

    k_scav = total_scavenging_capacity(species)

    assert k_scav == 3000.0


def test_radical_utilization_efficiency():
    target = Species("target", 1.0e-6, 1.0e9)
    background = Species("background", 2.0e-3, 1.0e6)

    species = [target, background]

    eta = radical_utilization_efficiency(target, species)

    assert abs(eta - (1000.0 / 3000.0)) < 1.0e-12
