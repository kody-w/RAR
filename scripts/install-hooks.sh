#!/usr/bin/env bash
# Installs the PII scrubber as a git pre-commit hook.
# Run once after cloning: bash scripts/install-hooks.sh

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
HOOK_DIR="$REPO_ROOT/.git/hooks"
HOOK_FILE="$HOOK_DIR/pre-commit"

cat > "$HOOK_FILE" << 'HOOK'
#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(git rev-parse --show-toplevel)"
SCRUBBER="$REPO_ROOT/scripts/pii_scrubber.py"
if [ ! -f "$SCRUBBER" ]; then
    echo "ERROR: PII scrubber not found at $SCRUBBER"
    exit 1
fi
echo "🔍 Running PII scrubber on staged files..."
python3 "$SCRUBBER" --staged
exit $?
HOOK

chmod +x "$HOOK_FILE"
echo "✅ Pre-commit PII scrubber hook installed at $HOOK_FILE"
