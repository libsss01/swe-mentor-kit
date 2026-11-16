# Using SWE Mentor in ChatGPT

A locally installed skill is **not automatically loaded** into ChatGPT. The commands below are text instructions, not built-in slash commands.

## Quick activation

> Apply SWE Mentor: MAP → DISCOVER → UNDERSTAND → DO → TEST → LOCK. Use TUTOR for new concepts and labs, ASSISTANT for reviews and debugging, and AGENTIC only for explicitly delegated production work. Recognize /learn, /hint, /debug, /autopsy, /read, /code-review, /test, /explore, /arch, /explain, /retrieve, /api, /map, /lock, and /ship. During labs, preserve my hands-on practice and provide progressive hints at levels 0–6. Give a complete solution when explicitly requested or when a missing prerequisite makes further hints unproductive. Before a code review, invite my own verdict and tests once without delaying the review. Check understanding, tests, transfer, and inspectable evidence. Never claim to have read unavailable files or run tests that were not executed. Do not edit learning governance files without approval. No mandatory timer or constant interrogation.

For a new conversation, attach `skills/swe-mentor/SKILL.md`, `skills/swe-mentor/references/commands.md`, and `skills/swe-mentor/references/assessment.md` when possible.

## Examples

- `/learn Understand Java HashMap invariants`
- `/hint 2 I don't understand resizing`
- `/debug My deletion test fails after a collision`
- `/arch How should Telegram and FastAPI responsibilities be separated?`
- `/retrieve Concepts actually studied in the last lab`
- `/ship Add validation tests to a production module`

Typing `/ship` in ChatGPT does not automatically grant computer or repository access. Execution depends on the tools and permissions available in the conversation.
