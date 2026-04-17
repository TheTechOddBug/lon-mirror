# OMNIABASE Synthetic Benchmark v0 — Results

## Status

This document records the first executed synthetic benchmark results for the OMNIABASE lens after the `base_sensitivity` correction.

This is not external validation.
This is not proof of superiority.
This is the first internally coherent benchmark result with non-saturated sensitivity behavior.

Correct state:

```text
implemented
executed
structurally improved
minimally discriminative
not externally validated


---

Benchmark configuration

lens: OmniabaseLens

file: omnia/lenses/base_lens.py

benchmark script: examples/omnia_base_lens_synthetic_benchmark.py

tested bases: 2..16

collapse threshold: 0.20


Tested classes:

1. random


2. repeated_pattern


3. powers_of_two


4. arithmetic_construction


5. logistic_mapped




---

Summary results

Dataset Class	Stability (mean)	Drift (mean)	Sensitivity (mean)	Collapse (mean)

Random	0.8142	0.1857	0.2140	9.4
Repeated Pattern	0.7621	0.2378	0.3412	12.1
Powers of Two	0.6912	0.3087	0.4851	14.8
Arithmetic Construction	0.8255	0.1744	0.1982	8.2
Logistic Mapped	0.8091	0.1908	0.2215	9.8



---

Primary result

The correction of base_sensitivity removed the previous saturation defect.

Old behavior:

sensitivity was collapsing near 1.0

metric was nearly useless for discrimination


Current behavior:

sensitivity now distributes across classes

class-level differences are visible

the metric has become structurally informative


This is a real improvement.


---

Main observations

1. powers_of_two is the strongest stress-test class

This class remains the most unstable across the tested base family.

Observed behavior:

lowest mean stability: 0.6912

highest mean drift: 0.3087

highest mean sensitivity: 0.4851

highest mean collapse count: 14.8


Interpretation:

powers_of_two carries a representation profile that is strongly privileged in binary-related regimes and deforms more sharply under many non-aligned bases.

This is not a philosophical claim. It is exactly what the lens should expose: cross-base dependence of apparent structural simplicity.


---

2. repeated_pattern is measurably more fragile than random

Comparison:

repeated pattern stability: 0.7621

random stability: 0.8142

repeated pattern drift: 0.2378

random drift: 0.1857

repeated pattern sensitivity: 0.3412

random sensitivity: 0.2140

repeated pattern collapse: 12.1

random collapse: 9.4


Interpretation:

decimal-looking repetition behaves as a representation-sensitive regularity rather than a cross-base persistent one.

This is an important result.

It means the lens is not merely detecting generic disorder. It is distinguishing between:

disorder distributed across representations and

apparent order that degrades under re-encoding


That is a useful structural distinction.


---

3. arithmetic_construction is the most stable class in this run

Observed behavior:

highest mean stability: 0.8255

lowest mean drift: 0.1744

lowest mean sensitivity: 0.1982

lowest mean collapse count: 8.2


Interpretation:

the current feature family reads simple additive construction as relatively uniform across the tested bases.

This does not prove deep mathematical invariance. It only shows lower cross-base deformation under the current profile.

Still, it is a good sign: the lens is not collapsing all deterministic classes into the same bucket.


---

4. logistic_mapped remains near the random regime

Observed behavior:

stability: 0.8091

drift: 0.1908

sensitivity: 0.2215

collapse: 9.8


Interpretation:

under the current shallow feature family, this synthetic irregular deterministic generator is not sharply separated from random.

This is acceptable.

It means either:

the current features are not deep enough to isolate that class strongly or

the class is structurally closer to distributed irregularity than to representation-bound fragility


At this stage, no stronger claim is justified.


---

What improved after the metric correction

The benchmark is now materially better in three ways.

A. sensitivity is usable

The metric now produces meaningful class differences:

arithmetic: 0.1982

random: 0.2140

logistic: 0.2215

repeated: 0.3412

powers: 0.4851


This ranking is coherent.


---

B. the benchmark now shows class signatures instead of metric collapse

Previously, one metric was nearly dead. Now the output profile is class-sensitive.

That means the benchmark has crossed the threshold from:

implemented but partially broken

to:

implemented and minimally discriminative


---

C. the lens is beginning to separate intrinsic structure from representational artifact

The strongest contrast in this run is:

repeated decimal pattern vs

arithmetic construction


The first is more fragile and more sensitive. The second is more stable and less sensitive.

This is exactly the kind of bounded structural distinction the lens was supposed to test.


---

What is justified now

The strongest justified claim is:

> The current OMNIABASE lens prototype can distinguish some controlled integer families through cross-base structural diagnostics, and the corrected sensitivity metric now provides usable discrimination across classes.



That claim is supported by the benchmark.


---

What is still not justified

The following claims remain unjustified:

universal structural truth detector

proof of hidden mathematical laws

causal detector

financial predictive advantage

superiority over all alternative methods

complete readiness for real-world LLM deployment


Those would still be false or premature.


---

Structural diagnosis

The current state is:

Strengths

deterministic

auditable

bounded

non-semantic

class-sensitive

no longer sensitivity-saturated


Remaining limits

shallow feature family

synthetic benchmark only

no inferential statistics

no comparison to alternative diagnostics

no direct OMNIA pipeline integration result yet


This is a prototype with signal, not a finished proof.


---

Next correct step

The next technically correct move is:

integrate the lens into one OMNIA diagnostic path

Best candidate:

Silent Failure Gate

Reason:

already post-hoc

already measurement-oriented

already aligned with OMNIA architecture

easiest place to test whether cross-base fragility adds useful signal beyond existing diagnostics


Only after that does the lens start becoming operational rather than merely coherent.


---

Minimal conclusion

This benchmark run matters for one precise reason:

the OMNIABASE lens is no longer only conceptually well-formed. It is now also empirically class-sensitive inside a controlled synthetic setting.

That is enough to continue.

Not enough to celebrate. Enough to build on.

