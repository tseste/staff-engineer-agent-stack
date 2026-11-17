# Applying engineering judgment to production ML

Use this alongside the [shared judgment guide](agent-stack/JUDGMENT.md). Start with the service's own evidence. The questions below apply to the parts of the release that could change.

**Identify the behavior at stake.** Trace one affected prediction, training example or batch record from input to consumer. A runtime upgrade can change feature ordering, missing-value handling or numerical behavior while the model weights stay the same. Specify which behavior the team promises and who experiences a regression.

**Identify a reproducible comparison.** Record the baseline and candidate revisions, model artifacts, preprocessing, data or feature versions and configuration that matter to the comparison. Use existing evaluation code and the service's acceptance criteria. Check the sensitive cohort or decision threshold when aggregate results could hide user harm. Allow tolerances justified by the product and numerical runtime.

**Read evidence at the level it supports.** Passing unit tests establishes the behavior those tests exercise. A changed input distribution calls for investigation. Claims about predictive quality need relevant outcomes or evaluation data. Claims about online impact need observation over the relevant window, including label delay. Name an early signal and who will check mature outcomes when the distinction matters to release.

**Make the release decision operational.** Verify that the recovery unit still works with current features, schemas and persisted state. Specify the smallest safe exposure, the metric or condition that would stop rollout, and who can act on it. For resource-sensitive changes, compare throughput, tail latency and cost per useful unit at a representative workload. Work within the team's existing release authority.

**Keep enough service context to use on the next change.** In the project's existing docs, record the evaluation entry point, authoritative baseline, critical slices and tolerances, release and rollback manifests, and responsible owner as each becomes relevant. A real path, command or dashboard plus its interpretation is enough. Surface undefined criteria when the choice would change promotion.

The lead and specialist can use the same evidence and still disagree. Resolve a disagreement by comparing their assumptions, population, revisions and acceptance criterion. Record what would change the decision and the person who owns any remaining tradeoff.
