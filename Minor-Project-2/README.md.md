# Zero Trust Architecture for Enterprise Security

Minor Project 2 — Naviotech Solution Pvt Ltd Cyber Security Internship

## Overview

A Zero Trust security framework ("never trust, always verify") designed
for a simulated enterprise network, combining micro-segmentation,
Multi-Factor Authentication (MFA), and Role-Based Access Control (RBAC).

## Files

- `report.pdf` — full project report: Zero Trust principles,
  authentication models, framework design, simulated environment, and
  security testing results
- `zero_trust_simulator.py` — Python script that simulates access
  requests against the framework's policies

## Running the simulator

```bash
python3 zero_trust_simulator.py
```

Evaluates sample access requests against zone isolation, RBAC, and MFA
rules, printing ALLOW/DENY for each — including the two test scenarios
from the report (a guest device probing the Finance zone, and a stolen
password without MFA).

## Summary of findings

Micro-segmentation blocked lateral movement from an isolated zone, and
MFA stopped access even with a valid password — showing that layered
Zero Trust controls hold even when one layer is bypassed.

## Author

Ayush Singh ([@Silentintro](https://github.com/Silentintro))
