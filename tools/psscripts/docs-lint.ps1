param(
    [switch]$Fix
)

# Run markdownlint-cli2 across repo docs. Use --fix if -Fix is supplied.
$patterns = @(
    'README.md',
    'AGENTS.md',
    'CLAUDE.md',
    'skills.md',
    'docs/**/*.md',
    '.github/**/*.md',
    '.claude/**/*.md',
    '.cursor/rules/README.md'
)

$args = @()
if ($Fix) {
    $args += '--fix'
}
$args += $patterns

Write-Host 'Running markdownlint-cli2...' -ForegroundColor Cyan
npx --yes markdownlint-cli2 @args
