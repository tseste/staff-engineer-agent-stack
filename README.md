# Staff engineer agent stack

A compiled research and proposal repository for a staff ML engineer using **Codex, Claude Code, and OpenCode**, primarily to maintain and upgrade production systems, alongside product development, research, and documents.

This repository gathers the complete proposed stack: existing plugins, specialist skills, workflow guidance, a production-ML working agreement, and four specialist agent definitions. It also preserves the original 50-skill screening and its evidence.

**Status: proposal and research archive.** The user's preferred way to invoke, coordinate, and share agents has not been established. Compilation does not mean the stack has been accepted, installed, or validated as a combined system. The agent definitions were prepared before that usage discussion and remain provisional.

## Start here

| Question | Document |
|---|---|
| What is the proposed complete stack? | [Production ML stack](PRODUCTION-ML-STACK.md) |
| How do the existing plugins interact? | [Stack direction and interactions](STACK-DIRECTION.md) |
| Who maintains the parts? | [Provenance and maintainer inventory](PROVENANCE.md) |
| What was established, and what still needs a decision? | [Decision status](DECISIONS.md) |
| Which skills belong in which workflow, and what replaces the dropped ones? | [Workflow report](WORKFLOW-REPORT.md) |
| What happened in the 50 skill trials? | [Evaluation table](REPORT.md), [method](METHOD.md), and [retained index](KEPT.md) |
| What behavior should be shared across hosts? | [Working agreement draft](production-ml-working-agreement.md) |
| Which specialist agents were proposed? | [Four-agent proposal and host setup](agent-stack/README.md) |
| How would a lead agent know when to delegate? | [Proposed routing instructions](agent-stack/ROUTING.md) |

## The proposed layers

| Layer | Components | Current status |
|---|---|---|
| Existing foundation | Caveman, Ponytail, Superpowers, Humanizer, and the user's document skills | User reports using these; exact installed variants, modes, and versions are unverified. Document packages are unspecified. |
| Shared judgment | Production-ML working agreement | Assistant-authored proposal; not evaluated as an installed policy. |
| First-choice specialists | software-architecture-analysis, software-architecture, dependency-upgrade, verification-methodology, site-reliability-engineering, capacity-and-cost-engineering | Selected from individually screened candidates; use selectively. |
| Additional specialist library | 42 retained skills across architecture, product, delivery, operations, security, and documentation | Screening shortlist; **not a recommendation to activate all 42 globally**. |
| Delegated agents | staff-code-reviewer, staff-security-reviewer, ml-release-reviewer, production-investigator | Four original adaptations, with 12 host-specific files. Syntax checked; no actual-host performance trials. |
| Host integration | Codex, Claude Code, OpenCode | Supported mechanisms researched; the user's installations have not been inspected or changed. |

There are **seven identified upstream maintainers**, plus assistant-authored adaptations. Unspecified document packages may add maintainers. See [PROVENANCE.md](PROVENANCE.md) for the exact mapping and source assumptions.

## Evidence and limits

- **50** original skills were each given to a fresh subagent for one prewritten qualitative scenario. The parent evaluated the resulting work product: **42 kept, 8 dropped**.
- The scenarios, work products, scoring judgments, pinned sources, and SHA-256 digests are preserved. These were proposed engineering responses, not execution against production systems.
- One case per skill, the same underlying model, one parent evaluator, and no no-skill baseline limit what the screening can establish. It does not prove causal improvement or safety.
- The workflow synthesis, narrowed production-ML stack, working agreement, and agent adaptations were produced later. **The original trials do not validate those combinations or adaptations.**
- Earlier standalone keep/drop decisions do not establish that internal Superpowers workflow components should be removed. Later tailored recommendations take precedence over earlier generic starting lists.

## Files and data

- `trials/01.json` through `trials/50.json`: the original agent-facing scenarios.
- `results/01.md` through `results/50.md`: the actual saved subagent work products.
- `manifest.json`: source commits, scenarios, and prewritten expectations.
- `judgments.json`, `evaluation.json`, and `staff-engineer-skills.csv`: reviewed decisions and the full table.
- `artifact-hashes.json`: original source/scenario/result digests.
- `workflow-routing.{json,csv}` and `dropped-alternatives.{json,csv}`: routing and replacement mappings.
- `skill-workflow.mmd`: the workflow diagram.
- `agent-stack/{codex,claude,opencode}/`: the proposed native agent definitions.
- `agent-stack/roles.json`: exported role descriptions; `agent-stack/build.py` contains their canonical generation source.
- `judgments-*.json`, `table-fields.json`, and `workflow-overview.md`: supporting assessment/build inputs.

The original manifest and trial JSON retain historical `/workspace/staff-skills/` paths to preserve their recorded hashes. Those paths identify the evaluation environment; they are not installation instructions. The report builders were adjusted to locate files relative to this checkout.

## Validate or regenerate

Requires Python 3.11+ and PyYAML. In an environment with those dependencies available:

```bash
python scripts/validate.py
python build_workflow_report.py
python agent-stack/build.py
```

To regenerate the original skill report including source digests, first fetch the pinned public source snapshots:

```bash
python download_sources.py
python build_report.py
```

The download script requires network access and writes static reference files under ignored `sources/`; it does not install plugins or run their scripts. Generators produce ignored ZIP bundles. No command here runs new agent trials, installs the proposed stack, or publishes a release.

## Attribution

Upstream repositories retain their own authorship and licenses. This repository links to upstream packages instead of vendoring them. Reports, scenario work products, the working agreement, and the four adapted agent definitions were produced with AI assistance. These materials are not official releases of the upstream projects. Source attribution and evidence boundaries are recorded in [PROVENANCE.md](PROVENANCE.md).
