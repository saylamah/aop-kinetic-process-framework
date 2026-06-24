# Quickstart

This page explains how to install and run the AOP Kinetic Process Framework.

## 1. Clone the repository

```bash
git clone https://github.com/saylamah/aop-kinetic-process-framework.git
cd aop-kinetic-process-framework
```

## 2. Create a Python environment

On macOS or Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

## 3. Install the package

```bash
pip install -e ".[dev]"
```

This installs the package in editable mode together with development tools such as `pytest` and `jupyter`.

## 4. Run the tests

```bash
pytest
```

All tests should pass.

## 5. Run the first example

```bash
python examples/01_matrix_scavenging_secondary_effluent.py
```

This example calculates hydroxyl-radical scavenging contributions in a representative secondary-effluent matrix.

## 6. Run all examples

```bash
python examples/01_matrix_scavenging_secondary_effluent.py
python examples/02_kapp_and_treatment_time.py
python examples/03_doc_sensitivity.py
python examples/04_oxidant_radical_yields.py
python examples/05_plot_scavenging_contributions.py
python examples/06_treatment_train_screening.py
python examples/07_reactor_scale_indicators.py
python examples/08_unit_conversions_for_matrix_setup.py
python examples/09_carbonate_system_scavenging.py
python examples/10_pH_effect_on_carbonate_scavenging.py
```

## 7. Basic Python usage

```python
from aop_framework import (
    Species,
    total_scavenging_capacity,
    radical_utilization_efficiency,
)

target = Species(
    name="carbamazepine",
    concentration_mol_L=4.23e-8,
    k_oh_L_mol_s=1.0e9,
    group="target_micropollutant",
)

bicarbonate = Species(
    name="bicarbonate",
    concentration_mol_L=6.20e-3,
    k_oh_L_mol_s=8.50e6,
    group="inorganic_scavenger",
)

species = [target, bicarbonate]

k_scav = total_scavenging_capacity(species)
eta = radical_utilization_efficiency(target, species)

print(k_scav)
print(eta)
```

## 8. Interpretation

The calculated scavenging capacity indicates how strongly the wastewater matrix consumes hydroxyl radicals.

The radical utilization efficiency indicates what fraction of generated hydroxyl radicals reacts with the target pollutant.

Low radical utilization efficiency means that most radicals are consumed by background matrix constituents rather than by the target contaminant.

## 9. Important note

The framework provides screening-level engineering calculations.

It should be used together with wastewater characterization, laboratory experiments, pilot testing, and site-specific engineering judgment.
