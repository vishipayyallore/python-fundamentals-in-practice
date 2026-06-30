param(
    [switch]$DumpOnly
)

# Run Lychee link checker in Docker. Uses lychee.toml config.
$patterns = @(
    'README.md',
    'CONTRIBUTING.md',
    'CODE_OF_CONDUCT.md',
    'SECURITY.md',
    'AGENTS.md',
    'CLAUDE.md',
    'skills.md',
    'docs/**/*.md',
    '.github/**/*.md',
    '.claude/**/*.md',
    '.cursor/rules/*.mdc',
    '.cursor/rules/README.md',
    '.clinerules/**/*.md',
    '.opencode/**/*.md'
)

if ($DumpOnly) {
    Write-Host 'Lychee (dump links only)...' -ForegroundColor Cyan
    docker run --rm -w /input -v "${PWD}:/input" lycheeverse/lychee:latest --config lychee.toml --no-progress --dump @patterns
}
else {
    Write-Host 'Lychee (validate links)...' -ForegroundColor Cyan
    docker run --rm -w /input -v "${PWD}:/input" lycheeverse/lychee:latest --config lychee.toml --no-progress @patterns
}
