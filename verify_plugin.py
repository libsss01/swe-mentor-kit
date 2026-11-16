#!/usr/bin/env python3
"""Validate distributable SWE Mentor plugin layout without running agents."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parent
COMMANDS = ("learn hint debug autopsy read code-review test explore arch explain retrieve api map lock ship").split()
for name in ("plugin.json", ".claude-plugin/plugin.json", ".claude-plugin/marketplace.json",
             ".agents/plugins/marketplace.json"):
    data = json.loads((ROOT/name).read_text(encoding="utf-8"))
    assert isinstance(data, dict) and data["name"] == "swe-mentor", name
assert json.loads((ROOT/"plugin.json").read_text())["version"] == "0.4.0"
skill = (ROOT/"skills/swe-mentor/SKILL.md").read_text(encoding="utf-8")
assert skill.startswith("---\nname: swe-mentor\n")
protocol = (ROOT/"skills/swe-mentor/references/commands.md").read_text(encoding="utf-8")
assert (ROOT/"skills/swe-mentor/references/assessment.md").exists()
for command in COMMANDS:
    content = (ROOT/f"commands/{command}.md").read_text(encoding="utf-8")
    assert content.startswith("---\n"), command
    assert "$ARGUMENTS" in content, command
    assert re.search(r"^## /"+re.escape(command)+r"(?:\s|\[)", protocol, re.M), command
claude=json.loads((ROOT/".claude-plugin/marketplace.json").read_text())
codex=json.loads((ROOT/".agents/plugins/marketplace.json").read_text())
assert claude["plugins"][0]["source"] == "./"
assert codex["plugins"][0]["source"]["path"] == "./"
root_manifest=json.loads((ROOT/"plugin.json").read_text(encoding="utf-8"))
assert root_manifest["extensions"]["com.openai"]["interface"]["displayName"] == "SWE Mentor"
assert (ROOT/"skills/swe-mentor/references/learning-logs.md").exists()
assert len(list((ROOT/"templates/learning").glob("*.md"))) == 4
assert (ROOT/"scripts/learning_logs.py").exists()
print("PASS: plugin manifests, 15 commands, learning log protocol, 4 templates and helper.")
