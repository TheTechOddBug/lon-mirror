# OMNIA-RADAR — Status

**Author:** Massimiliano Brighindi  
**Project:** MB-X.01

---

## Current state

```text
OMNIA-RADAR branch: operational offline
Mode: synthetic only
Runtime dependency: none
Regime space: GROWTH_ZONE / BORDERLINE_ZONE / DEAD_ZONE


---

What is already available

docs/RADAR_FORMALIZATION_v0.md

data/radar_cases_v0.json

radar_demo.py

report_generator_radar.py



---

What the current branch can do

The offline demonstrator can already:

load synthetic RADAR cases

compute radar_score

classify cases into GROWTH_ZONE, BORDERLINE_ZONE, or DEAD_ZONE

save structured JSON results

generate a Markdown report


This is sufficient for offline opportunity-detection sanity testing.


---

What is not available yet

The branch does not yet include:

real backend signal ingestion

empirical calibration on runtime traces

integration with OMNIAMIND real traces

integration with OMNIA real runtime outputs


So this branch remains an offline analytical demonstrator.


---

How to run the offline RADAR

1. Run the RADAR demo

python radar_demo.py

2. Generate the Markdown report

python report_generator_radar.py


---

Expected outputs

Running the offline RADAR should produce:

data/radar_results_v0.json

reports/radar_report_v0.md



---

Current meaning of the branch

OMNIA-RADAR v0 is currently a synthetic structural opportunity detector.

It is analytically usable. It is not yet empirically validated on real runtime signals.


---

Minimal conclusion

The OMNIA-RADAR offline branch is runnable and structurally coherent.

Real progress beyond this point requires real structural signals from OMNIA and/or OMNIAMIND.
