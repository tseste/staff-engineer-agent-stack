# Decision status

This file distinguishes user-provided context from assistant recommendations. Publishing this repository is an archive action, not acceptance or installation of its contents.

## Confirmed context

- The user works with Codex, Claude Code, and OpenCode.
- The user reports using Caveman, Ponytail, Superpowers, document skills, and Humanizer.
- Work spans production maintenance/upgrades, product development, research, and documents; the main role is staff ML engineer.
- The original request required 50 skills and subagent-based screening, followed by workflow guidance and alternatives for dropped skills.
- The user requested that all proposals be compiled into a new **public** GitHub repository.

## Recommendations made, not adoption decisions

- Keep the existing foundation with explicit ownership of workflow, implementation restraint, chat style, and authored prose.
- Use a shared production-ML working agreement and six first-choice specialist skills.
- Keep the wider 42-skill shortlist available selectively, not globally mandatory.
- Make four specialist agent roles discoverable through native host definitions and explicit routing instructions.
- Keep one task lead and use isolated workspaces when concurrent writers are actually needed.

## Open questions before changing the user's setup

1. How will the three hosts be used: alternatives for a task, sequential handoffs, simultaneous collaboration, or different workflows?
2. Should specialist agents run automatically at selected points, be invoked manually, or be offered as choices?
3. Does the user want upstream definitions unchanged, a small set from one maintainer, or maintained custom adaptations across sources?
4. What are the actual host versions, models, plugin repositories, enabled modes, and installation scopes?
5. Which document packages and production ML technologies need coverage?
6. Which representative tasks and observed gaps would justify each addition?

These questions were not resolved before the agent pack was prepared. The pack remains a proposal for review, not a finalized operating model.

## Relationship between the reports

1. [REPORT.md](REPORT.md) records the original broad 50-skill screening and its generic starting suggestions.
2. [WORKFLOW-REPORT.md](WORKFLOW-REPORT.md) maps the screened library to workflow stages and replacements for eight dropped entries.
3. [STACK-DIRECTION.md](STACK-DIRECTION.md) and [PRODUCTION-ML-STACK.md](PRODUCTION-ML-STACK.md) narrow the recommendation around the existing plugins and production-ML role.
4. [agent-stack/README.md](agent-stack/README.md) proposes four delegated roles and host adapters.

Later tailored recommendations supersede earlier generic selection suggestions where they differ. No later synthesis was evaluated as a combined stack. A standalone drop of a Superpowers skill does not establish that the skill should be removed from Superpowers' internal workflow.
