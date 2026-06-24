"""
AOP Kinetic Process Framework.

Python tools for matrix-aware kinetic and process-level evaluation of
advanced oxidation processes in wastewater treatment.
"""
from aop_framework.conversions import (
    alkalinity_mg_CaCO3_L_to_eq_L,
    mg_C_L_to_mol_C_L,
    mg_L_to_mol_L,
    mol_L_to_mg_L,
    mol_L_to_ug_L,
    ug_L_to_mol_L,
)
from aop_framework.energy import (
    energy_per_mass_removed,
    inverse_kapp_indicator,
    volumetric_energy_consumption,
)
from aop_framework.h2o2 import (
    hydroxyl_radical_generation_rate_from_h2o2_rate,
    hydroxyl_radical_production_from_h2o2,
)
from aop_framework.kinetics import (
    apparent_first_order_rate_constant,
    first_order_remaining_fraction,
    first_order_removal_fraction,
    hydroxyl_radical_steady_state,
    treatment_time_required,
)
from aop_framework.ozonation import (
    hydroxyl_radical_generation_rate_from_ozone_rate,
    hydroxyl_radical_production_from_ozone,
)
from aop_framework.reactor import (
    cavitation_number,
    damkohler_number,
    optical_thickness,
    reynolds_number,
    sherwood_number,
)
from aop_framework.scavenging import (
    Species,
    radical_utilization_efficiency,
    scavenging_table,
    total_scavenging_capacity,
)
from aop_framework.treatment_train import (
    AOPScreeningResult,
    classify_scavenging_capacity,
    screen_aop_readiness,
)

__version__ = "0.1.1"

__all__ = [
    "__version__",
    "Species",
    "AOPScreeningResult",
     "mg_L_to_mol_L",
    "ug_L_to_mol_L",
    "mol_L_to_mg_L",
    "mol_L_to_ug_L",
    "mg_C_L_to_mol_C_L",
    "alkalinity_mg_CaCO3_L_to_eq_L",
    "total_scavenging_capacity",
    "radical_utilization_efficiency",
    "scavenging_table",
    "hydroxyl_radical_steady_state",
    "apparent_first_order_rate_constant",
    "first_order_remaining_fraction",
    "first_order_removal_fraction",
    "treatment_time_required",
    "volumetric_energy_consumption",
    "energy_per_mass_removed",
    "inverse_kapp_indicator",
    "hydroxyl_radical_production_from_ozone",
    "hydroxyl_radical_generation_rate_from_ozone_rate",
    "hydroxyl_radical_production_from_h2o2",
    "hydroxyl_radical_generation_rate_from_h2o2_rate",
    "damkohler_number",
    "reynolds_number",
    "sherwood_number",
    "optical_thickness",
    "cavitation_number",
    "classify_scavenging_capacity",
    "screen_aop_readiness",
]
