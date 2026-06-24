"""
Example 02: Apparent rate constant and treatment time.

This example calculates the apparent hydroxyl-radical concentration,
the apparent first-order degradation constant k_app, and the treatment
time required for 90% removal of a target micropollutant.
"""

from pathlib import Path

import pandas as pd

from aop_framework.kinetics import (
    apparent_first_order_rate_constant,
    hydroxyl_radical_steady_state,
    treatment_time_required,
)
from aop_framework.scavenging import Species, total_scavenging_capacity


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


def main() -> None:
    """
    Run the apparent-kinetics calculation.
    """
    species = load_species_from_csv(DATA_FILE)

    target = find_species(species, "carbamazepine")

    # Assumed hydroxyl-radical generation rate.
    # This is a user-defined process parameter and should be replaced by
    # process-specific or experimentally estimated values when available.
    radical_generation_rate = 1.0e-10  # mol/(L s)

    k_scav = total_scavenging_capacity(species)

    oh_app = hydroxyl_radical_steady_state(
        radical_generation_rate_mol_L_s=radical_generation_rate,
        scavenging_capacity_s=k_scav,
    )

    k_app = apparent_first_order_rate_constant(
        k_oh_target_L_mol_s=target.k_oh_L_mol_s,
        oh_concentration_mol_L=oh_app,
    )

    removal_target = 0.90

    t_required_s = treatment_time_required(
        k_app_s=k_app,
        removal_fraction=removal_target,
    )

    t_required_min = t_required_s / 60.0

    print("\nAOP Kinetic Process Framework")
    print("Example 02: k_app and treatment time")
    print("-" * 72)

    print(f"\nTarget pollutant: {target.name}")
    print(f"Radical generation rate: {radical_generation_rate:.3e} mol/(L s)")
    print(f"Total scavenging capacity: {k_scav:.3e} s^-1")
    print(f"Apparent [OH]: {oh_app:.3e} mol/L")
    print(f"Apparent k_app: {k_app:.3e} s^-1")

    print(f"\nTreatment time for {removal_target * 100:.0f}% removal:")
    print(f"{t_required_s:.3e} s")
    print(f"{t_required_min:.2f} min")

    print("\nEngineering interpretation:")
    print(
        "For a fixed radical generation rate, higher matrix scavenging lowers "
        "the apparent hydroxyl-radical concentration. This reduces k_app and "
        "increases the treatment time required to reach a target removal."
    )


if __name__ == "__main__":
    main()
