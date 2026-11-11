# Cybersecurity Risk Assessment Framework for SMEs

Minor Project 1 — Naviotech Solution Pvt Ltd Cyber Security Internship

## Overview

A practical risk assessment model for small and medium enterprises (SMEs),
built on the NIST Cybersecurity Framework. Risks are scored using a
Likelihood × Impact metric and ranked by priority, with mitigation
strategies proposed for each.

## Files

- `report.pdf` — full project report: research, risk model, scoring
  table, mitigation strategies, and a validation case study
- `risk_assessment_tool.py` — Python script that automatically scores
  and ranks the risks from the report

## Running the tool

```bash
python3 risk_assessment_tool.py
```

Outputs a ranked table of risks with their Likelihood, Impact, Risk
Score, and Priority band (Critical/High, Medium, Low).

## Summary of findings

Phishing and weak password hygiene scored highest among common SME
risks, while also being among the cheapest to mitigate — MFA and basic
staff training offer the best risk reduction per rupee spent.

## Author

Ayush Singh ([@Silentintro](https://github.com/Silentintro))
