# Learning Logs — optional, local, meaningful

Inspired by Manware's four separate learning logs. These files record a learner's **actual** work; they are not a curriculum, surveillance system, or automatic score.

## Storage and privacy

Store real entries at `<project>/.swe-mentor/learning/`, never under the installed plugin's files. Use `templates/learning/` only as examples. The learner chooses whether to initialize logs. Do not stage, commit, upload or send logs externally without explicit authorization. Suggest `.swe-mentor/` in `.gitignore`; ask before changing the file.

The optional `scripts/learning_logs.py` utility can initialize and append entries, and its read-only `context` subcommand selects recent entries for the next session. Agents should ask consent before invoking it to write. Manual Markdown editing is equally valid. Avoid storing secrets, sensitive details, or full chat transcripts.

## Four files

1. **concepts.md**: Record only lasting understanding, in the learner's own words; optionally add a corrected explanation, example, and related concept. Explain whether the evidence was inspected.
2. **mistakes.md**: Preserve the failure, the original reasoning (do not rewrite it retroactively), the corrected mental model, the classification (slip, gap, misconception), an experiment, and a targeted retry.
3. **questions.md**: Capture an unresolved question, its context, current hypothesis, experiment/documentation needed, and state (open/answered). Never silently close it.
4. **review.md**: Track active recall prompts, last attempt, support needed, observed answer/verification, and a later transfer problem. A planned review is **not** a scheduled reminder.

## Session lifecycle

**/learn — beginning:** If logs exist and reading is authorized, run `python3 scripts/learning_logs.py --project <project> context` or inspect the available files; select at most one relevant unresolved question or mistake, one prior concept, and one current project objective. Ask a short recall or prediction before teaching. If no logs exist, begin normally and optionally offer log initialization once.

**During learning:** Progressively adjust hints to the actual response; a student's independent explanation/test earns stronger evidence than confidence or agreement. Keep a single active goal, not a ritual of typing commands.

**/lock — after meaningful work:** Offer a short factual entry in one or more relevant logs. Do not write unless authorized. Use dates for traceability, and distinguish claims, inspected artifacts, and executed tests.

**/retrieve — later:** Reopen available project logs on each new session; use prior logs without immediately showing the saved answers. Ask the learner to predict, debug or apply the concept in a *different* context. Correct misunderstandings, update only with authorization, and never say the learner remembered something you cannot actually access.

## Example: Java serialization over three sessions

- Session 1: Goal: save a library's book list so it survives restarts. Student learns why object data needs a persisted representation. Their initial explanation goes into `concepts.md` only after they successfully explain a round trip.
- Session 1 bug: `NotSerializableException` for a referenced field. Their wrong guess (“all fields are automatically serializable”) and experiment go to `mistakes.md`, if the student approves.
- Session 1 open question: “What happens if the Book class changes before loading an older file?” goes to `questions.md`.
- Session 2: `/learn` automatically recovers that question. Use `review.md` to quiz on compatibility before providing an explanation, then help build a migration/compatibility test.
- Session 3: Independent transfer to a new settings object plus tests and delayed recall; only then consider a scoped skill-validation claim based on inspectable proof.

Never mistake a log entry, an AI-generated implementation, or a single correct reply for demonstrated mastery.
