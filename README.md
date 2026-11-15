# SWE Mentor Kit — v0.1

**Learn to reason, build, debug, test, review, and ship software with AI — without outsourcing the skill you want to develop.**

A portable Socratic learning kit for **Claude Code**, **Codex**, and **ChatGPT**, inspired by [Manware's AI Learning Toolkit](https://github.com/i-am-manware/Manware-s-AI-Learning-Toolkit), adapted for the Software Engineering & Computer Science learning path.

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

Restart Claude Code and try `/swe-mentor:learn`, `/swe-mentor:hint 1`, `/swe-mentor:debug`, or `/swe-mentor:retrieve`. The plugin ships 15 namespaced commands. These commands are plugin commands, distinct from the legacy standalone `/swe-*` files.

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

> Availability of marketplace installation depends on your local Codex version. If `codex plugin add` is unsupported, use your desktop Plugins Directory or the standalone installer below. This repository is not yet listed in any universal public plugin directory.

### What gets installed?

- `plugin.json`: portable Agent Plugins manifest.
- `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`: Claude Code package identity and GitHub marketplace.
- `.codex-plugin/plugin.json` and `.agents/plugins/marketplace.json`: Codex compatibility and local marketplace.
- `skills/swe-mentor/SKILL.md`: self-contained Socratic tutoring skill with references.
- `commands/*.md`: 15 Claude Code plugin commands.

**This is a skills-only plugin.** It has no MCP server, credential requirements, telemetry, persistent cloud service, or automatic file mutation. Learning logs remain optional.

### Learn by building a plugin

A plugin is an installable bundle, a skill defines reusable instructions, and a marketplace indexes bundles. Start by reading `skills/swe-mentor/SKILL.md`, then `.claude-plugin/plugin.json`, `plugin.json`, and the two marketplace catalogs. To contribute: fork, edit a workflow, run static checks, validate the Claude plugin locally, then submit a pull request.

## Standalone/manual install (legacy)

Clone this repository, then run from its root:

**Windows PowerShell**

```powershell
git clone https://github.com/libsss01/swe-mentor-kit.git
cd swe-mentor-kit
python .\verify_kit.py
.\install.ps1 -Scope User
```

For a single project only: `.\install.ps1 -Scope Project -Target "C:\path\to\project"`.

**Linux/macOS**

```bash
git clone https://github.com/libsss01/swe-mentor-kit.git
cd swe-mentor-kit
python3 verify_kit.py
bash install.sh user
```

Or `bash install.sh project /path/to/project`.

**Install is non-destructive:** existing target files are skipped, not overwritten. Reinstall after an update only after examining the diff and backing up older installed files.

## Use

**Claude Code:** `/swe-learn`, `/swe-hint 2`, `/swe-debug`, `/swe-code-review`, `/swe-retrieve`, `/swe-ship`, etc. All 15 commands use the `/swe-` prefix to avoid name collisions.

**Codex:** `$swe-mentor /debug My Java test fails after deletion` or select the skill with `/skills` where available.

**ChatGPT:** use the guidance in [CHATGPT-USAGE.md](CHATGPT-USAGE.md). Text commands in chat are not guaranteed native slash commands.

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
core/
  SKILL.md
  references/
    commands.md
    assessment.md
claude-commands/        # 15 /swe-* wrappers
examples/
  learning-log-template.md
install.ps1             # Windows installer
install.sh              # Linux/macOS installer
verify_kit.py           # static validation
CHATGPT-USAGE.md
TESTS-MANUELS.md
```

## Safety, evaluation and limits

- No implicit repository edits in TUTOR mode, and no automatic escalation to SHIP after a blockage.
- Verification = observed tests and inspectable artifacts; AI-generated changes alone do not demonstrate mastery.
- The assistant should first invite a learner's own verdict and evidence, **without blocking a requested review**.
- No mandatory 30-minute timer, no compulsory journal after every message, no needless quizzes.
- Keep capability progress separate from what was discussed, attempted, or planned.
- Do not update learning governance documents automatically.
- Syntax and static checks are provided; behavior must be tested locally with your Claude Code and Codex versions.

Original inspiration: [Manware](https://github.com/i-am-manware/Manware-s-AI-Learning-Toolkit). Platform documentation: [Claude Code skills](https://code.claude.com/docs/en/skills) · [Codex skills](https://developers.openai.com/codex/skills). This is an independent pedagogical adaptation, not an official plugin.
