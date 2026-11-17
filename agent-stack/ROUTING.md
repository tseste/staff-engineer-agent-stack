# Choosing when to involve a specialist

Start with the [shared judgment guide](JUDGMENT.md). The lead can use the short descriptions in its host's agent catalog to discover the right person for a question. Each specialist gets its own instructions and assigned skills. Check which roles the host has actually registered.

| Situation | Lead's decision |
|---|---|
| The goal, remedy and acceptance check are clear | Make the change and verify it. An outdated runbook flag with a supported replacement usually takes one editor and one check. |
| A fact is unknown and available locally | Inspect the artifact or run the smallest check that distinguishes the options. |
| The outcome depends on a user's preference | Explain the consequence of the choice and ask the person who owns it. Continue the parts that work under either answer. |
| Independent expertise could change a consequential decision | Use the project's agreed review process. If the dispatch preference is still open, suggest the reviewer and name the question. Honor explicit requests to delegate and established review requirements. |

## Four questions the current roles can answer

| Role | A useful question for this role |
|---|---|
| `staff-code-reviewer` | Which caller could break under this diff, and would our tests notice? If Superpowers already schedules an independent review of the same change, use that review opportunity. |
| `staff-security-reviewer` | Does this change let a caller read artifacts outside its tenant, and where should the ownership check happen? |
| `ml-release-reviewer` | Are baseline and candidate predictions comparable on the critical cohort, and can the previous release read today's features? |
| `production-investigator` | Did inference get slower inside the runtime or did requests spend longer in a queue? Which observation would distinguish the two? |

Give the specialist the decision, the exact question, the revision or time window, the relevant evidence and any operating limits. For an independent check, supply the acceptance criteria and observations before giving it the lead's preferred answer. Ask for a finding, its evidence, and what the finding changes. The lead checks consequential claims, resolves conflicting assumptions and owns the recommendation. The service owner retains release authority under project policy.

If the role or an essential skill is missing, say what was available. Use direct evidence to finish what you can and describe the specific gap if it affects the result.

## A production example

A runtime upgrade passes unit tests. Aggregate recall holds steady, but the paired evaluation shows a critical cohort outside its agreed tolerance. The old model is still in the registry and its previous preprocessing image has disappeared from the rollback manifest.

The lead already has grounds to recommend holding promotion. It can inspect the image reference and prepare a replay while a release reviewer independently checks cohort membership and baseline parity, if that review is wanted. A competing reviewer opinion carries weight if it identifies a concrete error such as mismatched cohort filters. The service owner only needs a question if someone proposes changing the acceptance criterion or taking an exception. The graph, manifests and cohort results travel with the decision whichever host is used next.
