#!/usr/bin/env bash
# SWE Mentor Kit — installation non destructive (macOS/Linux)
set -euo pipefail
kit="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
mode="${1:-project}"
if [[ "$mode" == "user" ]]; then
  root="$HOME"
elif [[ "$mode" == "project" ]]; then
  root="$(cd "${2:-.}" && pwd)"
else
  echo 'Usage: bash install.sh project /chemin/vers/projet | bash install.sh user' >&2
  exit 2
fi
copy_safely() {
  local from="$1" to="$2"
  if [[ -e "$to" ]]; then printf 'SKIP (existe): %s\n' "$to"; return; fi
  mkdir -p "$(dirname "$to")"
  cp "$from" "$to"
  printf 'INSTALLE: %s\n' "$to"
}
for folder in .claude/skills/swe-mentor .agents/skills/swe-mentor; do
  while IFS= read -r -d '' file; do
    relative="${file#"$kit/core/"}"
    copy_safely "$file" "$root/$folder/$relative"
  done < <(find "$kit/core" -type f -print0)
done
while IFS= read -r -d '' file; do
  copy_safely "$file" "$root/.claude/commands/$(basename "$file")"
done < <(find "$kit/claude-commands" -maxdepth 1 -name '*.md' -type f -print0)
echo 'Installation terminée sans écraser les fichiers existants.'
