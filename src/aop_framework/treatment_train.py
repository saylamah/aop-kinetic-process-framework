from __future__ import annotations

from dataclasses import dataclass


@dataclass
class AOPScreeningResult:
    """
    Screening-level interpretation of AOP readiness for a wastewater matrix.
    """

    classification: str
    main_limitation: str
    recommendation: str
    notes: list[str]


def classify_scavenging_capacity(k_scav_s: float) -> str:
    """
    Classify total hydroxyl-radical scavenging capacity.

    The thresholds are heuristic and intended for screening-level interpretation,
    not final plant design.

    Parameters
    ----------
    k_scav_s:
        Total hydroxyl-radical scavenging capacity in s^-1.

    Returns
    -------
    str
        Scavenging class.
    """
    if k_scav_s < 0:
        raise ValueError("Scavenging capacity cannot be negative.")

    if k_scav_s < 1.0e4:
        return "low"

    if k_scav_s < 1.0e5:
        return "moderate"

    if k_scav_s < 5.0e5:
        return "high"

    return "very_high"


def screen_aop_readiness(
    k_scav_s: float,
    doc_mg_C_L: float | None = None,
    turbidity_NTU: float | None = None,
    nitrite_mg_L: float | None = None,
    target: str = "micropollutants",
) -> AOPScreeningResult:
    """
    Provide screening-level AOP readiness guidance.

    This function is intended for early engineering interpretation. It does not
    replace experimental validation, pilot testing, detailed reactor modeling,
    or regulatory design.

    Parameters
    ----------
    k_scav_s:
        Total hydroxyl-radical scavenging capacity in s^-1.
    doc_mg_C_L:
        Dissolved organic carbon concentration in mg C/L, if available.
    turbidity_NTU:
        Turbidity in NTU, if available.
    nitrite_mg_L:
        Nitrite concentration in mg/L, if available.
    target:
        Target treatment objective, for example "micropollutants" or "COD polishing".

    Returns
    -------
    AOPScreeningResult
        Screening classification, main limitation, recommendation, and notes.
    """
    scavenging_class = classify_scavenging_capacity(k_scav_s)

    notes = [
        f"Target objective: {target}",
        f"Scavenging capacity class: {scavenging_class}",
    ]

    limitations = []

    if scavenging_class in {"high", "very_high"}:
        limitations.append("matrix radical scavenging")

    if doc_mg_C_L is not None:
        if doc_mg_C_L < 0:
            raise ValueError("DOC cannot be negative.")

        notes.append(f"DOC: {doc_mg_C_L:.2f} mg C/L")

        if doc_mg_C_L > 5.0:
            limitations.append("high DOC")
        elif doc_mg_C_L > 2.0:
            limitations.append("moderate DOC")

    if turbidity_NTU is not None:
        if turbidity_NTU < 0:
            raise ValueError("Turbidity cannot be negative.")

        notes.append(f"Turbidity: {turbidity_NTU:.2f} NTU")

        if turbidity_NTU > 10.0:
            limitations.append("high turbidity or optical attenuation")
        elif turbidity_NTU > 5.0:
            limitations.append("moderate turbidity")

    if nitrite_mg_L is not None:
        if nitrite_mg_L < 0:
            raise ValueError("Nitrite cannot be negative.")

        notes.append(f"Nitrite: {nitrite_mg_L:.2f} mg/L")

        if nitrite_mg_L > 1.0:
            limitations.append("nitrite scavenging")
        elif nitrite_mg_L > 0.2:
            limitations.append("moderate nitrite scavenging")

    if not limitations:
        classification = "favorable"
        main_limitation = "none dominant at screening level"
        recommendation = (
            "AOP may be suitable as a polishing step. Proceed with target-specific "
            "kinetic testing and oxidant or energy-dose optimization."
        )

    elif scavenging_class == "moderate":
        classification = "moderate"
        main_limitation = ", ".join(limitations)
        recommendation = (
            "AOP may be feasible, but pretreatment and matrix control should be "
            "considered before increasing oxidant or energy input."
        )

    elif scavenging_class == "high":
        classification = "challenging"
        main_limitation = ", ".join(limitations)
        recommendation = (
            "AOP performance is likely matrix-limited. Improve upstream biological "
            "treatment, solids removal, DOC reduction, or adsorption before AOP."
        )

    else:
        classification = "severe"
        main_limitation = ", ".join(limitations)
        recommendation = (
            "Direct AOP application is likely inefficient without substantial "
            "pretreatment or process integration. Consider adsorption, membranes, "
            "biological polishing, or hybrid treatment before oxidation."
        )

    return AOPScreeningResult(
        classification=classification,
        main_limitation=main_limitation,
        recommendation=recommendation,
        notes=notes,
    )
