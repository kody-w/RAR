# RAR Brainstem Installer — Local-First Mode (Ollama + Gemma 4)
# Usage: irm https://raw.githubusercontent.com/kody-w/RAR/main/scripts/install_local.ps1 | iex
# No cloud. No API keys. No data leaves your machine.
$ErrorActionPreference = "Stop"

Write-Host ""
Write-Host "  +==========================================+" -ForegroundColor Green
Write-Host "  |     RAR Brainstem - Local-First Install  |" -ForegroundColor Green
Write-Host "  |     AI engine: Ollama + Gemma 4          |" -ForegroundColor Green
Write-Host "  |     No cloud. No API keys.               |" -ForegroundColor Green
Write-Host "  +==========================================+" -ForegroundColor Green
Write-Host ""

$BrainstemDir = "$env:USERPROFILE\.brainstem"
$Repo = "https://github.com/kody-w/CommunityRAPP.git"
$Model = if ($env:RAR_MODEL) { $env:RAR_MODEL } else { "gemma4" }

# ── Ollama ──
Write-Host "[1/5] Checking Ollama..." -ForegroundColor Yellow
if (-not (Get-Command ollama -ErrorAction SilentlyContinue)) {
    Write-Host "  Installing Ollama via winget..."
    winget install Ollama.Ollama --accept-package-agreements --accept-source-agreements
    $env:Path = [System.Environment]::GetEnvironmentVariable("Path", "Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path", "User")
}
Write-Host "  Ollama found"

# ── Pull model ──
Write-Host "[2/5] Pulling $Model (this may take a few minutes)..." -ForegroundColor Yellow
ollama pull $Model

# ── Python ──
Write-Host "[3/5] Checking Python..." -ForegroundColor Yellow
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "  Installing Python via winget..."
    winget install Python.Python.3.11 --accept-package-agreements --accept-source-agreements
    $env:Path = [System.Environment]::GetEnvironmentVariable("Path", "Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path", "User")
}
$pyVer = python --version 2>&1
Write-Host "  $pyVer"

# ── Git ──
Write-Host "[4/5] Checking Git..." -ForegroundColor Yellow
if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    winget install Git.Git --accept-package-agreements --accept-source-agreements
    $env:Path = [System.Environment]::GetEnvironmentVariable("Path", "Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path", "User")
}
Write-Host "  Git found"

# ── Clone & Install ──
Write-Host "[5/5] Setting up Brainstem..." -ForegroundColor Yellow
New-Item -ItemType Directory -Force -Path $BrainstemDir | Out-Null

if (Test-Path "$BrainstemDir\src") {
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

# Configure Ollama
if (-not (Test-Path ".env") -and (Test-Path ".env.example")) {
    Copy-Item ".env.example" ".env"
}
if (Test-Path ".env") {
    Add-Content ".env" "`nOLLAMA_HOST=http://localhost:11434`nOLLAMA_MODEL=$Model"
}
Pop-Location

Write-Host ""
Write-Host "  Done! Brainstem installed with local AI." -ForegroundColor Green
Write-Host "  Ollama running with $Model" -ForegroundColor Green
Write-Host ""
Write-Host "  Next steps:" -ForegroundColor Cyan
Write-Host "    1. ollama serve            # start Ollama (if not running)"
Write-Host "    2. cd $BrainstemDir\src && python run.py"
Write-Host "    3. open localhost:7071     # chat with your agents"
Write-Host ""
Write-Host "  No cloud. No API keys. Everything runs on this machine." -ForegroundColor Green
Write-Host "  Agent Store: https://kody-w.github.io/RAR/" -ForegroundColor Blue
Write-Host ""
