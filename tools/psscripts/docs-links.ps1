param(
    [switch]$DumpOnly
)

# Run Lychee link checker in Docker. Uses lychee.toml config.
$patterns = @(
    'README.md',
    'docs/**/*.md',
    '.github/**/*.md'
)

if ($DumpOnly) {
    Write-Host 'Lychee (dump links only)...' -ForegroundColor Cyan
    docker run --rm -w /input -v "${PWD}:/input" lycheeverse/lychee:latest --config lychee.toml --no-progress --dump @patterns
}
else {
    Write-Host 'Lychee (validate links)...' -ForegroundColor Cyan
    docker run --rm -w /input -v "${PWD}:/input" lycheeverse/lychee:latest --config lychee.toml --no-progress @patterns
}
