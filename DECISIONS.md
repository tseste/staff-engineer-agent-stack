# Decision record

## User direction

The user works with Codex, Claude Code and OpenCode. They use Caveman, Ponytail, Superpowers, document skills and Humanizer across production ML maintenance and upgrades, product development, research and writing. They asked for a public record of the stack proposals and the 50-skill screening.

On 2026-11-17 the user prioritized writing down how the agent should exercise judgment and specified that they plan to have many custom agents with their own skills. This revision implements that direction in a shared guide and a role manifest.

## Design choices in this revision

- Keep one authored decision guide. The lead can read it through project instructions. Every generated specialist definition carries its text, including on hosts that start a separate context.
- Give each role an advertised purpose, instructions and named skill assignments with conditions for use. Four advisory examples cover code review, security review, ML release review and production investigation. The role count can grow with actual demand.
- Treat each host's skill discovery, loading and tool permissions as separate configuration concerns. Match skill identifiers to what the installation exposes.
- Leave the choice of manual review, suggested review or automatic review to the operator and repository workflow. Registering a specialist makes the option available. The proposed default in the absence of a preference is to suggest a discretionary reviewer when its answer matters.
- Use current plugins as the comparison baseline. Replay a past decision with and without one proposed addition on the same host and model. Compare concrete findings, false alarms and review effort before expanding adoption.

## Still to decide in a real project

The user's three-host handoff pattern, preferred delegation mode, versions, installed skill IDs, actual document packages, and service-specific evaluation entry points are open. Those choices can vary by project. A useful first comparison is an upgrade with a known regression and its pre-release evidence, with the historical outcome withheld during review.

## Earlier work

The [50-skill evaluation](REPORT.md) and [workflow report](WORKFLOW-REPORT.md) preserve the original screening and alternatives. The [October stack proposal](PRODUCTION-ML-STACK.md) records the six suggested specialists and plugin roles. The [judgment guide](agent-stack/JUDGMENT.md), [agent guide](agent-stack/README.md) and [routing guidance](agent-stack/ROUTING.md) describe the current design. A standalone keep/drop judgment did not test the effect of removing an internal Superpowers step.
