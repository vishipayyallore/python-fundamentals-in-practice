param(
    [string]$Path = ".",
    [int]$Depth = 5,
    [string]$OutFile = "",
    [string[]]$Exclude = @(".git", ".venv", "bin", "obj", "__pycache__", ".vs", ".cache", "node_modules")
)

function Show-Tree($folder, $prefix = "", $depth = 0, $maxDepth = 5, $excludePatterns) {
    if ($depth -ge $maxDepth) { return }

    $items = Get-ChildItem -Path $folder -Force | Sort-Object PSIsContainer, Name

    # Apply exclude filter
    $items = $items | Where-Object {
        $skip = $false
        foreach ($pattern in $excludePatterns) {
            if ($_.Name -like $pattern) { $skip = $true; break }
        }
        -not $skip
    }

    for ($i = 0; $i -lt $items.Count; $i++) {
        $item = $items[$i]
        $isLast = ($i -eq $items.Count - 1)

        if ($isLast) {
            Write-Output "$prefix└── $($item.Name)"
            $newPrefix = "$prefix    "
        }
        else {
            Write-Output "$prefix├── $($item.Name)"
            $newPrefix = "$prefix│   "
        }

        if ($item.PSIsContainer) {
            Show-Tree -folder $item.FullName -prefix $newPrefix -depth ($depth + 1) -maxDepth $maxDepth -excludePatterns $excludePatterns
        }
    }
}

# Run the tree
$tree = Show-Tree -folder $Path -maxDepth $Depth -excludePatterns $Exclude

# Output to console or file
if ($OutFile -ne "") {
    Show-Tree -folder $Path -maxDepth $Depth -excludePatterns $Exclude | Out-File $OutFile -Encoding utf8
    Write-Host "Folder structure saved to $OutFile"
}
else {
    Show-Tree -folder $Path -maxDepth $Depth -excludePatterns $Exclude
}
