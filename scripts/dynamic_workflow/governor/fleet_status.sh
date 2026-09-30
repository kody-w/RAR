#!/bin/bash
# One screen: every governed run on this machine (the RAPP engine's) and, if logged, Copilot's native one.
HERE="$(cd "$(dirname "$0")" && pwd)"
A="${RAPP_WORKFLOWS_AGENT:-$HERE/../../../agents/@kody-w/dynamic_workflow_agent.py}"
HOME_WF="${RAPP_WORKFLOWS_HOME:-$HOME/.rapp/workflows}"
NATIVE="${RAPP_WORKFLOWS_NATIVE_LOG:-$HOME_WF/governor/native-monitor.log}"
echo "== $(date '+%H:%M:%S')  load $(sysctl -n vm.loadavg 2>/dev/null | awk '{print $2}')  copilot processes: $(pgrep -f 'copilot -p' | wc -l | tr -d ' ')"
for d in $(ls -t "$HOME_WF/runs" 2>/dev/null | head -8); do
  python3 "$A" status --run-id "$d" --lines 2 | python3 -c 'import json,sys; d=json.load(sys.stdin); print("RAPP  " + d["summary"]); [print("        " + l[:150]) for l in d.get("progress", [])[-2:]]'
done
if [ -f "$NATIVE" ]; then echo "NATIVE (Copilot engine):"; tail -2 "$NATIVE" | sed 's/^/        /'; fi
