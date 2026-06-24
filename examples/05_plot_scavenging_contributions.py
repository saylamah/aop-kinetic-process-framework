"""
Example 05: Plot hydroxyl-radical scavenging contributions.

This example calculates the scavenging contribution of each matrix component
and saves a horizontal bar chart as a PNG file.
"""

from pathlib import Path

import pandas as pd

from aop_framework.plotting import plot_scavenging_contributions
from aop_framework.scavenging import Species, scavenging_table


DATA_FILE = Path("data/representative_effluent_matrix.csv")
OUTPUT_DIR = Path("outputs")
OUTPUT_FILE = OUTPUT_DIR / "scavenging_contributions.png"


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
    Generate scavenging contribution plot.
    """
    OUTPUT_DIR.mkdir(exist_ok=True)

    species = load_species_from_csv(DATA_FILE)
    table = scavenging_table(species)

    plot_scavenging_contributions(
        table=table,
        value_column="percent",
        label_column="species",
        title="Hydroxyl-radical scavenging contributions",
        output_file=OUTPUT_FILE,
    )

    print("\nAOP Kinetic Process Framework")
    print("Example 05: Plot scavenging contributions")
    print("-" * 72)
    print(f"\nFigure saved to: {OUTPUT_FILE}")

    print("\nEngineering interpretation:")
    print(
        "The plot shows which matrix components dominate hydroxyl-radical "
        "consumption. Large background scavenging fractions indicate that "
        "only a small fraction of generated radicals is available for target "
        "micropollutant degradation."
    )


if __name__ == "__main__":
    main()
