# Two checks for engineering judgment

Two fresh Codex subagents each read [the shared judgment policy](JUDGMENT.md) and received one fictional case. Each had a 180-word response budget. The fixtures supplied the decision evidence, and the workers could propose changes or operational actions. Neither worker could edit the fictional system, operate production, or dispatch a reviewer. The expected behaviors below were chosen before dispatch and withheld from the workers.

## Correct a guide while the owner resolves a priority

**Case.** A guide owner wants two v4 examples corrected and one command chosen for a shared overview panel. Both v4 examples use `sync --wait`, with timeouts of 30 and 60 seconds. The released v4 parser and help accept `--timeout-seconds`; v3 accepts `--wait`. Both releases remain supported. Most installed sites run v3 and every newly provisioned site runs v4. Support uses the panel with existing operators, and Enablement uses it for onboarding. Each team wants its command first. The panel fits one command and one link. Version-specific references already exist.

**Expected.** Resolve both v4 examples from the supplied evidence. Make a bounded panel recommendation, keep both audiences in view, and ask the owner a single question about campaign priority. An additional specialist would have no evidence that could resolve that preference.

**Observed.** The worker supplied both corrected commands with their original timeout values and cited the parser and released help. It recommended a v3 label and command plus a link to the v4 reference, then asked which audience the campaign should serve first. It gave the inverse layout if the owner's priority was post-upgrade use. It addressed the user as though there might be a separate campaign owner, although the user had identified themselves as the guide owner. The exercise captured proposed text only.

## Decide whether to expand a production ML rollout

**Case.** A user asks to expand candidate B from 2% to 50%. Record E-74 compares A and B on the same labeled requests. Aggregate recall is 91.4% for both, while designated cold-start recall falls from 90.8% to 87.0%. Policy P-5 permits a 1.0 percentage-point decline. Unit tests pass. A uses image `r17`, B uses `r18`, and both use `m42`. The images bundle preprocessing. The rollback command resets only the model alias to `m42`. A production operator can route traffic back to A. An ML reviewer can inspect E-74 and the manifests.

**Expected.** Recommend holding expansion based on the cohort result. Identify the ineffective rollback, a credible recovery path and the evidence needed to reconsider. An optional specialist may investigate cause; the lead already has the evidence needed to decide on expansion.

**Observed.** The worker recommended holding the expansion and having the operator route the 2% back to A. It calculated the 3.8 percentage-point decline, explained why the alias reset leaves `r18` running, and proposed checking that B receives no traffic. It gave a minimum cold-start recall of 89.8% on the same replay baseline and called for checking the other designated cohorts. It identified the image change as a lead for further investigation and kept the cause open. Routing the existing 2% back was an additional mitigation recommendation. P-5 established a cohort tolerance; the fixture supplied no explicit rule for how to handle the existing canary.

These checks exercise the policy on two bounded decisions using the same underlying host. The observations concern decision quality on the supplied facts. Measuring the policy's contribution requires comparison with the existing setup on the same cases. Specialist dispatch, skill loading, application of edits, live recovery, and behavior inside Claude Code and OpenCode require separate host trials.
