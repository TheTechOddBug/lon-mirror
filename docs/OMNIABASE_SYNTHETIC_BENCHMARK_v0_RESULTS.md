# OMNIABASE Synthetic Benchmark v0 — First Run Results

## Status

This document records the first executed run of the OMNIABASE synthetic benchmark v0.

This is not validation.
This is not external evidence.
This is the first real run.

The correct state is:

```text
partially successful, structurally limited


---

Run configuration

lens: OmniabaseLens

bases: 2..16

collapse threshold: 0.20

sample size per class: 30

seed: 42


Tested classes:

1. random


2. repeated_pattern


3. powers_of_two


4. arithmetic_construction


5. prime_subset


6. logistic_mapped




---

Summary results

random

cross_base_stability mean: 0.751826

representation_drift mean: 0.248174

base_sensitivity mean: 1.0

collapse_count mean: 8.1


repeated_pattern

cross_base_stability mean: 0.735245

representation_drift mean: 0.264755

base_sensitivity mean: 0.981638

collapse_count mean: 8.9


powers_of_two

cross_base_stability mean: 0.609347

representation_drift mean: 0.390653

base_sensitivity mean: 1.0

collapse_count mean: 12.7


arithmetic_construction

cross_base_stability mean: 0.754464

representation_drift mean: 0.245536

base_sensitivity mean: 0.995205

collapse_count mean: 7.966667


prime_subset

cross_base_stability mean: 0.756041

representation_drift mean: 0.243959

base_sensitivity mean: 1.0

collapse_count mean: 8.233333


logistic_mapped

cross_base_stability mean: 0.756114

representation_drift mean: 0.243886

base_sensitivity mean: 1.0

collapse_count mean: 8.0



---

What worked

1. the lens is not emitting uniform noise

At least one class separates clearly.

powers_of_two is strongly distinct from the rest of the benchmark set.

Compared to the cluster formed by random, arithmetic_construction, prime_subset, and logistic_mapped, the powers_of_two class shows:

much lower cross_base_stability

much higher representation_drift

much higher collapse_count


This is a real result.

It means the current lens is capable of detecting some class-specific cross-base structural behavior.

That is enough to say the prototype is not trivial.


---

2. repeated-pattern inputs show a weak but coherent fragility signal

Compared to random, the repeated_pattern class shows:

lower cross_base_stability

higher representation_drift

higher collapse_count


This is directionally consistent with the intended purpose of the lens: detecting cases where apparent regularity may depend on privileged encoding.

However, the effect is still modest. This is not yet a strong separation result.


---

What failed or degraded

1. base_sensitivity is effectively saturated

This is the clearest internal defect in the current run.

Observed behavior:

base_sensitivity is equal or extremely close to 1.0 for almost every class

this prevents useful discrimination


Therefore:

base_sensitivity is currently not an informative metric

In this version, it should not be treated as evidential.

This metric needs redesign.


---

2. most non-power classes remain too close

The following classes are still clustered too tightly:

random

arithmetic_construction

prime_subset

logistic_mapped


This means the current feature family is still too weak to separate several controlled regimes.

That does not invalidate the lens. It limits its current resolution.


---

Interpretation

The first run supports a narrow claim:

> The current OMNIABASE lens prototype can distinguish at least some controlled integer families through cross-base diagnostics.



That claim is justified.

The first run does not support stronger claims such as:

universal structural discrimination

deep hidden-law extraction

causal interpretation

external predictive value

superiority over other OMNIA layers


Those claims remain unjustified.


---

Structural diagnosis of v0

The run suggests three things at once:

A. the lens has signal

Because powers_of_two separates clearly.

B. the lens has limited resolution

Because several other classes remain clustered.

C. one metric is badly behaved

Because base_sensitivity is saturated and nearly useless.

This is the real outcome.


---

Immediate consequences

The next step should not be public communication.

The next step should be feature and metric repair.

Priority order:

1. redesign base_sensitivity

Current formula is too close to a hard saturation regime.

It should be replaced by a more discriminative statistic.

Possible directions:

normalized outlier ratio with clipping removed

percentile gap instead of max-vs-mean

coefficient of variation over per-base distances

entropy-style spread over base contributions


2. strengthen the feature family

Current profile is too shallow.

Candidate additions:

digit entropy

compressibility proxy

transition irregularity

local motif counts

palindrome / symmetry proxy

multi-scale run profile


3. rerun the synthetic benchmark after the metric upgrade

Only then can we test whether the lens gains meaningful class resolution.


---

Correct project state after first run

implemented
executed
minimally testable
not validated
metric revision required

That is the true state.


---

Minimal conclusion

The first run is useful because it produced both:

one real positive separation

one real internal failure


That is good.

A system that shows signal and exposes its own weakness is scientifically more useful than a system that only looks clean on paper.

