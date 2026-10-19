# Provenance and maintainer inventory

The complete proposal references seven upstream maintainers. This is a count of repository owners/organizations, not a count of every contributor to those projects, and it is not a verified inventory of the user's installations.

| Maintainer | Repository | Role in the proposal |
|---|---|---|
| JuliusBrussee | [caveman](https://github.com/JuliusBrussee/caveman) | Conversation style; broader runtime capabilities require separate selection. |
| DietrichGebert | [ponytail](https://github.com/DietrichGebert/ponytail) | Implementation restraint and smallest complete change. |
| obra | [superpowers](https://github.com/obra/superpowers) | Development workflow, several original trial skills, and code-reviewer template. |
| blader | [humanizer](https://github.com/blader/humanizer) | Authored prose editing. |
| magnus919 | [agent-skills](https://github.com/magnus919/agent-skills) | Architecture, verification, reliability, capacity/cost, and other screened skills. |
| wshobson | [agents](https://github.com/wshobson/agents) | Dependency upgrades and other screened skills; MLOps and troubleshooting agent references. |
| Anthropic | [claude-plugins-official](https://github.com/anthropics/claude-plugins-official) and [claude-code](https://github.com/anthropics/claude-code) | Selected security-agent reference and an alternative code-reviewer reference. |

**Additional instruction layer:** the assistant authored the working agreement, synthesis, routing policy, and four adapted agent definitions. It is a distinct source of design choices, not another upstream maintainer. Exact document skills are unknown and could add maintainers. The assumed Caveman/Ponytail/Superpowers/Humanizer repositories have not been confirmed against the user's installed variants.

## Pinned skill-screening sources

| Repository | Commit used for the original screening |
|---|---|
| magnus919/agent-skills | `06ca706ecaa80f6afb31ae28eb160d39372b7267` |
| wshobson/agents | `0874a27b17a22e2b7c2e2bcd725768e0803cad06` |
| obra/superpowers | `bb92a77741419a4ab5f06e711a283343f1ada0c3` |

The [manifest](manifest.json) identifies each exact source path and commit. [artifact-hashes.json](artifact-hashes.json) preserves the original bytes' digests for each skill, scenario, and work product. Original trial and result files are preserved unchanged in this compilation.

## Later source review

The foundation-plugin review and some agent references used upstream `main` links. Those links may evolve; they are not lockfiles or guarantees of the version installed by the user. The four-agent package was assembled on 2026-10-19. Its MLOps and troubleshooting source links use the pinned wshobson commit; the Superpowers and Anthropic source links point to `main`.

The agent adaptations are newly written definitions, not copies of the named upstream agents. In particular, `ml-release-reviewer` is a newly created review role, rather than an upstream agent offered under that name. Read [agent-stack/README.md](agent-stack/README.md) for the per-role relationship.

## Considered but not selected

[VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) was inspected as an alternative source. Its security-auditor and sre-engineer templates were not selected for the initial agent proposal. VoltAgent therefore belongs to the research history, not the seven-maintainer proposed stack. The reasons are recorded in the [agent report](agent-stack/README.md).

## Publication scope

The compilation includes generated reports, synthetic scenarios, saved subagent responses, assessment data, and proposed configuration files. It excludes downloaded third-party source trees, credentials, host configuration, and redundant generated ZIP archives. No blanket license is asserted over upstream work. Follow each upstream project's terms when obtaining or adapting its packages.
