#!/usr/bin/env python3
"""Explicit, local-only learning logs. Never auto-commits user records."""
from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path

KINDS = ("concepts", "mistakes", "questions", "review")
HEADERS = {
    "concepts": "# Concepts\n\nRecord durable understanding, not every definition encountered.\n",
    "mistakes": "# Mistakes\n\nPreserve significant bugs, original reasoning, and corrected models.\n",
    "questions": "# Questions\n\nKeep unresolved questions and hypotheses visible.\n",
    "review": "# Review\n\nActive recall attempts and transfer exercises; no automatic mastery scores.\n",
}


def log_dir(project: Path) -> Path:
    return project.resolve() / ".swe-mentor" / "learning"


def initialize(project: Path) -> list[Path]:
    if not project.is_dir():
        raise ValueError("Project directory does not exist")
    folder = log_dir(project)
    folder.mkdir(parents=True, exist_ok=True)
    created: list[Path] = []
    for kind in KINDS:
        path = folder / f"{kind}.md"
        try:
            with path.open("x", encoding="utf-8") as handle:
                handle.write(HEADERS[kind])
            created.append(path)
        except FileExistsError:
            pass  # preserve existing learning history
    return created


def append(project: Path, kind: str, title: str, content: str) -> Path:
    if kind not in KINDS:
        raise ValueError(f"Unknown category: {kind}")
    if not title.strip() or not content.strip():
        raise ValueError("Title and text cannot be empty")
    path = log_dir(project) / f"{kind}.md"
    if not path.is_file():
        raise FileNotFoundError("Logs are not initialized. Run init first.")
    with path.open("a", encoding="utf-8") as handle:
        handle.write(f"\n## {date.today().isoformat()}: {title.strip()}\n\n{content.strip()}\n")
    return path



def read_context(project: Path, limit: int = 3) -> dict[str, object]:
    """Read recent entries from four local logs without creating or editing files.

    Markdown headings are entry boundaries. A missing file is treated as absent
    history, never as a reason to invent content.
    """
    if not 1 <= limit <= 20:
        raise ValueError("limit must be between 1 and 20")
    folder = log_dir(project)
    output: dict[str, object] = {
        "project": str(project.resolve()),
        "available": False,
        "logs": {},
    }
    logs: dict[str, list[dict[str, str]]] = {}
    for kind in KINDS:
        file = folder / f"{kind}.md"
        entries: list[dict[str, str]] = []
        if file.is_file():
            output["available"] = True
            text = file.read_text(encoding="utf-8")
            current_title = None
            buffer: list[str] = []
            for line in text.splitlines():
                if line.startswith("## "):
                    if current_title is not None:
                        entries.append({"title": current_title, "text": "\n".join(buffer).strip()})
                    current_title = line[3:].strip()
                    buffer = []
                elif current_title is not None:
                    buffer.append(line)
            if current_title is not None:
                entries.append({"title": current_title, "text": "\n".join(buffer).strip()})
        logs[kind] = entries[-limit:]
    output["logs"] = logs
    return output


def main() -> None:
    parser = argparse.ArgumentParser(description="Manage project-local learning logs with explicit user intent")
    parser.add_argument("--project", type=Path, default=Path.cwd())
    sub = parser.add_subparsers(dest="action", required=True)
    sub.add_parser("init", help="Create missing logs, never overwriting existing ones")
    view = sub.add_parser("context", help="Read recent local notes without changing the project")
    view.add_argument("--limit", type=int, default=3)
    add = sub.add_parser("append", help="Append one user-approved learning note")
    add.add_argument("kind", choices=KINDS)
    add.add_argument("--title", required=True)
    add.add_argument("--text", required=True)
    args = parser.parse_args()
    if args.action == "init":
        created = initialize(args.project)
        print(f"Initialized {len(created)} new logs at {log_dir(args.project)}")
        print("Consider adding .swe-mentor/ to .gitignore (with the project owner's permission).")
    elif args.action == "context":
        print(json.dumps(read_context(args.project, args.limit), indent=2, ensure_ascii=False))
    else:
        path = append(args.project, args.kind, args.title, args.text)
        print(f"Appended to {path}")


if __name__ == "__main__":
    main()
