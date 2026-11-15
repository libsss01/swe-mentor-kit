# SWE Mentor Kit — non-destructive installer (PowerShell 5+)
[CmdletBinding()]
param(
  [ValidateSet('Project', 'User')]
  [string]$Scope = 'Project',
  [string]$Target = '.'
)
$ErrorActionPreference = 'Stop'
$kit = Split-Path -Parent $MyInvocation.MyCommand.Path
if ($Scope -eq 'User') { $root = [Environment]::GetFolderPath('UserProfile') }
else { $root = (Resolve-Path -LiteralPath $Target -ErrorAction Stop).Path }

function Copy-Safely([string]$source, [string]$destination) {
  if (Test-Path -LiteralPath $destination) {
    Write-Host "SKIP (already exists): $destination" -ForegroundColor Yellow
    return
  }
  $parent = Split-Path -Parent $destination
  if (-not (Test-Path -LiteralPath $parent)) { New-Item -ItemType Directory -Path $parent -Force | Out-Null }
  Copy-Item -LiteralPath $source -Destination $destination
  Write-Host "INSTALLED: $destination" -ForegroundColor Green
}
$sourceCore = Join-Path $kit 'core'
foreach ($sub in @('.claude/skills/swe-mentor', '.agents/skills/swe-mentor')) {
  $targetSkill = Join-Path $root $sub
  Get-ChildItem -LiteralPath $sourceCore -File -Recurse | ForEach-Object {
    $relative = $_.FullName.Substring($sourceCore.Length).TrimStart([char[]]@('\', '/'))
    Copy-Safely $_.FullName (Join-Path $targetSkill $relative)
  }
}
$commands = Join-Path $kit 'claude-commands'
Get-ChildItem -LiteralPath $commands -Filter '*.md' -File | ForEach-Object {
  Copy-Safely $_.FullName (Join-Path $root (Join-Path '.claude/commands' $_.Name))
}
Write-Host "`nInstallation complete. Restart Claude Code and Codex if the skills do not appear. Existing configuration was not overwritten." -ForegroundColor Cyan
