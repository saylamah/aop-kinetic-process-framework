from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import pandas as pd


@dataclass
class Species:
    """
    Chemical or lumped matrix component participating in hydroxyl-radical scavenging.

    Parameters
    ----------
    name:
        Species name.
    concentration_mol_L:
        Concentration in mol/L.

        For lumped DOC terms, this may be set to 1.0 and the rate constant
        may be interpreted as an effective pseudo-first-order contribution.
    k_oh_L_mol_s:
        Second-order hydroxyl-radical rate constant in L/(mol s), or an
        effective lumped value when representing DOC as a pseudo-first-order term.
    group:
        Component group, for example target_micropollutant, inorganic_scavenger,
        or bulk_organic_matter.
    """

    name: str
    concentration_mol_L: float
    k_oh_L_mol_s: float
    group: str = "unspecified"

    @property
    def scavenging_rate_s(self) -> float:
        """
        Return pseudo-first-order scavenging contribution.

        k_scav,i = kOH_i * C_i

        Returns
        -------
        float
            Scavenging contribution in s^-1.
        """
        return self.k_oh_L_mol_s * self.concentration_mol_L


def total_scavenging_capacity(species: Iterable[Species]) -> float:
    """
    Calculate total hydroxyl-radical scavenging capacity.

    k_scav = sum(kOH_i * C_i)

    Parameters
    ----------
    species:
        Iterable of Species objects.

    Returns
    -------
    float
        Total scavenging capacity in s^-1.
    """
    return sum(s.scavenging_rate_s for s in species)


def radical_utilization_efficiency(
    target: Species,
    species: Iterable[Species],
) -> float:
    """
    Calculate radical utilization efficiency toward a target species.

    eta_j = (kOH_j * C_j) / k_scav

    Parameters
    ----------
    target:
        Target pollutant or component.
    species:
        Full matrix including target pollutants and background scavengers.

    Returns
    -------
    float
        Dimensionless radical utilization efficiency.
    """
    k_scav = total_scavenging_capacity(species)

    if k_scav <= 0:
        raise ValueError("Total scavenging capacity must be positive.")

    return target.scavenging_rate_s / k_scav


def scavenging_table(species: Iterable[Species]) -> pd.DataFrame:
    """
    Create a table of scavenging contributions and fractional radical consumption.

    Returns
    -------
    pandas.DataFrame
        Table containing species, group, concentration, rate constant,
        pseudo-first-order scavenging contribution, fraction, and percent.
    """
    species_list = list(species)
    k_scav = total_scavenging_capacity(species_list)

    if k_scav <= 0:
        raise ValueError("Total scavenging capacity must be positive.")

    rows = []

    for s in species_list:
        rows.append(
            {
                "species": s.name,
                "group": s.group,
                "concentration_mol_L": s.concentration_mol_L,
                "k_oh_L_mol_s": s.k_oh_L_mol_s,
                "scavenging_rate_s": s.scavenging_rate_s,
                "fraction": s.scavenging_rate_s / k_scav,
                "percent": 100.0 * s.scavenging_rate_s / k_scav,
            }
        )

    return pd.DataFrame(rows).sort_values(
        "scavenging_rate_s",
        ascending=False,
    )
