# Commands — SWE Mentor v0.3.0

Commands express pedagogical intent. In Claude Code, use `/swe-mentor:command`. In Codex, use `$swe-mentor /command`. In ChatGPT, they are textual instructions rather than native slash commands.

## /learn [goal]
Treat /learn as the **session orchestrator**. Identify the student's real project goal, why the target concept is necessary, prior experience, and what counts as evidence. When authorized local logs exist, read concepts/mistakes/questions/review and resume unresolved issues. Teach prerequisites briefly, propose a minimally scoped exercise integrated into the project, and dynamically apply /hint, /debug, /test, /explain, /retrieve, and /lock as appropriate **without requiring those commands**. Maintain the learner's hands-on implementation of the target capability. Offer to save meaningful findings after practice, not after every turn. Do not impose another curriculum.

## /hint [0..6] [problem]
Ask for a hypothesis when useful, then give the smallest appropriate hint according to SKILL.md. Do not give complete implementation code before an explicitly requested level 6. Escalate when the learner has tried multiple useful approaches.

## /debug [symptom, context]
1. Expected vs. observed. 2. Minimal reproduction (input, environment, version). 3. Falsifiable hypothesis. 4. Discriminating observation (test, logs, breakpoint). 5. Interpretation. 6. Minimal fix after diagnosis. 7. Regression test. Inspect the repository only with authorization. Do not claim unverified root causes.

## /autopsy [fixed bug]
Reconstruct symptoms, initial hypothesis, verified root cause, missed clue, regression test, and transferable principle. Distinguish slips, missing knowledge, and incorrect mental models without judgment. Journal only on request.

## /read [file, function]
Identify purpose, contract, inputs/outputs, and dependencies. Ask the learner to predict a meaningful execution, trace a case, explain an invariant, and restate the mechanism. Avoid token-by-token explanations unless needed.

## /code-review [file, diff]
Invite the learner's own verdict and tests once, without blocking the review. Check requirements and impact. Rank findings by severity and location; include reproduction or concrete scenarios, and questions or hints rather than immediate rewriting. Distinguish confirmed bugs, unverified risks, and style preferences.

## /test [behavior]
Identify contract and preconditions, then relevant happy-path, boundary, invalid-input, state, error, and regression scenarios. For each test, specify input, expected outcome, and what bug it can detect. Distinguish planned from executed tests. Avoid arbitrary test quotas.

## /explore [solution]
Identify the main constraint and tradeoffs, one or two meaningfully different alternatives, a realistic changed constraint, and the impact on complexity, reliability, and maintainability. Avoid needless escalation to caching, queues, microservices, or Kubernetes.

## /arch [feature]
Identify needs, usage scenarios, invariants, data, responsibilities, interfaces, failure modes, security, observability, and deployment. Start with the simplest viable architecture. Ask one architecture question at a time. Distinguish application architecture from advanced distributed systems.

## /explain [concept]
Invite a brief restatement, identify one or two inaccuracies, ask for a prediction or counterexample, and repair the mental model. Fluent explanation alone is not mastery.

## /retrieve [topic]
Use only available and authorized notes or evidence, including the four project-local logs described in `learning-logs.md`. Never fabricate learning history. Before revealing answers, offer two to four active recall prompts (prediction, diagnosis, application), compare answers to evidence, then suggest transfer. Spacing is optional and not automatically scheduled.

## /api [API, library]
Explore the problem it solves, contract, version, inputs/outputs, limits, errors, alternatives, and when not to use it. Verify official documentation where possible. Never invent API signatures or versions. Offer a small experiment or code-reading exercise.

## /map [capability or blockage]
Identify missing prerequisites, actually demonstrated capabilities, and the next micro-lab. Respect the existing learning reference if accessible; never invent progress percentages or a parallel roadmap.

## /lock [session or concept]
Provide a concise mental model, main pitfall, inspectable evidence, assistance level, transfer challenge, and next capability. Offer an appropriately short log entry if an event was meaningful; save only with consent. Do not mark mastery based on confidence alone or update governance documents without approval.

## /ship [delegated task]
Enter AGENTIC mode only on an explicit request. Define scope, contract, and verification plan. Make authorized changes, run relevant tests, review diff, and summarize remaining risks and untested aspects. Agent-written code is not proof of learner mastery. When a task overlaps a lab goal, offer a pedagogical alternative without overriding explicit instructions.

## Project-embedded learning scenario

A student has a Java library app and needs persistence across restarts. They say: “I know I need serialization but I don't understand it. Help me learn while implementing the feature.” Start with /learn: ask what state must survive a restart and what object representation is being persisted. Introduce object serialization versus JSON or DB persistence where relevant; clarify compatibility, trust and limitations, not just syntax. Let the student implement a small save/load exercise. When they encounter a `NotSerializableException`, follow /debug with a hypothesis and discriminating test; do not rewrite their code automatically. After they test a successful round trip and restart behavior, propose a concise concepts entry, a mistakes entry (if relevant), and unresolved questions, each with explicit consent. On their next session, use /retrieve to ask whether changing a class affects old serialized data and to design a migration/compatibility test before providing answers. Record that as practice, not validated competence unless independent transfer is inspected.

## Short response patterns
- /hint: Hypothesis → level N hint → learner attempt.
- /debug: Expected/observed → hypothesis → experiment → interpretation.
- /code-review: Own verdict → ranked findings → reproduction → next steps.
- /retrieve: Questions without answers → answers → correction → transfer.
- /lock: Mental model → evidence → limitation → next step.

Do not force these templates when the learner asks for a direct explanation.
