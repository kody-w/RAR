#!/usr/bin/env bash
# RAR Brainstem Installer — Local-First Mode (Ollama + Gemma 4)
# Usage: curl -fsSL https://raw.githubusercontent.com/kody-w/RAR/main/scripts/install_local.sh | bash
# No cloud. No API keys. No data leaves your machine.
set -euo pipefail

BRAINSTEM_DIR="$HOME/.brainstem"
REPO="https://github.com/kody-w/CommunityRAPP.git"
MODEL="${RAR_MODEL:-gemma4}"

echo ""
echo "  ╔══════════════════════════════════════════╗"
echo "  ║     RAR Brainstem — Local-First Install  ║"
echo "  ║     AI engine: Ollama + Gemma 4          ║"
echo "  ║     No cloud. No API keys.               ║"
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

# ── Ollama ──
if command -v ollama &>/dev/null; then
  OLLAMA_VER="$(ollama --version 2>/dev/null || echo 'installed')"
  echo "[2/5] Ollama found ($OLLAMA_VER)"
else
  echo "[2/5] Installing Ollama..."
  curl -fsSL https://ollama.com/install.sh | sh
fi

# ── Pull model ──
echo "[3/5] Pulling $MODEL (this may take a few minutes on first run)..."
ollama pull "$MODEL"

# ── Python ──
if command -v python3 &>/dev/null; then
  PY_VER="$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"
  echo "[4/5] Python $PY_VER found"
else
  echo "[4/5] Installing Python..."
  if [ "$PLATFORM" = "mac" ]; then
    if command -v brew &>/dev/null; then
      brew install python@3.11
    else
      /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
      brew install python@3.11
    fi
  else
    sudo apt-get update -qq && sudo apt-get install -y python3.11 python3.11-venv python3-pip 2>/dev/null || \
    sudo dnf install -y python3.11
  fi
fi

# ── Clone & Install Brainstem ──
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

# ── Configure for Ollama ──
ENV_FILE="$BRAINSTEM_DIR/src/.env"
if [ ! -f "$ENV_FILE" ] && [ -f "$BRAINSTEM_DIR/src/.env.example" ]; then
  cp "$BRAINSTEM_DIR/src/.env.example" "$ENV_FILE"
fi
# Set Ollama as the AI provider
if [ -f "$ENV_FILE" ]; then
  if grep -q "OLLAMA_HOST" "$ENV_FILE" 2>/dev/null; then
    sed -i.bak "s|^#*OLLAMA_HOST=.*|OLLAMA_HOST=http://localhost:11434|" "$ENV_FILE"
  else
    echo "" >> "$ENV_FILE"
    echo "# Local-first AI via Ollama" >> "$ENV_FILE"
    echo "OLLAMA_HOST=http://localhost:11434" >> "$ENV_FILE"
    echo "OLLAMA_MODEL=$MODEL" >> "$ENV_FILE"
  fi
fi

# ── Shell aliases ──
SHELL_RC="$HOME/.bashrc"
[ -f "$HOME/.zshrc" ] && SHELL_RC="$HOME/.zshrc"
if ! grep -q "brainstem" "$SHELL_RC" 2>/dev/null; then
  echo "" >> "$SHELL_RC"
  echo "# RAR Brainstem (local-first)" >> "$SHELL_RC"
  echo "alias brainstem='cd $BRAINSTEM_DIR/src && python3 run.py'" >> "$SHELL_RC"
  echo "  Added 'brainstem' alias to $SHELL_RC"
fi

echo ""
echo "  ✓ Brainstem installed at $BRAINSTEM_DIR/src"
echo "  ✓ Ollama running with $MODEL"
echo ""
echo "  Next steps:"
echo "    1. ollama serve            # start Ollama (if not running)"
echo "    2. brainstem               # start the agent server"
echo "    3. open localhost:7071     # chat with your agents"
echo ""
echo "  No cloud. No API keys. Everything runs on this machine."
echo "  Open the Agent Store: https://kody-w.github.io/RAR/"
echo ""
echo "  Change model: RAR_MODEL=gemma4:26b bash install_local.sh"
echo ""
