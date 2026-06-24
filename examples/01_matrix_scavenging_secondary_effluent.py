"""
Example 01: Matrix scavenging in a representative secondary effluent.

This example calculates hydroxyl-radical scavenging contributions for a
representative wastewater matrix containing DOC, inorganic scavengers,
and target micropollutants.
"""

from pathlib import Path

import pandas as pd

from aop_framework.scavenging import (
    Species,
    scavenging_table,
    total_scavenging_capacity,
)


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
    Run the scavenging calculation.
    """
    species = load_species_from_csv(DATA_FILE)

    k_scav = total_scavenging_capacity(species)
    table = scavenging_table(species)

    print("\nAOP Kinetic Process Framework")
    print("Example 01: Matrix scavenging in secondary effluent")
    print("-" * 72)

    print(f"\nTotal hydroxyl-radical scavenging capacity:")
    print(f"k_scav = {k_scav:.3e} s^-1")

    print("\nScavenging contribution table:")
    print(
        table[
            [
                "species",
                "group",
                "scavenging_rate_s",
                "fraction",
                "percent",
            ]
        ].to_string(index=False)
    )

    print("\nEngineering interpretation:")
    print(
        "Components with the largest pseudo-first-order scavenging rates "
        "consume the largest share of hydroxyl radicals. In realistic "
        "wastewater matrices, DOC and inorganic scavengers often dominate "
        "radical consumption, while trace micropollutants receive only a "
        "small fraction of generated radicals."
    )


if __name__ == "__main__":
    main()
