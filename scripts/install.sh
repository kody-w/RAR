#!/usr/bin/env bash
# RAR Brainstem Installer — Cloud Mode (GitHub Copilot)
# Usage: curl -fsSL https://raw.githubusercontent.com/kody-w/RAR/main/scripts/install.sh | bash
set -euo pipefail

BRAINSTEM_DIR="$HOME/.brainstem"
REPO="https://github.com/kody-w/CommunityRAPP.git"
REQUIRED_PYTHON="3.11"

echo ""
echo "  ╔══════════════════════════════════════════╗"
echo "  ║     RAR Brainstem — Cloud Install        ║"
echo "  ║     AI engine: GitHub Copilot            ║"
echo "  ╚══════════════════════════════════════════╝"
echo ""

# ── Check OS ──
OS="$(uname -s)"
case "$OS" in
  Linux*)  PLATFORM="linux" ;;
  Darwin*) PLATFORM="mac" ;;
  *)       echo "Unsupported OS: $OS"; exit 1 ;;
esac
echo "[1/5] Platform: $PLATFORM"

# ── Python ──
install_python() {
  echo "[2/5] Python $REQUIRED_PYTHON not found. Installing..."
  if [ "$PLATFORM" = "mac" ]; then
    if command -v brew &>/dev/null; then
      brew install python@3.11
    else
      echo "  Installing Homebrew first..."
      /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
      brew install python@3.11
    fi
  else
    if command -v apt-get &>/dev/null; then
      sudo apt-get update -qq && sudo apt-get install -y python3.11 python3.11-venv python3-pip
    elif command -v dnf &>/dev/null; then
      sudo dnf install -y python3.11
    else
      echo "  Could not auto-install Python. Please install Python $REQUIRED_PYTHON+ manually."
      exit 1
    fi
  fi
}

if command -v python3 &>/dev/null; then
  PY_VER="$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"
  echo "[2/5] Python $PY_VER found"
  if [ "$(echo "$PY_VER < $REQUIRED_PYTHON" | bc -l 2>/dev/null || echo 0)" = "1" ]; then
    install_python
  fi
else
  install_python
fi

# ── Git ──
if ! command -v git &>/dev/null; then
  echo "[3/5] Installing git..."
  if [ "$PLATFORM" = "mac" ]; then
    xcode-select --install 2>/dev/null || true
  else
    sudo apt-get install -y git 2>/dev/null || sudo dnf install -y git
  fi
else
  echo "[3/5] Git found"
fi

# ── GitHub CLI ──
if ! command -v gh &>/dev/null; then
  echo "[4/5] Installing GitHub CLI..."
  if [ "$PLATFORM" = "mac" ]; then
    brew install gh
  else
    curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
    sudo apt-get update -qq && sudo apt-get install -y gh
  fi
else
  echo "[4/5] GitHub CLI found"
fi

# ── Clone & Install ──
echo "[5/5] Setting up Brainstem..."
mkdir -p "$BRAINSTEM_DIR"

if [ -d "$BRAINSTEM_DIR/src" ]; then
  echo "  Updating existing install..."
  cd "$BRAINSTEM_DIR/src" && git pull --ff-only
else
  git clone "$REPO" "$BRAINSTEM_DIR/src"
fi

cd "$BRAINSTEM_DIR/src"
python3 -m venv .venv 2>/dev/null || true
source .venv/bin/activate 2>/dev/null || true
pip3 install -r requirements.txt -q 2>/dev/null || pip install -r requirements.txt -q

# ── Shell alias ──
SHELL_RC="$HOME/.bashrc"
[ -f "$HOME/.zshrc" ] && SHELL_RC="$HOME/.zshrc"
if ! grep -q "brainstem" "$SHELL_RC" 2>/dev/null; then
  echo "" >> "$SHELL_RC"
  echo "# RAR Brainstem" >> "$SHELL_RC"
  echo "alias brainstem='cd $BRAINSTEM_DIR/src && python3 run.py'" >> "$SHELL_RC"
  echo "  Added 'brainstem' alias to $SHELL_RC"
fi

echo ""
echo "  ✓ Brainstem installed at $BRAINSTEM_DIR/src"
echo ""
echo "  Next steps:"
echo "    1. gh auth login          # authenticate with GitHub"
echo "    2. brainstem              # start the agent server"
echo "    3. open localhost:7071    # chat with your agents"
echo ""
echo "  Or open the Agent Store: https://kody-w.github.io/RAR/"
echo ""
