# Custom agents and their skills

The lead reads one [judgment guide](JUDGMENT.md) and sees short descriptions of the specialists registered in its host. Each specialist receives that same guide plus its remit, the skills assigned to it, and when to use each skill. The role descriptions and assignments live in [roles.json](roles.json). The [routing guide](ROUTING.md) explains when a specialist's answer earns the extra review.

## Starting assignments

| Specialist | Skills | Decision it helps the lead make | Upstream role reference |
|---|---|---|---|
| `staff-code-reviewer` | `code-review-excellence` | Whether the change preserves downstream behavior and whether the tests cover the risky path. It can fill the existing Superpowers review step. | [Superpowers reviewer](https://github.com/obra/superpowers/blob/main/skills/requesting-code-review/code-reviewer.md) |
| `staff-security-reviewer` | `secure-software-engineering`, `privacy-engineering` | Whether a change to identity, permissions, artifact loading or sensitive data crosses a boundary the application is meant to enforce. | [Anthropic security auditor](https://github.com/anthropics/claude-plugins-official/blob/main/plugins/code-modernization/agents/security-auditor.md) |
| `ml-release-reviewer` | `verification-methodology`, `dependency-upgrade` | Whether the evidence supports promotion, including the critical cohort and compatibility of the recovery path. | [MLOps engineer](https://github.com/wshobson/agents/blob/0874a27b17a22e2b7c2e2bcd725768e0803cad06/plugins/machine-learning-ops/agents/mlops-engineer.md) |
| `production-investigator` | `systematic-debugging`, `site-reliability-engineering` | Which explanation best fits the incident and which observation would discriminate between plausible causes. | [DevOps troubleshooter](https://github.com/wshobson/agents/blob/0874a27b17a22e2b7c2e2bcd725768e0803cad06/plugins/incident-response/agents/devops-troubleshooter.md) |

These are four assistant-authored advisory roles. For each starting skill, the manifest's `screening_id` identifies its [pinned upstream source](../evaluation.json). A skill can belong to multiple roles where each has a concrete use for it. The user can keep a custom skill local to a project.

## Add an agent or change its skills

1. Copy a role entry in [roles.json](roles.json). Choose a unique name and describe the decision it can inform. In `instructions`, state the evidence it should examine, its responsibilities, and what the lead needs back. The calibration test is whether the new role can answer a recurring question better than a role you already have.
2. Give it a `skills` list. Each entry has an exact `id`, a short `use_when`, and either a `screening_id` for a retained skill or a `source` pointing to the custom skill. The `source` field records provenance. Install the actual skill under a supported host location. Use the optional `host_ids` mapping when installed names differ, for example a plugin-qualified Claude skill ID.
3. From the repository root, run `python agent-stack/build.py` then `python scripts/validate.py`. Review the generated files and copy the desired roles to your project's agent directory for that host. Publish or register as many roles as you intend to use there.
4. In a fresh session, ask the host to call one named role with a case where its skill matters. Check the invocation or preload record, its effective tool permissions, and the evidence in its answer. Try an unrelated skill to check any intended restriction. Then try the normal workflow and observe whether the lead uses the role at the point you want.

For example, a custom skill entry in a data-contract reviewer's `skills` list could read as follows. The path is illustrative.

```json
{
  "id": "feature-contract-check",
  "use_when": "Check the default and ordering of features shared by batch training and online inference.",
  "source": "skills/feature-contract-check/SKILL.md"
}
```

The generator currently produces **advisory** agents. Their assignments cover inspection and recommendations. Creating an agent that edits code, runs jobs or operates production calls for defining that authority and its tool permissions explicitly. Review the effective permissions on the target host.

## Bind skills in the chosen host

| Host and output directory | Project destination | How skills are made available |
|---|---|---|
| Codex, `codex/` | `.codex/agents/` | The portable TOML names the role's assigned skills in its instructions. Codex inherits the parent's available skills. For native per-skill disables, export against the installed catalog as shown below. [Codex subagents](https://developers.openai.com/codex/subagents/) |
| Claude Code, `claude/` | `.claude/agents/` | The `skills` frontmatter preloads the assigned installed IDs. The reviewer tool list allows Read, Glob and Grep. Missing or disabled skills can be skipped, so verify the actual preload. [Claude Code subagents](https://code.claude.com/docs/en/sub-agents) |
| OpenCode V1, `opencode/` | `.opencode/agents/` | The legacy `permission.skill` map denies skill calls by default and allows the assigned IDs. Use the format matching your installed version. |
| OpenCode V2, `opencode-v2/` | `.opencode/agents/` | Ordered `permissions` rules allow the `skill` action for the assigned IDs. Confirm IDs from the host's catalog. [OpenCode agents](https://opencode.ai/docs/agents/) · [Skill permissions](https://opencode.ai/docs/skills/) |

Choose one OpenCode format per installation. For any host, register the supporting skills and use their effective IDs. A role manifest does not install third-party code. Restricting skill invocation is separate from restricting access to files, shell tools or services. For example, a reviewer with a file reader can still inspect files within its permitted workspace.

### Scope a Codex export to local skills

Create a local inventory JSON object mapping **every installed skill ID in scope** to the absolute path of its `SKILL.md` on that machine. Include all skills assigned to the roles in the manifest. From the repository root run the following command, replacing the example paths with your own. Choose a new or empty output directory outside `agent-stack/`.

```bash
python agent-stack/build.py --codex-inventory /path/to/inventory.json --output-dir /path/to/codex-export
```

The exported TOML disables the inventoried unassigned skills for each role. Copy the local export to the target host's agent directory. Regenerate when the installed skill catalog changes. Omitted skills can remain visible through parent inheritance, and an assigned skill still needs to be enabled in the host. Keep the machine-specific inventory and export local.

## Verification and adoption

The builder checks that the generated files match the shared policy and per-host assignments. The [judgment checks](judgment-checks.md) record two fresh policy-only scenarios. For an adoption decision, replay a real historical upgrade on the same host and model with the existing workflow and then with one specialist added. Withhold the outcome until scoring. Compare consequential findings, false alarms, and time spent on review.

## Other agent references considered

The [VoltAgent security auditor](https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/04-quality-security/security-auditor.md) assumes a wider audit scope. The [VoltAgent SRE engineer](https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/03-infrastructure/sre-engineer.md) supplies fixed operational targets where the project should supply its actual objectives. The [wshobson architecture reviewer](https://github.com/wshobson/agents/blob/0874a27b17a22e2b7c2e2bcd725768e0803cad06/plugins/comprehensive-review/agents/architect-review.md) is a candidate for major boundary changes. The [Anthropic code reviewer](https://github.com/anthropics/claude-code/blob/main/plugins/feature-dev/agents/code-reviewer.md) offers an alternative to the Superpowers review step.
