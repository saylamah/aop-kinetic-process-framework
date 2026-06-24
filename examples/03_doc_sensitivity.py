"""
Example 03: DOC sensitivity and radical utilization efficiency.

This example evaluates how changing the dissolved organic carbon (DOC)
scavenging contribution affects the radical utilization efficiency toward
a target micropollutant.

DOC is represented as a lumped pseudo-first-order scavenging term.
"""

from copy import deepcopy
from pathlib import Path

import pandas as pd

from aop_framework.scavenging import (
    Species,
    radical_utilization_efficiency,
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


def find_species(species: list[Species], name: str) -> Species:
    """
    Find a species by name.
    """
    for item in species:
        if item.name == name:
            return item

    raise ValueError(f"Species not found: {name}")


def set_doc_scavenging(
    species: list[Species],
    doc_scavenging_rate_s: float,
) -> list[Species]:
    """
    Return a copied species list with updated lumped DOC scavenging.

    The DOC term is represented as:

        concentration_mol_L = 1.0
        k_oh_L_mol_s = pseudo-first-order DOC scavenging contribution
    """
    updated_species = deepcopy(species)

    doc = find_species(updated_species, "doc_lumped")
    doc.concentration_mol_L = 1.0
    doc.k_oh_L_mol_s = doc_scavenging_rate_s

    return updated_species


def main() -> None:
    """
    Run DOC sensitivity analysis.
    """
    base_species = load_species_from_csv(DATA_FILE)

    target_name = "carbamazepine"

    # Baseline assumption:
    # doc_lumped = 2.30e5 s^-1 at 4.4 mgC/L.
    baseline_doc_mg_C_L = 4.4
    baseline_doc_scavenging_s = 2.30e5

    doc_values_mg_C_L = [
        0.5,
        1.0,
        2.0,
        3.0,
        4.4,
        6.0,
        8.0,
    ]

    rows = []

    for doc_mg_C_L in doc_values_mg_C_L:
        doc_scavenging_s = (
            baseline_doc_scavenging_s
            * doc_mg_C_L
            / baseline_doc_mg_C_L
        )

        species = set_doc_scavenging(
            base_species,
            doc_scavenging_rate_s=doc_scavenging_s,
        )

        target = find_species(species, target_name)

        k_scav = total_scavenging_capacity(species)
        eta = radical_utilization_efficiency(target, species)

        rows.append(
            {
                "DOC_mg_C_L": doc_mg_C_L,
                "DOC_scavenging_s": doc_scavenging_s,
                "total_k_scav_s": k_scav,
                "target": target_name,
                "eta_fraction": eta,
                "eta_percent": 100.0 * eta,
                "relative_treatment_time_indicator": k_scav,
            }
        )

    results = pd.DataFrame(rows)

    print("\nAOP Kinetic Process Framework")
    print("Example 03: DOC sensitivity")
    print("-" * 72)

    print(
        results[
            [
                "DOC_mg_C_L",
                "DOC_scavenging_s",
                "total_k_scav_s",
                "eta_percent",
                "relative_treatment_time_indicator",
            ]
        ].to_string(index=False)
    )

    print("\nEngineering interpretation:")
    print(
        "As DOC increases, total scavenging capacity increases. "
        "For the same radical generation rate, this lowers useful radical "
        "utilization toward the target pollutant and increases the relative "
        "treatment-time or energy penalty."
    )


if __name__ == "__main__":
    main()
