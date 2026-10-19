**Direction for the user's complete skill stack**

The user's goal is a coherent agent that shows staff-engineer judgment, initiative, engineering restraint, reliable execution, and useful communication. Their reported starting stack is Caveman, Ponytail, Superpowers, document skills, and Humanizer.

The prior 50-skill evaluation is a source of candidate capabilities. It does not establish the marginal value of adding 42 skills to this existing stack. Its keep/drop results are not instructions to remove internal parts of a workflow plugin.

**Working source assumptions, awaiting confirmation**

- Caveman: JuliusBrussee/caveman.
- Ponytail: DietrichGebert/ponytail.
- Superpowers: obra/superpowers.
- Humanizer: blader/humanizer.
- Confirmed hosts: Codex, Claude Code, and OpenCode. Primary work: maintaining and upgrading production systems as a staff ML engineer, alongside product development, research and documents. Codex surface (CLI/app/IDE), OpenCode version/model choices, exact installed plugin versions/modes and document packages are not established.
- Available plugin search did not identify Caveman/Ponytail/Humanizer; public primary sources were inspected. Superpowers appeared as available but not installed in this connected catalog, which does not establish the user's installation state in another agent host.

**Proposed ownership**

| Concern | Owner | Boundary |
|---|---|---|
| Software development workflow | Superpowers | Own planning/execution/review handoffs; avoid adding a competing mandatory planning framework. |
| Implementation restraint | Ponytail, provisionally full mode | Prefer the smallest complete solution while preserving caller coverage, validation, security, accessibility and meaningful checks. Consider ultra for deliberate design challenge, not automatic argument on every task. |
| Chat brevity | Caveman | Compress explanation, never facts, uncertainty, necessary decision rationale, or material limitations. Its actual source excludes persisted docs/code/PRs from the chat voice. |
| Authored prose | Humanizer in embedded/file mode | Polish audience and voice after factual drafting. Preserve facts, citations, commands, code, caveats and technical meaning. |
| Artifact production | The user's document skills | Own format, layout, tables, rendering and file validation. Identify actual formats before recommending replacements. |
| Staff-level decision behavior | A short explicit working agreement plus a small number of gap-filling skills | Frame intent, recommend a direction, explain tradeoffs, consider consequences beyond the immediate edit, make reversible calls, and finish authorized work. |
| Durable project context | Existing repository instructions and decision/task records | Ground decisions in actual constraints; preserve current state across sessions without introducing redundant sources of truth. |
| Specialist depth | On-demand, project-specific skills | Add only for observed gaps such as contracts, migrations, security, operations or product discovery. |

**Observed interactions requiring resolution**

1. Ponytail mandates a closing note about skipped checks and risks; Caveman usually removes closers. Preserve material limitations once in concise prose, omit ritual filler.
2. Caveman's brevity is explicitly scoped away from persisted artifacts. It should not compress a design report or override a document skill's format.
3. Humanizer has an embedded mode that returns only final prose. Prefer that integration over its pasted-text draft/audit/final presentation during ordinary document work.
4. Superpowers links brainstorming, planning, execution and review. Dropping brainstorming or writing-plans from a standalone shortlist does not establish they should be disabled inside the framework.
5. Ponytail's minimum complete change and Superpowers' verification can be compatible, but their test/process triggers and host hooks require inspection. Do not assume prompt order will resolve runtime activation behavior.
6. More architecture/process skills may duplicate Ponytail and Superpowers. Audit marginal value before adding them.

**Next decision**

The three hosts and primary work are confirmed. The recommendation is now centered on production ML maintenance and upgrades. See PRODUCTION-ML-STACK.md for the concrete shared stack and production-ml-working-agreement.md for a proposed portable behavioral policy. Exact plugin variants/modes remain unverified; source review has not established the installed configuration or tested combined behavior.

**Implications of three hosts**

- Maintain one canonical working agreement, project constraints, decision record, and task state. Load them through each host's supported mechanisms using thin adapters; verify loading rather than assuming file names imply support.
- Keep the intended plugin roles consistent across hosts, but use each plugin's supported integration. Avoid a plugin install plus a second copied bootstrap of the same rules. Check effective activation, compaction behavior and delegated-agent behavior per host.
- Track exact source versions and local overrides. Review updates before spreading them across all three environments.
- Use one task lead and a clear handoff. When multiple agents edit concurrently, isolate workspaces/branches and assign integration ownership. Do not assume three simultaneous agents are always better.
- Choose task roles from demonstrated performance, current model, tools and available context; do not assume the host brand establishes planning or coding superiority.
- A full stack includes repository context, tool access, runtime/model settings, and deliverable validation, in addition to skill prompts.
- Current Caveman documentation distinguishes the voice skill from a larger runtime with input processing, model routing and work patterns. The existing voice-only recommendation is conditional on using that component. Avoid treating the broader runtime as a mere style setting.

**Source review of host integration**

- [Ponytail portability](https://github.com/DietrichGebert/ponytail/blob/main/docs/agent-portability.md) describes native Claude Code/Codex lifecycle integration and a separate OpenCode plugin. These are upstream claims, not verified local installations.
- [Superpowers OpenCode integration](https://github.com/obra/superpowers/blob/main/docs/README.opencode.md) documents version-dependent registration, bootstrap injection, tool mappings, and skill priority. Exact installed version therefore matters.
- [Caveman current scope](https://github.com/JuliusBrussee/caveman/blob/main/README.md) includes a standalone voice option and broader runtime features. Confirm which features are enabled before recommending changes.

**Evaluation that would support a recommendation**

Compare the existing stack with the proposed configuration on the same representative tasks: an approved tiny edit, an ambiguous feature request, a cross-file defect, a consequential design decision, and a document produced from evidence. Judge correctness, coverage of consequences, quality of recommendation, unnecessary questions/process, factual fidelity, evidence honesty, and cost/effort. Repeat representative cases before making broad efficacy claims. No new combined-stack trials have been run.

**Sources inspected**

- [caveman](https://github.com/JuliusBrussee/caveman/blob/main/skills/caveman/SKILL.md)
- [ponytail](https://github.com/DietrichGebert/ponytail/blob/main/skills/ponytail/SKILL.md)
- [humanizer](https://github.com/blader/humanizer/blob/main/SKILL.md)
- [superpowers](https://github.com/obra/superpowers/blob/main/README.md)
