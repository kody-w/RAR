# RAR Brainstem Installer — Cloud Mode (GitHub Copilot)
# Usage: irm https://raw.githubusercontent.com/kody-w/RAR/main/scripts/install.ps1 | iex
$ErrorActionPreference = "Stop"

Write-Host ""
Write-Host "  +==========================================+" -ForegroundColor Cyan
Write-Host "  |     RAR Brainstem - Cloud Install        |" -ForegroundColor Cyan
Write-Host "  |     AI engine: GitHub Copilot            |" -ForegroundColor Cyan
Write-Host "  +==========================================+" -ForegroundColor Cyan
Write-Host ""

$BrainstemDir = "$env:USERPROFILE\.brainstem"
$Repo = "https://github.com/kody-w/CommunityRAPP.git"

# ── Python ──
Write-Host "[1/4] Checking Python..." -ForegroundColor Yellow
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "  Installing Python via winget..."
    winget install Python.Python.3.11 --accept-package-agreements --accept-source-agreements
    $env:Path = [System.Environment]::GetEnvironmentVariable("Path", "Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path", "User")
}
$pyVer = python --version 2>&1
Write-Host "  $pyVer"

# ── Git ──
Write-Host "[2/4] Checking Git..." -ForegroundColor Yellow
if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Host "  Installing Git via winget..."
    winget install Git.Git --accept-package-agreements --accept-source-agreements
    $env:Path = [System.Environment]::GetEnvironmentVariable("Path", "Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path", "User")
}
Write-Host "  Git found"

# ── GitHub CLI ──
Write-Host "[3/4] Checking GitHub CLI..." -ForegroundColor Yellow
if (-not (Get-Command gh -ErrorAction SilentlyContinue)) {
    Write-Host "  Installing GitHub CLI via winget..."
    winget install GitHub.cli --accept-package-agreements --accept-source-agreements
    $env:Path = [System.Environment]::GetEnvironmentVariable("Path", "Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path", "User")
}
Write-Host "  GitHub CLI found"

# ── Clone & Install ──
Write-Host "[4/4] Setting up Brainstem..." -ForegroundColor Yellow
New-Item -ItemType Directory -Force -Path $BrainstemDir | Out-Null

if (Test-Path "$BrainstemDir\src") {
    Write-Host "  Updating existing install..."
    Push-Location "$BrainstemDir\src"
    git pull --ff-only
    Pop-Location
} else {
    git clone $Repo "$BrainstemDir\src"
}

Push-Location "$BrainstemDir\src"
python -m venv .venv 2>$null
if (Test-Path ".venv\Scripts\Activate.ps1") { & ".venv\Scripts\Activate.ps1" }
pip install -r requirements.txt -q
Pop-Location

Write-Host ""
Write-Host "  Done! Brainstem installed at $BrainstemDir\src" -ForegroundColor Green
Write-Host ""
Write-Host "  Next steps:" -ForegroundColor Cyan
Write-Host "    1. gh auth login          # authenticate with GitHub"
Write-Host "    2. cd $BrainstemDir\src && python run.py"
Write-Host "    3. open localhost:7071    # chat with your agents"
Write-Host ""
Write-Host "  Agent Store: https://kody-w.github.io/RAR/" -ForegroundColor Blue
Write-Host ""
