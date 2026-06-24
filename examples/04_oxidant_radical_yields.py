"""
Example 04: Oxidant radical-yield comparison.

This example compares simplified hydroxyl-radical production estimates
from ozone consumption and H2O2 consumption.

The calculations are screening-level estimates and should not be interpreted
as detailed chain-reaction or radiation-field models.
"""

from aop_framework.h2o2 import hydroxyl_radical_production_from_h2o2
from aop_framework.ozonation import hydroxyl_radical_production_from_ozone


def main() -> None:
    """
    Run oxidant radical-yield comparison.
    """
    oxidant_consumed_mol_L = 1.0e-5

    oh_from_ozone = hydroxyl_radical_production_from_ozone(
        ozone_consumed_mol_L=oxidant_consumed_mol_L,
        hydroxyl_yield_mol_per_mol_ozone=0.21,
    )

    oh_from_h2o2_ideal = hydroxyl_radical_production_from_h2o2(
        h2o2_consumed_mol_L=oxidant_consumed_mol_L,
        hydroxyl_yield_mol_per_mol_h2o2=2.0,
        efficiency=1.0,
    )

    oh_from_h2o2_practical = hydroxyl_radical_production_from_h2o2(
        h2o2_consumed_mol_L=oxidant_consumed_mol_L,
        hydroxyl_yield_mol_per_mol_h2o2=2.0,
        efficiency=0.30,
    )

    print("\nAOP Kinetic Process Framework")
    print("Example 04: Oxidant radical-yield comparison")
    print("-" * 72)

    print(f"\nOxidant consumed: {oxidant_consumed_mol_L:.3e} mol/L")

    print("\nEstimated hydroxyl-radical production:")
    print(f"Ozone, Y_OH = 0.21:              {oh_from_ozone:.3e} mol/L")
    print(f"H2O2 ideal UV photolysis:        {oh_from_h2o2_ideal:.3e} mol/L")
    print(f"H2O2 with 30% efficiency:        {oh_from_h2o2_practical:.3e} mol/L")

    print("\nEngineering interpretation:")
    print(
        "Ozone and H2O2-based AOPs should not be compared only by oxidant dose. "
        "Their useful radical production depends on radical yield, activation "
        "efficiency, water matrix scavenging, radiation or mass-transfer limits, "
        "and reactor configuration."
    )


if __name__ == "__main__":
    main()
