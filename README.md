# Staff engineer agent stack

A common decision guide and a collection of custom agents for Codex, Claude Code and OpenCode. The primary use case is maintaining and upgrading production ML systems. The guide also covers everyday code changes, research and documentation.

**Start with the shared judgment guide.** It gives the lead and each specialist the same starting questions. What decision does the user need? What does the system actually do? What evidence would change the recommendation? Which remaining choice belongs to the user? Routine changes can take one edit and one check. [How to exercise engineering judgment](agent-stack/JUDGMENT.md)

| What you want to do | Where to start |
|---|---|
| Use the guidance in a project | The repository's [AGENTS.md](AGENTS.md) reads the shared guide. [CLAUDE.md](CLAUDE.md) imports those instructions for Claude Code. To use it elsewhere, copy the guide and reference its real location from the project's existing instructions. |
| Give each custom reviewer its own skills | Edit the [role manifest](agent-stack/roles.json), then [generate the host definitions](agent-stack/README.md). |
| Decide whether to call a reviewer | Read the [delegation guide](agent-stack/ROUTING.md). An available reviewer can answer a specific question or fill an existing review step. |
| Review an ML upgrade | Use the [production ML working agreement](production-ml-working-agreement.md) with the service's actual baselines, tolerances and recovery plan. |
| See how the guidance behaved | Read the two [scenario checks](agent-stack/judgment-checks.md), including a support-policy question and a rollout decision. |

## How the pieces fit

The lead owns the task end to end. It gets the shared guidance, the project's constraints, and descriptions of available specialists. Each specialist gets that same guidance, its own assignment, and skills selected for that assignment. Four advisory roles illustrate the pattern. The [agent guide](agent-stack/README.md) covers skill access and adding another role.

Caveman, Ponytail, Superpowers, Humanizer and document skills form the user's existing baseline. The six specialist skills in the October proposal are candidates for particular gaps. Choose additions against the outcome of real work, including whether a reviewer catches a material issue and how much extra review it creates. The user's installation versions, preferred dispatch settings and choice of host for a given task are still open. [Stack proposal](PRODUCTION-ML-STACK.md) · [Decision record](DECISIONS.md)

## Research and evidence

The original evaluation gave 50 skills one qualitative scenario each, with one model, one evaluator and no comparison run. It retained 42 candidates and dropped eight on performance, overlap or scope. The six suggested specialists came from that set of 42. The trial scores describe the work products from those scenarios. The effectiveness of the combined stack on the user's three installations remains unmeasured.

| Research artifact | Contents |
|---|---|
| [Skill evaluation](REPORT.md) and [method](METHOD.md) | All 50 decisions, judgments, scenarios and work products. [Retained candidates](KEPT.md) |
| [Workflow report](WORKFLOW-REPORT.md) | Task routing, worked examples and replacements for all eight dropped skills. |
| [Plugin interactions](STACK-DIRECTION.md) and [provenance](PROVENANCE.md) | The roles and interactions of the existing plugins, seven upstream owners and the assistant-authored additions. |
| [Evaluation data](evaluation.json) and [evidence hashes](artifact-hashes.json) | Machine-readable decisions and SHA-256 digests. Original trial files retain their historical environment paths for verification. |

## Build and check

With Python 3.11+ and PyYAML installed, regenerate and validate the configurations after editing the shared policy or manifest.

```bash
python agent-stack/build.py
python scripts/validate.py
```

The historical reports have separate generators. Run `python download_sources.py` to fetch the pinned public snapshots, then `python build_report.py` to create the original skill report and evidence ZIP. Finally run `python build_workflow_report.py` to rebuild the workflow tables and their bundle, which includes that ZIP. The source snapshots and generated ZIP files are ignored by Git.
