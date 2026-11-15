# Manual Behavioral Tests After Installation

Test the skill in a disposable repository before using it in a production repository.

| Input | Expected behavior |
|---|---|
| `/hint 0` for a Java bug | Hypothesis-focused question, no code |
| Explicit `/hint 6` | Explained solution and transfer exercise |
| `/debug` with insufficient logs | Expected vs. observed and a discriminating experiment; no invented cause |
| `/read` for Python code | Guided prediction and contract, not unnecessary line-by-line paraphrasing |
| `/code-review` with a diff | One non-blocking invitation for self-assessment, then verifiable ranked findings |
| `/retrieve` without notes | No fabricated memories |
| `/arch` for a CRUD API | Simple architecture before extra infrastructure |
| Explicit `/ship` task | Authorized diff, tests, and risks |
| `/lock` without evidence | No “mastered” status without proof |

**Still requires local verification:** model behavior, native slash commands, permissions, and compatibility with installed Claude Code and Codex versions. `verify_kit.py` performs static checks, not model-behavior tests.
