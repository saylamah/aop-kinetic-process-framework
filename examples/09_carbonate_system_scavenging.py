"""
Example 09: Carbonate-system scavenging estimate.

This example estimates bicarbonate and carbonate concentrations from
alkalinity and pH, then calculates their hydroxyl-radical scavenging
contributions.

The carbonate-system calculation is simplified and intended for
screening-level interpretation.
"""

from aop_framework.carbonate import (
    estimate_bicarbonate_carbonate_from_alkalinity,
)
from aop_framework.conversions import alkalinity_mg_CaCO3_L_to_eq_L
from aop_framework.scavenging import Species, scavenging_table, total_scavenging_capacity


def main() -> None:
    """
    Run carbonate-system scavenging calculation.
    """
    alkalinity_mg_CaCO3_L = 310.0
    pH = 7.8

    alkalinity_eq_L = alkalinity_mg_CaCO3_L_to_eq_L(
        alkalinity_mg_CaCO3_L=alkalinity_mg_CaCO3_L,
    )

    carbonate_result = estimate_bicarbonate_carbonate_from_alkalinity(
        alkalinity_eq_L=alkalinity_eq_L,
        pH=pH,
    )

    bicarbonate = Species(
        name="bicarbonate",
        concentration_mol_L=carbonate_result.bicarbonate_mol_L,
        k_oh_L_mol_s=8.5e6,
        group="inorganic_scavenger",
    )

    carbonate = Species(
        name="carbonate",
        concentration_mol_L=carbonate_result.carbonate_mol_L,
        k_oh_L_mol_s=3.9e8,
        group="inorganic_scavenger",
    )

    species = [bicarbonate, carbonate]

    k_scav = total_scavenging_capacity(species)
    table = scavenging_table(species)

    print("\nAOP Kinetic Process Framework")
    print("Example 09: Carbonate-system scavenging estimate")
    print("-" * 72)

    print("\nInput:")
    print(f"Alkalinity: {alkalinity_mg_CaCO3_L:.1f} mg/L as CaCO3")
    print(f"pH:         {pH:.2f}")

    print("\nEstimated carbonate system:")
    print(f"Alkalinity:  {alkalinity_eq_L:.3e} eq/L")
    print(f"Bicarbonate: {carbonate_result.bicarbonate_mol_L:.3e} mol/L")
    print(f"Carbonate:   {carbonate_result.carbonate_mol_L:.3e} mol/L")
    print(f"HCO3 fraction: {carbonate_result.bicarbonate_fraction:.4f}")
    print(f"CO3 fraction:  {carbonate_result.carbonate_fraction:.4f}")

    print("\nHydroxyl-radical scavenging:")
    print(f"Total carbonate-system scavenging capacity: {k_scav:.3e} s^-1")

    print("\nContribution table:")
    print(
        table[
            [
                "species",
                "concentration_mol_L",
                "k_oh_L_mol_s",
                "scavenging_rate_s",
                "percent",
            ]
        ].to_string(index=False)
    )

    print("\nEngineering interpretation:")
    print(
        "Bicarbonate is usually the dominant carbonate-system species near "
        "neutral pH, but carbonate has a much higher hydroxyl-radical rate "
        "constant. Therefore, pH changes can strongly affect inorganic "
        "radical scavenging in AOP systems."
    )


if __name__ == "__main__":
    main()
