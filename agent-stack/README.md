# Four specialist agents for production ML work

Prepared 2026-10-19 for a staff ML engineer using Codex, Claude Code, OpenCode, Superpowers, Ponytail, Caveman, document skills, and Humanizer.

Use four named specialists alongside the lead agent. Their value is a distinct question, focused evidence, and an independent review context. Keep the main agent responsible for understanding the whole problem and integrating the result. Keep built-in exploration and implementation agents for their existing jobs.

## Picks and upstream sources

| Recommended role | Upstream starting point | Decision and adaptation | When it earns its cost |
|---|---|---|---|
| `staff-code-reviewer` | [Superpowers code reviewer template](https://github.com/obra/superpowers/blob/main/skills/requesting-code-review/code-reviewer.md) | Reuse the review process you already have. Register a named role where useful; preserve task-specific Superpowers review prompts. | Consequential implementation is ready for independent review. Look for real behavior regressions and missing requirements, with file references. |
| `staff-security-reviewer` | [Anthropic code-modernization security-auditor](https://github.com/anthropics/claude-plugins-official/blob/main/plugins/code-modernization/agents/security-auditor.md) | Add. Its concrete attack-path, secret-handling, and finding requirements are a useful starting point. Narrow to the affected system and add relevant ML artifact/data boundaries. | Changes touch identity, tenancy, external input, dependencies, secrets, or sensitive data. |
| `ml-release-reviewer` | [wshobson mlops-engineer](https://github.com/wshobson/agents/blob/0874a27b17a22e2b7c2e2bcd725768e0803cad06/plugins/machine-learning-ops/agents/mlops-engineer.md) | Adapt substantially. The upstream agent builds infrastructure; your recurring need is independent review of existing ML releases. This role name and its evaluation contract are newly authored. | Runtime/library upgrades or changes to model, preprocessing, features, data contracts, or serving. |
| `production-investigator` | [wshobson DevOps troubleshooter](https://github.com/wshobson/agents/blob/0874a27b17a22e2b7c2e2bcd725768e0803cad06/plugins/incident-response/agents/devops-troubleshooter.md) | Adapt into an investigator that returns evidence and discriminating checks. Keep remediation with the lead. | Failed upgrades, production incidents, inference/training failures, latency or cost regressions. |

The included definitions are original, concise adaptations informed by these sources and the production-ML working agreement. They are not verbatim upstream agents, and their performance has not been established by the earlier 50 skill trials. No model is pinned: choose by observed performance and available tools, rather than assigning intelligence by host brand.

## How the model knows they exist

There are two separate pieces: native agent registration exposes each name and description; the lead's routing instructions say when to delegate. A collection of Markdown files in a generic skills directory does not establish a callable specialist agent.

These adapters follow the official documentation inspected on the date above:

| Host | Pack files | Personal destination | Project destination | Discovery |
|---|---|---|---|---|
| [Codex](https://developers.openai.com/codex/subagents/) | `codex/*.toml` | `~/.codex/agents/` | `.codex/agents/` | Standalone TOML with `name`, `description`, and `developer_instructions`. Applicable project/skill instructions or an explicit request can trigger delegation. |
| [Claude Code](https://code.claude.com/docs/en/sub-agents) | `claude/*.md` | `~/.claude/agents/` | `.claude/agents/` | YAML frontmatter defines the name, description, and allowed tools; matching descriptions guide delegation. |
| [OpenCode](https://opencode.ai/docs/agents/) | `opencode/*.md` | `~/.config/opencode/agents/` | `.opencode/agents/` | Filename gives the name; `description` and `mode: subagent` expose the role for delegation. The lead's task permissions must permit it. |

Choose one scope per role and preserve existing definitions. The user's installed versions have not been inspected; older releases may require different configuration. The Codex files target the currently documented standalone-agent format, rather than assuming an older `agents.<name>.config_file` setup.

Merge the short [ROUTING.md](ROUTING.md) policy into the instructions the lead already reads: usually `AGENTS.md` for Codex/OpenCode and `CLAUDE.md` for Claude Code. This gives explicit, scoped delegation guidance without requiring the user to remember each agent name. It does not override host permissions or higher-priority instructions. Restart after introducing new agent directories, then check that the host recognizes the names.

The current Superpowers reviewer source is a prompt template that dispatches a general-purpose subagent. Having that skill installed does not itself prove that a named `staff-code-reviewer` exists. This pack makes the role explicit; it does not patch Superpowers or automatically replace every review step.

## Tool boundaries and handoff

Claude variants allow `Read`, `Glob`, and `Grep`. OpenCode variants allow local reading/search and deny other tool actions. The lead supplies diffs, command results, scanner output, and redacted telemetry. These narrow review roles can inspect underlying code but do not independently run tests or query production.

Codex agents inherit the parent's permissions under the current documentation. The included instruction to avoid modifications is a behavioral restriction, not a separately enforced read-only sandbox. Apply actual access controls through the host, and retain the parent session's appropriate permissions. No files here alter global permissions, credentials, or production access. See [Codex subagent permissions](https://developers.openai.com/codex/subagents/) and [OpenCode permissions](https://opencode.ai/docs/permissions/).

Superpowers remains the workflow owner. Ponytail's preference for the smallest complete change applies to recommendations. Caveman can shorten conversational updates without deleting evidence or material uncertainty. Use normal technical prose for findings that become review comments or reports; Humanizer belongs to final prose editing, not rewriting technical evidence.

## Candidates I would leave out initially

- [VoltAgent security-auditor](https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/04-quality-security/security-auditor.md): broad audit/compliance scope and a presumed context-manager protocol need substantial adaptation. Its sample progress numbers are examples, not measurements. Anthropic's code-focused reviewer is closer to your immediate need.
- [VoltAgent sre-engineer](https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/03-infrastructure/sre-engineer.md): includes fixed MTTR, availability, and automation targets independent of your services. Prefer a scoped investigator using your actual objectives.
- [wshobson architect-review](https://github.com/wshobson/agents/blob/0874a27b17a22e2b7c2e2bcd725768e0803cad06/plugins/comprehensive-review/agents/architect-review.md): retain as a possible later specialist for major boundary changes; the pattern-compliance emphasis is not a useful gate on every maintenance task.
- [Anthropic feature-dev code-reviewer](https://github.com/anthropics/claude-code/blob/main/plugins/feature-dev/agents/code-reviewer.md): a credible alternative if you move away from Superpowers review. I would not add both for the same review; its tool list also needs checking against the installed host.

## What is verified and what remains

Inspected the linked source instructions and current official host documentation. Generated four definitions for each host and parsed all TOML and YAML frontmatter. Checked matching role names and ZIP integrity. Files live in this review pack only; no agents or plugins were installed or activated.

These checks establish valid file syntax, not that your host loads them or that they outperform default agents. A useful first pilot is a representative runtime upgrade: give the lead a fixed diff and evidence, confirm it selects `ml-release-reviewer`, and check whether the specialist finds a real compatibility/evaluation issue without inventing failures or expanding scope. Repeat for a known security defect and an incident with an established cause. Compare against the current workflow before keeping the new definitions permanently.

Role descriptions are exported in [roles.json](roles.json); [build.py](build.py) contains their source and generates the adapters and archive. This is a proposed starting stack, ready for local installation and host-level evaluation.
