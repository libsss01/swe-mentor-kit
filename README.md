# SWE Mentor Kit — v0.3.0

**Learn to reason, build, debug, test, review, and ship software with AI — without outsourcing the skill you want to develop.**

An installable, portable Socratic learning plugin for **Claude Code** and **Codex**, with a separate prompt-based guide for **ChatGPT**, inspired by [Manware's AI Learning Toolkit](https://github.com/i-am-manware/Manware-s-AI-Learning-Toolkit), adapted for the Software Engineering & Computer Science learning path.

## Pedagogical protocol

**MAP → DISCOVER → UNDERSTAND → DO → TEST → LOCK**

Three modes:
- **TUTOR**: new concepts and focused labs; the learner writes the target code, AI offers graduated hints.
- **ASSISTANT**: debugging, code reading, design discussions and reviews; inspect hypotheses and evidence.
- **AGENTIC / SHIP**: explicit delegation for production, with diff, tests, and risk review. This does not establish that the learner mastered AI-generated code.

The goal is **Software Engineer** competency, not a particular framework, badge, or technology stack. The kit does not replace any existing roadmap.

## Install as a plugin (recommended)

SWE Mentor is now a **distributable plugin** for Claude Code and Codex. You don't need to clone the repository or execute an installer for normal use.

### Claude Code

Run these inside a Claude Code session, one at a time:

```text
/plugin marketplace add libsss01/swe-mentor-kit
/plugin install swe-mentor@swe-mentor
```

Restart Claude Code and try `/swe-mentor:learn`, `/swe-mentor:hint 1`, `/swe-mentor:debug`, or `/swe-mentor:retrieve`. The plugin ships 15 namespaced commands.

Optional local validation before installation:

```bash
claude plugin validate .
```

### Codex

Register the GitHub marketplace, then install the plugin:

```bash
codex plugin marketplace add libsss01/swe-mentor-kit
codex plugin add swe-mentor@swe-mentor
```

In Codex, select or invoke the bundled skill with `$swe-mentor` and describe your workflow, for example: `$swe-mentor /debug My deletion test fails after a hash collision`.

> Availability of marketplace installation depends on your local Codex version. If `codex plugin add` is unsupported, consult the Codex plugin support for your client version. Do not assume marketplace installation is supported. This repository is not yet listed in any universal public plugin directory.

### What gets installed?

- `plugin.json`: portable Agent Plugins manifest.
- `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`: Claude Code package identity and GitHub marketplace.
- `.codex-plugin/plugin.json` and `.agents/plugins/marketplace.json`: Codex compatibility and local marketplace.
- `skills/swe-mentor/SKILL.md`: self-contained Socratic tutoring skill with references.
- `commands/*.md`: 15 Claude Code plugin commands.

**This is a skills-only plugin.** It has no MCP server, credential requirements, telemetry, persistent cloud service, or automatic file mutation. Learning logs remain optional.

### Learn by building a plugin

A plugin is an installable bundle, a skill defines reusable instructions, and a marketplace indexes bundles. Start by reading `skills/swe-mentor/SKILL.md`, then `.claude-plugin/plugin.json`, `plugin.json`, and the two marketplace catalogs. To contribute: fork, edit a workflow, run `python3 verify_plugin.py`, validate the Claude plugin locally, then submit a pull request.

## Usage

**Claude Code:** after installing the plugin, try `/swe-mentor:learn`, `/swe-mentor:hint 2`, `/swe-mentor:debug`, `/swe-mentor:code-review`, `/swe-mentor:retrieve`, or `/swe-mentor:ship`. The 15 commands live in `commands/` and are namespaced by the plugin.

**Codex:** invoke the included skill using `$swe-mentor /debug My Java deletion test fails after a collision`, or select it in a supported skill picker.

**ChatGPT:** this repository does not install a native ChatGPT plugin. Follow the prompt-based instructions below.

### Local validation

```bash
python3 verify_plugin.py
claude plugin validate .
```

The Python script checks the repository structure and bundled learning-log layout; the second command needs Claude Code. Actual installation and agent behavior still require local tests.

## Complete command set

| Command | Purpose |
|---|---|
| `/learn` | Select target competency and first exercise |
| `/hint` | Graduated help 0–6 |
| `/debug` | Reproduce, hypothesize, inspect, fix and test |
| `/autopsy` | Postmortem a bug and learn its transferable lesson |
| `/read` | Understand existing code and predict behavior |
| `/code-review` | Severity-ranked review without immediate rewrite |
| `/test` | Derive meaningful tests from contracts |
| `/explore` | Compare tradeoffs and alternatives |
| `/arch` | Challenge minimal architecture and failure modes |
| `/explain` | Explain-back and check understanding |
| `/retrieve` | Active recall from inspectable past work |
| `/api` | Understand an API's contract, errors and constraints |
| `/map` | Locate a prerequisite or next micro-lab |
| `/lock` | Consolidate a lesson and link actual evidence |
| `/ship` | Delegate an explicit, bounded production task |

Manware-inspired commands are adapted, not reproduced verbatim. `/map`, `/lock`, `/ship` extend the workflow.

## Repository structure

```text
.claude-plugin/
  plugin.json              # Claude Code plugin metadata
  marketplace.json         # Claude Code marketplace catalog
.codex-plugin/
  plugin.json              # Codex compatibility metadata
.agents/plugins/
  marketplace.json         # Codex marketplace catalog
plugin.json                # Portable Agent Plugins manifest
skills/swe-mentor/
  SKILL.md                 # Main pedagogical behavior
  references/
    commands.md            # Workflows for all 15 commands
    assessment.md          # Evidence standards
    learning-logs.md       # Persistent learning log protocol
commands/                  # 15 Claude Code plugin commands
templates/learning/        # Four log templates, not student data
scripts/learning_logs.py   # Optional local init/append tool
tests/                     # Local filesystem regression tests
.github/workflows/test.yml # CI checks on push and pull request
verify_plugin.py           # Plugin structure validation
README.md
LICENSE
```

## Using the method in ChatGPT (prompt-based, not a native plugin)

A locally installed Claude/Codex skill is **not automatically loaded** into ChatGPT. Copy this brief guidance into a ChatGPT conversation and attach the skill files if the conversation does not already contain the instructions:

> Apply SWE Mentor: MAP → DISCOVER → UNDERSTAND → DO → TEST → LOCK. Tutor new concepts and labs; assist reviews and debugging; use agentic implementation only on explicit delegation. During /learn, dynamically use hints 0–6, debugging, testing, code review and retrieval without requiring slash commands. Treat '/hint', '/debug', '/retrieve', and '/ship' as textual intents, not built-in ChatGPT commands. Protect the learner's independent practice. Do not claim access to unavailable logs or tests. Store learning notes only in authorized project-local files and with consent.

Example: `/learn I need to save and load my Java book catalog, and want to understand serialization while implementing it.`

## Manual behavior checks (also supported by automated structural and filesystem tests)

| Scenario | Expected |
|---|---|
| /learn: Java project needs serialization | A project-specific path from concept to micro-lab, no demand to call /hint |
| Student hits NotSerializableException | Hypothesis, discriminating observation, no unrequested rewrite |
| /hint 0 | Question to elicit a prediction, not complete code |
| Explicit /hint 6 | Explained solution and transfer challenge |
| Session starts with approved existing logs | Retrieval from one real prior difficulty, not invented memory |
| No project logs / declined logging | Session still works; no files created |
| /lock after meaningful learning | Suggest concise notes; write only with consent |
| /ship explicitly delegated production task | Authorized implementation with tests/diff/risks; no mastery claim |

**Automated tests**: run `python3 verify_plugin.py` and `python3 -m unittest discover -s tests -v`. GitHub Actions runs both on pushes and pull requests. These tests do **not** test model responses or prove Claude/Codex compatibility; those require real-client evaluation.

## Safety, evaluation and limits

- No implicit repository edits in TUTOR mode, and no automatic escalation to SHIP after a blockage.
- Verification = observed tests and inspectable artifacts; AI-generated changes alone do not demonstrate mastery.
- The assistant should first invite a learner's own verdict and evidence, **without blocking a requested review**.
- No mandatory 30-minute timer, no compulsory journal after every message, no needless quizzes.
- Keep capability progress separate from what was discussed, attempted, or planned.
- Do not update learning governance documents automatically.
- Syntax and static checks are provided; behavior must be tested locally with your Claude Code and Codex versions.

Original inspiration: [Manware](https://github.com/i-am-manware/Manware-s-AI-Learning-Toolkit). Platform documentation: [Claude Code skills](https://code.claude.com/docs/en/skills) · [Codex skills](https://developers.openai.com/codex/skills). This is an independent pedagogical adaptation, not an official plugin.
