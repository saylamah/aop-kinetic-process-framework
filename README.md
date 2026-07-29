# AOP Kinetic Process Framework

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20841383.svg)](https://doi.org/10.5281/zenodo.20841383)
[![Python tests](https://github.com/saylamah/aop-kinetic-process-framework/actions/workflows/python-tests.yml/badge.svg)](https://github.com/saylamah/aop-kinetic-process-framework/actions/workflows/python-tests.yml)

A Python framework for matrix-aware kinetic and process-level assessment of advanced oxidation processes in wastewater treatment.

---

## Purpose

Advanced oxidation processes are often compared using pollutant-removal percentages or apparent first-order rate constants.

These indicators can be misleading when wastewater-matrix constituents consume a substantial fraction of the generated reactive species.

This repository provides transparent calculation tools for examining how:

- hydroxyl-radical generation;
- dissolved organic matter;
- bicarbonate and carbonate;
- inorganic scavengers;
- pollutant concentration;
- radical competition;
- reactor conditions;
- oxidant utilization;
- treatment time;
- simplified energy indicators

interact to determine apparent AOP performance.

The objective is not to identify one universally superior AOP. It is to improve engineering interpretation, comparison, screening, and validation planning for specific water matrices and treatment objectives.

---

## Practical Engineering Questions

The framework is intended to support questions such as:

- Which matrix constituents dominate hydroxyl-radical consumption?
- What fraction of generated radicals is used toward the target pollutant?
- Why can two waters show different degradation rates under similar operating conditions?
- How does dissolved organic carbon affect apparent treatment performance?
- How do alkalinity and pH influence bicarbonate and carbonate scavenging?
- What treatment time follows from an assumed apparent first-order rate constant?
- Is poor performance associated primarily with radical generation or non-productive scavenging?
- Which measurements are required before comparing AOP alternatives?
- When might pretreatment or a treatment train be preferable to increasing oxidant or energy input?
- Which assumptions must be validated before pilot- or plant-scale use?

---

## Scientific Concept

The initial framework uses a simplified competition-kinetics and apparent steady-state representation.

The total hydroxyl-radical scavenging capacity is expressed as:

```text
k_scav = sum(kOH_i * C_i)
