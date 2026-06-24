"""
Example 08: Unit conversions for wastewater matrix setup.

This example shows how to convert common wastewater concentration units
into mol/L or equivalent/L before using kinetic calculations.

Common input units in wastewater engineering include:

- microgram/L for micropollutants,
- mg/L for inorganic species,
- mg C/L for dissolved organic carbon,
- mg/L as CaCO3 for alkalinity.
"""

from aop_framework.conversions import (
    alkalinity_mg_CaCO3_L_to_eq_L,
    mg_C_L_to_mol_C_L,
    mg_L_to_mol_L,
    ug_L_to_mol_L,
)


def main() -> None:
    """
    Run example unit conversions.
    """
    # Example micropollutants
    carbamazepine_ug_L = 10.0
    carbamazepine_molar_mass_g_mol = 236.27

    diclofenac_ug_L = 10.0
    diclofenac_molar_mass_g_mol = 296.15

    carbamazepine_mol_L = ug_L_to_mol_L(
        concentration_ug_L=carbamazepine_ug_L,
        molar_mass_g_mol=carbamazepine_molar_mass_g_mol,
    )

    diclofenac_mol_L = ug_L_to_mol_L(
        concentration_ug_L=diclofenac_ug_L,
        molar_mass_g_mol=diclofenac_molar_mass_g_mol,
    )

    # Example inorganic species
    nitrite_mg_L = 0.03
    nitrite_molar_mass_g_mol = 46.0055

    nitrite_mol_L = mg_L_to_mol_L(
        concentration_mg_L=nitrite_mg_L,
        molar_mass_g_mol=nitrite_molar_mass_g_mol,
    )

    # Example DOC
    doc_mg_C_L = 4.4

    doc_mol_C_L = mg_C_L_to_mol_C_L(
        concentration_mg_C_L=doc_mg_C_L,
    )

    # Example alkalinity
    alkalinity_mg_CaCO3_L = 310.0

    alkalinity_eq_L = alkalinity_mg_CaCO3_L_to_eq_L(
        alkalinity_mg_CaCO3_L=alkalinity_mg_CaCO3_L,
    )

    print("\nAOP Kinetic Process Framework")
    print("Example 08: Unit conversions for matrix setup")
    print("-" * 72)

    print("\nMicropollutants:")
    print(
        f"Carbamazepine: {carbamazepine_ug_L:.2f} ug/L "
        f"= {carbamazepine_mol_L:.3e} mol/L"
    )
    print(
        f"Diclofenac:    {diclofenac_ug_L:.2f} ug/L "
        f"= {diclofenac_mol_L:.3e} mol/L"
    )

    print("\nInorganic species:")
    print(
        f"Nitrite:       {nitrite_mg_L:.3f} mg/L "
        f"= {nitrite_mol_L:.3e} mol/L"
    )

    print("\nDissolved organic carbon:")
    print(
        f"DOC:           {doc_mg_C_L:.2f} mg C/L "
        f"= {doc_mol_C_L:.3e} mol C/L"
    )

    print("\nAlkalinity:")
    print(
        f"Alkalinity:    {alkalinity_mg_CaCO3_L:.1f} mg/L as CaCO3 "
        f"= {alkalinity_eq_L:.3e} eq/L"
    )

    print("\nEngineering interpretation:")
    print(
        "Wastewater data are often reported in mass-based units, while kinetic "
        "calculations require molar concentrations. Unit conversion should be "
        "performed carefully before calculating radical scavenging capacity, "
        "radical utilization efficiency, or apparent kinetic constants."
    )


if __name__ == "__main__":
    main()
