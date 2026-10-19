**Recommended shared stack for a staff ML engineer**

Primary work: maintaining and upgrading production systems, with product development, research, and documents also in scope. Hosts: Codex, Claude Code, and OpenCode.

The recommendation is one shared behavioral contract, the user's existing workflow/style foundation, and a small specialist library. Host-specific adapters should handle discovery, tools and activation. Model choice, repository context and access to real evidence are part of the stack; skills alone cannot supply them.

**Foundation**

| Component | Recommendation | Responsibility and limit |
|---|---|---|
| Superpowers | Keep as the development workflow owner | Planning, debugging, implementation, review and verification. Preserve its internal handoffs; do not blindly remove brainstorming or planning based on the earlier standalone shortlist. Use an explicit small-task path consistent with user/repository instructions. |
| Ponytail | Keep; full mode is the provisional default | Smallest complete implementation, reuse of existing conventions, caller coverage and preservation of safety checks. Use stronger challenge deliberately for design decisions. Short diff is not evidence of low production risk. |
| Caveman | Keep the ordinary voice component for chat | Brevity must preserve decision rationale, uncertainty and material limits. Its own skill excludes persisted documents. Confirm whether the installed variant also enables runtime, model-routing or additional work-pattern features before assigning those responsibilities. |
| Humanizer | Keep for authored prose in embedded/file mode | Polish drafts after facts and document structure are established. Preserve citations, numbers, technical meaning and uncertainty. Keep prose edits separate from source-code or structured-data changes. |
| Existing document skills | Keep pending format-specific review | Own DOCX/PDF/slides/spreadsheets or other formats actually used, including rendering and validation. Exact packages have not been supplied; no claim is made that their coverage is complete. |
| Production ML working agreement | Proposed shared policy | Preserve end-to-end ML behavior through change, exercise staff-level judgment, and make bounded claims from evidence. This is a new draft, not a tested marketplace skill. |

**Six first-choice specialist skills**

Keep these available on demand or enabled in relevant projects. They do not all belong in every session. The prior trials support individual screening only; their combined behavior with the user's plugins is untested.

| Skill | Activate for | Why it earns a place |
|---|---|---|
| [software-architecture-analysis](https://github.com/magnus919/agent-skills/blob/06ca706ecaa80f6afb31ae28eb160d39372b7267/software-architecture-analysis/SKILL.md) | Unfamiliar or misleadingly documented production systems | Establish actual dependencies, data ownership, runtime paths and coupling before touching a mature system. |
| [software-architecture](https://github.com/magnus919/agent-skills/blob/06ca706ecaa80f6afb31ae28eb160d39372b7267/software-architecture/SKILL.md) | Consequential boundaries, replacements, platform changes or rewrites | Make an explicit recommendation using operational and organizational tradeoffs; preserve the option of doing less. |
| [dependency-upgrade](https://github.com/wshobson/agents/blob/0874a27b17a22e2b7c2e2bcd725768e0803cad06/plugins/framework-migration/skills/dependency-upgrade/SKILL.md) | Runtime/framework/library upgrades or security remediation | Analyze the actual exposure and compatibility surface, stage the change, and retain a credible recovery path. |
| [verification-methodology](https://github.com/magnus919/agent-skills/blob/06ca706ecaa80f6afb31ae28eb160d39372b7267/verification-methodology/SKILL.md) | Changes where passing tests or equal counts do not prove semantic equivalence | Use independent invariants and candidate-bound evidence. This complements Superpowers' completion verification rather than creating a second completion process. |
| [site-reliability-engineering](https://github.com/magnus919/agent-skills/blob/06ca706ecaa80f6afb31ae28eb160d39372b7267/site-reliability-engineering/SKILL.md) | Release risk, incidents, reliability debt or noisy observability | Connect decisions to user outcomes, error budgets, operational ownership and recovery. |
| [capacity-and-cost-engineering](https://github.com/magnus919/agent-skills/blob/06ca706ecaa80f6afb31ae28eb160d39372b7267/capacity-and-cost-engineering/SKILL.md) | Serving/training capacity, failure tolerance and cost changes | Check degraded-state capacity, bottlenecks, workload mix and unit economics. Per-engine GPU/runtime expertise remains project-specific. |

**Additional specialists only when the change requires them**

- Data/schema migration: database-migration and, for destructive failure modes, resilience-and-recovery.
- API, event, feature or client contract: api-design-and-evolution.
- Access boundaries or personal data: secure-software-engineering, auth-implementation-patterns and privacy-engineering as applicable.
- Release mechanics: deployment-pipeline-design; incident response: incident-runbook-templates and on-call-handoff-patterns; learning: postmortem-writing.
- A newly proposed product or major scope choice: product-discovery and product-shaping.
- Cross-team delivery: technical-program-management. Recurring ownership bottlenecks: org-design.
- Specific ML/serving engines and infrastructure: choose against the repository's actual PyTorch/TensorFlow/scikit-learn/XGBoost/Spark/Triton/vLLM/Kubernetes/cloud stack. Those technologies are examples, not known facts about the user's environment.
- LLM/RAG/agent evaluation belongs only in systems that use those techniques. General ML evaluation, feature semantics and leakage remain relevant across model families.

**ML-specific judgment**

For production changes, determine the affected parts of the release unit: code, dependencies/runtime, model artifact, preprocessing, feature definitions, configuration, data contracts and state. Version or identify them so comparisons and recovery refer to a real candidate.

Required evidence depends on the change. Possible checks include prediction and feature parity, important slice regressions, temporal correctness, calibration/threshold behavior, failure handling, throughput and tail latency, memory, hardware/runtime compatibility and cost per useful unit. Specify tolerances and provenance; avoid demanding bitwise equality where numerical variation is expected, or accepting numerical variation without examining consequences.

Offline model metrics, data drift, system health and business outcomes are separate signals. A drift alert does not establish a quality regression. A quality improvement does not automatically justify a harmful critical-slice regression. Delayed labels and incomplete observation should remain explicit.

Prefer extending the project's real evaluation and data-contract machinery over installing a generic framework. The inspected ml-engineering package contains useful evaluation/lineage references but substantial LLM material and a role split that assigns experimental design and business metrics away. It is an optional reference, not the default staff-engineer policy. The inspected data-quality-frameworks package is not selected as executable production guidance; library snippets require version-specific validation.

**Three-host operation**

1. Maintain one canonical working agreement and shared project decisions/task evidence. Use thin, supported adapters for each host; verify that they load the intended policy.
2. Install each chosen plugin through one supported mechanism per host. Check for duplicate bootstrap injection, global/project duplication, mode state and behavior after compaction.
3. Keep versions and overrides recorded. OpenCode version and model choice can change plugin/tool behavior; do not assume installation parity implies behavioral parity.
4. Select a task lead from context, tools, model performance and availability. Use a second agent for consequential review when useful. Concurrent writers need isolated branches/workspaces and integration ownership.
5. Treat completion claims as evidence-bound. A handoff to another host carries the current revision, decision, relevant evidence, outstanding issue and next action.

**What is established and what remains**

The earlier evaluation screened 50 individual skills. Source review now covers the likely existing plugin repositories and their integration instructions. No changes have been made to the user's agent installations. The six-specialist selection and proposed working agreement are tailored recommendations, not a validated combined configuration.

Before broad adoption, compare the current and proposed configurations on a routine upgrade, an ambiguous production regression, a critical ML behavior change and an evidence-based document. Exercise each actual host/model configuration; same-model subagents cannot establish performance inside Claude Code or OpenCode. Check correctness, consequences caught, unnecessary interaction, factual fidelity, recovery reasoning and cost.

**Sources and companion material**

- [Working agreement draft](production-ml-working-agreement.md)
- [Existing 50-skill evidence](REPORT.md)
- [Caveman skill](https://github.com/JuliusBrussee/caveman/blob/main/skills/caveman/SKILL.md) and [broader runtime scope](https://github.com/JuliusBrussee/caveman/blob/main/README.md)
- [Ponytail](https://github.com/DietrichGebert/ponytail/blob/main/skills/ponytail/SKILL.md) and [host integration](https://github.com/DietrichGebert/ponytail/blob/main/docs/agent-portability.md)
- [Superpowers](https://github.com/obra/superpowers) and [OpenCode integration](https://github.com/obra/superpowers/blob/main/docs/README.opencode.md)
- [Humanizer](https://github.com/blader/humanizer/blob/main/SKILL.md)
- [ML engineering reference inspected](https://github.com/magnus919/agent-skills/blob/06ca706ecaa80f6afb31ae28eb160d39372b7267/ml-engineering/SKILL.md)
