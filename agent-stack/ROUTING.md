# Specialist delegation instructions

Proposed text to merge into the lead agent's existing repository instructions after installing the corresponding definitions. These names must refer to registered agents; this document alone does not register them.

Use the following specialist subagents when their scope materially matches the task. Spawn the matching registered agent through the host's delegation tool, subject to its applicable rules. Do not invoke every specialist for every change.

- `staff-code-reviewer`: independent review of completed, nontrivial code changes before integration. If Superpowers already schedules a review, use this role for that compatible review step and preserve the workflow's required checks. Do not add a second identical review.
- `staff-security-reviewer`: changes involving authorization, tenant boundaries, external input, artifact loading, secrets, dependencies with a security impact, or sensitive data.
- `ml-release-reviewer`: changes affecting model behavior, data or feature contracts, preprocessing, training, numerical libraries, or serving-runtime compatibility.
- `production-investigator`: unclear production failures, failed upgrades, performance regressions, or unexplained resource and cost changes.

Give each specialist the task's purpose, exact question, applicable constraints, relevant files, and available evidence. For reviews, supply a diff or patch and identify the base/head or working-tree snapshot. For incidents, supply the time window, impact, relevant configuration, and available redacted telemetry. These agents inspect local evidence; the lead supplies command, scan, and live-system results when needed.

Keep implementation and integration ownership with the lead. Act on substantiated findings, resolve disagreements using evidence, and carry material uncertainty into the final answer. Specialists advise; they do not independently change production or grant release approval. Avoid duplicate review of unchanged work and recursive delegation.

If a specialist is unavailable, report that fact and perform the relevant checks directly where possible. Never claim to have delegated merely because its instructions were read.
