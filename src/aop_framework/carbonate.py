from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CarbonateSystemResult:
    """
    Simplified carbonate-system speciation result.

    Concentrations are reported in mol/L.
    """

    pH: float
    alkalinity_eq_L: float
    bicarbonate_mol_L: float
    carbonate_mol_L: float
    carbonate_fraction: float
    bicarbonate_fraction: float


def carbonate_bicarbonate_ratio(
    pH: float,
    pka2: float = 10.33,
) -> float:
    """
    Calculate carbonate-to-bicarbonate ratio.

    CO3 / HCO3 = 10^(pH - pKa2)

    Parameters
    ----------
    pH:
        Water pH.
    pka2:
        Second dissociation pKa of carbonic acid.
        Default is 10.33 at approximately 25 C.

    Returns
    -------
    float
        Dimensionless carbonate-to-bicarbonate ratio.
    """
    if pH < 0 or pH > 14:
        raise ValueError("pH should be between 0 and 14.")

    return 10.0 ** (pH - pka2)


def estimate_bicarbonate_carbonate_from_alkalinity(
    alkalinity_eq_L: float,
    pH: float,
    pka2: float = 10.33,
) -> CarbonateSystemResult:
    """
    Estimate bicarbonate and carbonate concentrations from alkalinity and pH.

    Simplified alkalinity relationship:

        Alk = [HCO3-] + 2[CO3--]

    with:

        r = [CO3--] / [HCO3-] = 10^(pH - pKa2)

    Therefore:

        [HCO3-] = Alk / (1 + 2r)
        [CO3--] = r * [HCO3-]

    This is a screening-level calculation and neglects contributions from
    hydroxide, hydrogen ion, organic acids, phosphate, ammonia, borate, and
    other alkalinity contributors.

    Parameters
    ----------
    alkalinity_eq_L:
        Alkalinity in equivalents/L.
    pH:
        Water pH.
    pka2:
        Second dissociation pKa of carbonic acid.

    Returns
    -------
    CarbonateSystemResult
        Estimated bicarbonate and carbonate concentrations.
    """
    if alkalinity_eq_L < 0:
        raise ValueError("Alkalinity cannot be negative.")

    ratio = carbonate_bicarbonate_ratio(pH=pH, pka2=pka2)

    bicarbonate = alkalinity_eq_L / (1.0 + 2.0 * ratio)
    carbonate = ratio * bicarbonate

    total_carbonate_species = bicarbonate + carbonate

    if total_carbonate_species > 0:
        bicarbonate_fraction = bicarbonate / total_carbonate_species
        carbonate_fraction = carbonate / total_carbonate_species
    else:
        bicarbonate_fraction = 0.0
        carbonate_fraction = 0.0

    return CarbonateSystemResult(
        pH=pH,
        alkalinity_eq_L=alkalinity_eq_L,
        bicarbonate_mol_L=bicarbonate,
        carbonate_mol_L=carbonate,
        carbonate_fraction=carbonate_fraction,
        bicarbonate_fraction=bicarbonate_fraction,
    )
