"""
Example 07: Reactor-scale dimensionless indicators.

This example calculates simplified reactor-scale indicators that are useful
for interpreting AOP performance beyond intrinsic reaction kinetics.

The indicators are screening-level quantities and should not be interpreted
as a substitute for detailed reactor design or CFD.
"""

from aop_framework.reactor import (
    cavitation_number,
    damkohler_number,
    optical_thickness,
    reynolds_number,
    sherwood_number,
)


def main() -> None:
    """
    Run reactor-scale indicator calculations.
    """
    # Representative apparent first-order rate constant and residence time.
    k_app_s = 2.0e-3
    residence_time_s = 500.0

    da = damkohler_number(
        reaction_rate_constant_s=k_app_s,
        residence_time_s=residence_time_s,
    )

    re = reynolds_number(
        density_kg_m3=1000.0,
        velocity_m_s=1.0,
        characteristic_length_m=0.1,
        dynamic_viscosity_Pa_s=1.0e-3,
    )

    sh = sherwood_number(
        mass_transfer_coefficient_m_s=1.0e-5,
        characteristic_length_m=0.01,
        diffusion_coefficient_m2_s=1.0e-9,
    )

    tau_opt = optical_thickness(
        absorption_coefficient_1_m=20.0,
        path_length_m=0.05,
    )

    sigma = cavitation_number(
        pressure_Pa=101325.0,
        vapor_pressure_Pa=2330.0,
        density_kg_m3=1000.0,
        velocity_m_s=10.0,
    )

    print("\nAOP Kinetic Process Framework")
    print("Example 07: Reactor-scale indicators")
    print("-" * 72)

    print(f"\nDamkohler number, Da:       {da:.3f}")
    print(f"Reynolds number, Re:        {re:.3e}")
    print(f"Sherwood number, Sh:        {sh:.3f}")
    print(f"Optical thickness, tau_opt: {tau_opt:.3f}")
    print(f"Cavitation number, sigma:   {sigma:.3f}")

    print("\nEngineering interpretation:")
    print(
        "The apparent reaction rate constant alone is not sufficient for "
        "scale-up. Reactor residence time, hydrodynamics, mass transfer, "
        "optical attenuation, and cavitation conditions can all influence "
        "observable AOP performance."
    )


if __name__ == "__main__":
    main()
