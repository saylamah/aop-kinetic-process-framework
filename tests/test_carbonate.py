from aop_framework.carbonate import (
    carbonate_bicarbonate_ratio,
    estimate_bicarbonate_carbonate_from_alkalinity,
)


def test_carbonate_bicarbonate_ratio_at_pka2():
    ratio = carbonate_bicarbonate_ratio(
        pH=10.33,
        pka2=10.33,
    )

    assert abs(ratio - 1.0) < 1.0e-12


def test_carbonate_bicarbonate_ratio_below_pka2():
    ratio = carbonate_bicarbonate_ratio(
        pH=7.33,
        pka2=10.33,
    )

    assert abs(ratio - 1.0e-3) < 1.0e-15


def test_estimate_bicarbonate_carbonate_from_alkalinity():
    result = estimate_bicarbonate_carbonate_from_alkalinity(
        alkalinity_eq_L=1.0e-3,
        pH=10.33,
        pka2=10.33,
    )

    # At pH = pKa2, [CO3--] / [HCO3-] = 1.
    # Alk = [HCO3-] + 2[CO3--] = 3[HCO3-]
    assert abs(result.bicarbonate_mol_L - (1.0e-3 / 3.0)) < 1.0e-18
    assert abs(result.carbonate_mol_L - (1.0e-3 / 3.0)) < 1.0e-18
    assert abs(result.bicarbonate_fraction - 0.5) < 1.0e-12
    assert abs(result.carbonate_fraction - 0.5) < 1.0e-12


def test_estimate_bicarbonate_carbonate_low_pH():
    result = estimate_bicarbonate_carbonate_from_alkalinity(
        alkalinity_eq_L=1.0e-3,
        pH=7.33,
        pka2=10.33,
    )

    assert result.bicarbonate_mol_L > result.carbonate_mol_L
    assert result.bicarbonate_fraction > 0.99
    assert result.carbonate_fraction < 0.01
