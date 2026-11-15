#!/usr/bin/env python3
"""Vérifications statiques du kit ; aucun agent n'est exécuté."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
COMMANDS = ['learn', 'hint', 'debug', 'autopsy', 'read', 'code-review',
            'test', 'explore', 'arch', 'explain', 'retrieve', 'api',
            'map', 'lock', 'ship']

main = (ROOT / 'core/SKILL.md').read_text(encoding='utf-8')
protocol = (ROOT / 'core/references/commands.md').read_text(encoding='utf-8')
assert main.startswith('---\nname: swe-mentor\n')
assert 'description:' in main.split('---', 2)[1]
for command in COMMANDS:
    assert re.search(r'^## /' + re.escape(command) + r'(?:\s|\[)', protocol, flags=re.M), command
    wrapper = ROOT / f'claude-commands/swe-{command}.md'
    assert wrapper.exists(), command
    content = wrapper.read_text(encoding='utf-8')
    assert content.startswith('---\n') and f'`/{command}`' in content
    assert '$ARGUMENTS' in content
assert (ROOT / 'examples/learning-log-template.md').exists()
assert (ROOT / 'CHATGPT-USAGE.md').exists()
assert (ROOT / 'install.ps1').exists() and (ROOT / 'install.sh').exists()
print('OK : 1 skill principal, 15 commandes Claude, 2 références, installation et chat.')
