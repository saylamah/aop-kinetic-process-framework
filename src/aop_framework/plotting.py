from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def plot_scavenging_contributions(
    table: pd.DataFrame,
    value_column: str = "percent",
    label_column: str = "species",
    title: str = "Hydroxyl-radical scavenging contributions",
    output_file: str | Path | None = None,
):
    """
    Plot hydroxyl-radical scavenging contributions.

    Parameters
    ----------
    table:
        DataFrame containing scavenging results.
    value_column:
        Column to plot. Common choices are "percent", "fraction",
        or "scavenging_rate_s".
    label_column:
        Column used for species labels.
    title:
        Plot title.
    output_file:
        Optional path for saving the figure.

    Returns
    -------
    matplotlib.axes.Axes
        Plot axis.
    """
    if value_column not in table.columns:
        raise ValueError(f"Column not found: {value_column}")

    if label_column not in table.columns:
        raise ValueError(f"Column not found: {label_column}")

    plot_data = table.sort_values(value_column, ascending=True)

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.barh(
        plot_data[label_column],
        plot_data[value_column],
    )

    ax.set_xlabel(value_column)
    ax.set_ylabel(label_column)
    ax.set_title(title)

    fig.tight_layout()

    if output_file is not None:
        fig.savefig(output_file, dpi=300, bbox_inches="tight")

    return ax


def plot_doc_sensitivity(
    results: pd.DataFrame,
    x_column: str = "DOC_mg_C_L",
    y_column: str = "eta_percent",
    title: str = "Effect of DOC on radical utilization efficiency",
    output_file: str | Path | None = None,
):
    """
    Plot DOC sensitivity results.

    Parameters
    ----------
    results:
        DataFrame containing DOC sensitivity results.
    x_column:
        Column for DOC concentration.
    y_column:
        Column for radical utilization efficiency or related metric.
    title:
        Plot title.
    output_file:
        Optional path for saving the figure.

    Returns
    -------
    matplotlib.axes.Axes
        Plot axis.
    """
    if x_column not in results.columns:
        raise ValueError(f"Column not found: {x_column}")

    if y_column not in results.columns:
        raise ValueError(f"Column not found: {y_column}")

    plot_data = results.sort_values(x_column)

    fig, ax = plt.subplots(figsize=(7, 5))

    ax.plot(
        plot_data[x_column],
        plot_data[y_column],
        marker="o",
    )

    ax.set_xlabel(x_column)
    ax.set_ylabel(y_column)
    ax.set_title(title)
    ax.grid(True)

    fig.tight_layout()

    if output_file is not None:
        fig.savefig(output_file, dpi=300, bbox_inches="tight")

    return ax
