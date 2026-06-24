"""
Example 10: Effect of pH on carbonate-system radical scavenging.

This example evaluates how pH changes bicarbonate/carbonate speciation
and hydroxyl-radical scavenging capacity at fixed alkalinity.

The calculation is screening-level and does not replace full aqueous
equilibrium modeling.
"""

import pandas as pd

from aop_framework.carbonate import (
    estimate_bicarbonate_carbonate_from_alkalinity,
)
from aop_framework.conversions import alkalinity_mg_CaCO3_L_to_eq_L
from aop_framework.scavenging import Species, total_scavenging_capacity


def main() -> None:
    """
    Run pH-sensitivity calculation for carbonate-system scavenging.
    """
    alkalinity_mg_CaCO3_L = 310.0

    alkalinity_eq_L = alkalinity_mg_CaCO3_L_to_eq_L(
        alkalinity_mg_CaCO3_L=alkalinity_mg_CaCO3_L,
    )

    pH_values = [
        6.5,
        7.0,
        7.5,
        8.0,
        8.5,
        9.0,
        9.5,
        10.0,
        10.5,
    ]

    rows = []

    for pH in pH_values:
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

        rows.append(
            {
                "pH": pH,
                "bicarbonate_mol_L": carbonate_result.bicarbonate_mol_L,
                "carbonate_mol_L": carbonate_result.carbonate_mol_L,
                "bicarbonate_fraction": carbonate_result.bicarbonate_fraction,
                "carbonate_fraction": carbonate_result.carbonate_fraction,
                "carbonate_system_k_scav_s": k_scav,
            }
        )

    results = pd.DataFrame(rows)

    print("\nAOP Kinetic Process Framework")
    print("Example 10: pH effect on carbonate-system scavenging")
    print("-" * 72)

    print("\nInput:")
    print(f"Alkalinity: {alkalinity_mg_CaCO3_L:.1f} mg/L as CaCO3")
    print(f"Alkalinity: {alkalinity_eq_L:.3e} eq/L")

    print("\nResults:")
    print(
        results[
            [
                "pH",
                "bicarbonate_mol_L",
                "carbonate_mol_L",
                "carbonate_fraction",
                "carbonate_system_k_scav_s",
            ]
        ].to_string(index=False)
    )

    print("\nEngineering interpretation:")
    print(
        "At fixed alkalinity, increasing pH shifts part of the carbonate system "
        "from bicarbonate toward carbonate. Because carbonate reacts much faster "
        "with hydroxyl radicals than bicarbonate, alkaline conditions can increase "
        "inorganic radical scavenging and reduce useful radical availability for "
        "target micropollutants."
    )


if __name__ == "__main__":
    main()
