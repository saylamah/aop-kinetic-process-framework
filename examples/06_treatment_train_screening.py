"""
Example 06: Treatment-train screening for AOP readiness.

This example uses the representative wastewater matrix to calculate total
hydroxyl-radical scavenging capacity and then provides screening-level
guidance for AOP placement and pretreatment needs.
"""

from pathlib import Path

import pandas as pd

from aop_framework.scavenging import Species, total_scavenging_capacity
from aop_framework.treatment_train import screen_aop_readiness


DATA_FILE = Path("data/representative_effluent_matrix.csv")


def load_species_from_csv(file_path: Path) -> list[Species]:
    """
    Load matrix species from a CSV file.
    """
    df = pd.read_csv(file_path)

    species = []

    for _, row in df.iterrows():
        species.append(
            Species(
                name=row["species"],
                concentration_mol_L=float(row["concentration_mol_L"]),
                k_oh_L_mol_s=float(row["k_oh_L_mol_s"]),
                group=row["group"],
            )
        )

    return species


def main() -> None:
    """
    Run treatment-train screening.
    """
    species = load_species_from_csv(DATA_FILE)

    k_scav = total_scavenging_capacity(species)

    result = screen_aop_readiness(
        k_scav_s=k_scav,
        doc_mg_C_L=4.4,
        turbidity_NTU=3.0,
        nitrite_mg_L=0.03,
        target="micropollutant polishing",
    )

    print("\nAOP Kinetic Process Framework")
    print("Example 06: Treatment-train screening")
    print("-" * 72)

    print(f"\nTotal scavenging capacity: {k_scav:.3e} s^-1")
    print(f"Classification: {result.classification}")
    print(f"Main limitation: {result.main_limitation}")

    print("\nRecommendation:")
    print(result.recommendation)

    print("\nNotes:")
    for note in result.notes:
        print(f"- {note}")

    print("\nEngineering interpretation:")
    print(
        "AOPs are most efficient when applied after upstream treatment has "
        "reduced suspended solids, DOC, nitrite, and other radical scavengers. "
        "If matrix scavenging remains high, increasing oxidant or energy dose "
        "alone may not be the most efficient strategy."
    )


if __name__ == "__main__":
    main()
