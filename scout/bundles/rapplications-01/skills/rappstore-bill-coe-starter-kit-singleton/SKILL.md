---
name: "rappstore-bill-coe-starter-kit-singleton"
description: "One-shot onboarding for Bill Whalen's Agent Team (BWAT) neighborhood. Fetches Bill's team's 5 workflow agents over plain HTTPS (no auth), sha256-verifies each against the published manifest, installs them into your local agents/ directory, records the subscription, and returns a friendly Bill-voice orientation. After running, your brainstem has OutcomeFramer / Intake / OutcomeValidator / PM / BillTwin all callable. Use this when a solution engineer in the field wants to be set up for BWAT in one move. Default dry_run=False."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@bill/coe-starter-kit-singleton", "rar_sha256": "50a04db67238b2bedd3817fa3ab4225032fb050531671b5dde126881efac4fbe", "source_kind": "federated-rapplication", "source_commit": null}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@bill/coe-starter-kit-singleton`. The original RAPP
agent is preserved byte-for-byte in `coe_starter_kit_agent.py` and in the RCI capsule.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the linked
agent SHA-256 before importing it. If preflight reports a host dependency that
Scout cannot satisfy, use the `brainstem_chat` MCP tool to run the canonical
agent in the user's Brainstem. Never paraphrase the factory or agent into a new
implementation. The generic direct-file commands in the generated Toaster
section are recovery guidance; Scout should prefer the verified runner.

bill_team_starter_agent — the one-file BWAT onboarding agent.

Drop this file into your local brainstem's `agents/` directory. The
brainstem hot-reloads agents on every request, so on your next chat
turn the new agent is callable. Then say something like:

    "set me up for Bill's team"
    "join Bill Whalen's neighborhood"
    "run the bill team starter"

…and this agent will:

  1. Fetch Bill Whalen's Agent Team neighborhood manifest
     (https://github.com/kody-w/billwhalen-agent-team/blob/main/rar/index.json)
  2. Pull each listed agent over plain HTTPS (no auth required).
  3. Verify each against the manifest's sha256 — refuse on mismatch.
  4. Write them into your local agents/ directory, sha256-pinned.
  5. Record the join at ~/.brainstem/neighborhoods.json.
  6. Hand you back a friendly orientation in Bill's voice.

Self-contained. Stdlib only. Works on any RAPP brainstem with
internet access to github.com.

After this agent runs you'll have 5 new agents loaded:
  • BwatOutcomeFramer  — frame the outcome before any build work
  • BwatIntake         — log raw ideas + solutions to local backlog
  • BwatOutcomeValidator — verify delivery before any close
  • BwatPm             — sprint planning + status reports
  • BillTwin           — Bill's digital twin; walks you through the flow

No additional setup. No cloud. Works in a basement at a customer
site with no wifi (after this initial fetch).

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "dry_run": {
      "default": false,
      "description": "If true, fetches the manifest + verifies but does NOT write any files. Useful for inspection.",
      "type": "boolean"
    }
  },
  "required": [],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `coe_starter_kit_agent.py` and embedded as the fenced Python below (sha256 50a04db67238b2be…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `coe_starter_kit_agent.py` first:

```bash
python3 coe_starter_kit_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 coe_starter_kit_agent.py   # or on stdin
python3 coe_starter_kit_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""bill_team_starter_agent — the one-file BWAT onboarding agent.

Drop this file into your local brainstem's `agents/` directory. The
brainstem hot-reloads agents on every request, so on your next chat
turn the new agent is callable. Then say something like:

    "set me up for Bill's team"
    "join Bill Whalen's neighborhood"
    "run the bill team starter"

…and this agent will:

  1. Fetch Bill Whalen's Agent Team neighborhood manifest
     (https://github.com/kody-w/billwhalen-agent-team/blob/main/rar/index.json)
  2. Pull each listed agent over plain HTTPS (no auth required).
  3. Verify each against the manifest's sha256 — refuse on mismatch.
  4. Write them into your local agents/ directory, sha256-pinned.
  5. Record the join at ~/.brainstem/neighborhoods.json.
  6. Hand you back a friendly orientation in Bill's voice.

Self-contained. Stdlib only. Works on any RAPP brainstem with
internet access to github.com.

After this agent runs you'll have 5 new agents loaded:
  • BwatOutcomeFramer  — frame the outcome before any build work
  • BwatIntake         — log raw ideas + solutions to local backlog
  • BwatOutcomeValidator — verify delivery before any close
  • BwatPm             — sprint planning + status reports
  • BillTwin           — Bill's digital twin; walks you through the flow

No additional setup. No cloud. Works in a basement at a customer
site with no wifi (after this initial fetch).
"""

from __future__ import annotations

import hashlib
import json
import os
import urllib.request
from datetime import datetime, timezone

try:
    from agents.basic_agent import BasicAgent
except ImportError:
    from basic_agent import BasicAgent


_GATE_REPO = "kody-w/billwhalen-agent-team"
_RAR_URL = (
    f"https://raw.githubusercontent.com/{_GATE_REPO}/main/rar/index.json"
)


def _now_iso() -> str:
    return (
        datetime.now(timezone.utc)
        .isoformat(timespec="seconds")
        .replace("+00:00", "Z")
    )


def _agents_dir() -> str:
    """Where to install the fetched agents.

    Honours $AGENTS_PATH if set (the brainstem sets this); otherwise
    falls back to the directory this file lives in (which is the
    brainstem's agents/ dir if you dropped this file there).
    """
    explicit = os.environ.get("AGENTS_PATH")
    if explicit:
        return explicit
    return os.path.dirname(os.path.abspath(__file__))


def _brainstem_home() -> str:
    return os.path.expanduser(os.environ.get("BRAINSTEM_HOME", "~/.brainstem"))


def _http_get(url: str, timeout: int = 20) -> bytes | None:
    try:
        req = urllib.request.Request(
            url, headers={"User-Agent": "bwat-starter/1.0"}
        )
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read()
    except Exception:
        return None


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _record_subscription(home: str, gate_repo: str, nb_rappid: str,
                          display: str) -> bool:
    os.makedirs(home, exist_ok=True)
    path = os.path.join(home, "neighborhoods.json")
    data: dict = {"schema": "rapp-neighborhood-subscriptions/1.0",
                  "subscribed": []}
    if os.path.exists(path):
        try:
            data = json.load(open(path))
        except Exception:
            pass
    subs = data.get("subscribed", [])
    if any(s.get("gate_repo") == gate_repo for s in subs):
        return False
    subs.append({
        "gate_repo": gate_repo,
        "neighborhood_rappid": nb_rappid,
        "display_name": display,
        "joined_at": _now_iso(),
    })
    data["subscribed"] = subs
    data["updated_at"] = _now_iso()
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    return True


_BILL_VOICE = (
    "Hey — welcome to BWAT. I'm a twin of Bill Whalen, here to help you "
    "get useful before you get clever. Three rules:\n"
    "  1. Outcome before build. If you can't say what success looks like "
    "in one sentence, ask BwatOutcomeFramer first.\n"
    "  2. Log everything. Even half-formed ideas. BwatIntake is your "
    "friend; you cannot have too much in the backlog.\n"
    "  3. Nothing closes without OutcomeValidator's say-so.\n\n"
    "Stuck? Ask `BillTwin next_move` — the twin reads your local "
    "backlog and tells you what I'd do next."
)


class BillTeamStarterAgent(BasicAgent):
    metadata = {
        "name": "BillTeamStarter",
        "description": (
            "One-shot onboarding for Bill Whalen's Agent Team (BWAT) "
            "neighborhood. Fetches Bill's team's 5 workflow agents over "
            "plain HTTPS (no auth), sha256-verifies each against the "
            "published manifest, installs them into your local agents/ "
            "directory, records the subscription, and returns a friendly "
            "Bill-voice orientation. After running, your brainstem has "
            "OutcomeFramer / Intake / OutcomeValidator / PM / BillTwin "
            "all callable. Use this when a solution engineer in the field "
            "wants to be set up for BWAT in one move. Default dry_run=False."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "dry_run": {
                    "type": "boolean",
                    "default": False,
                    "description": (
                        "If true, fetches the manifest + verifies but "
                        "does NOT write any files. Useful for inspection."
                    ),
                },
            },
            "required": [],
        },
    }

    def __init__(self):
        self.name = "BillTeamStarter"

    def perform(self, **kwargs) -> str:
        dry_run = bool(kwargs.get("dry_run", False))

        # 1. Fetch the manifest.
        rar_bytes = _http_get(_RAR_URL)
        if rar_bytes is None:
            return json.dumps({
                "ok": False,
                "error": (
                    f"Couldn't fetch {_RAR_URL}. Check your internet, then "
                    "try again. (Once you've installed the agents once, "
                    "they live locally and run offline.)"
                ),
            })
        try:
            rar = json.loads(rar_bytes.decode())
        except Exception as e:
            return json.dumps({
                "ok": False, "error": f"Manifest unparseable: {e}"
            })
        if rar.get("schema") != "rapp-rar-index/1.0":
            return json.dumps({
                "ok": False,
                "error": (
                    f"Manifest is wrong schema "
                    f"({rar.get('schema')!r}); refusing to install."
                ),
            })

        items = rar.get("required_for_participation") or []
        if not items:
            return json.dumps({
                "ok": False,
                "error": (
                    "Manifest has no required agents to install. The "
                    "neighborhood looks empty — try again later or "
                    "check https://github.com/kody-w/billwhalen-agent-team."
                ),
            })

        # 2-4. Fetch + verify + install each agent.
        target_dir = _agents_dir()
        installed: list[dict] = []
        verified_only: list[dict] = []
        errors: list[dict] = []
        for item in items:
            name = item.get("name") or item.get("file") or "<unknown>"
            raw_url = item.get("raw_url")
            expected = (item.get("sha256") or "").lower()
            file_rel = item.get("file") or f"agents/{name}.py"
            base = os.path.basename(file_rel)
            if not (raw_url and expected):
                errors.append({"name": name,
                               "error": "manifest entry missing raw_url or sha256"})
                continue
            body = _http_get(raw_url)
            if body is None:
                errors.append({"name": name, "error": f"couldn't fetch {raw_url}"})
                continue
            actual = _sha256(body)
            if actual != expected:
                errors.append({
                    "name": name,
                    "error": (
                        f"sha256 mismatch (manifest says {expected[:12]}…, "
                        f"got {actual[:12]}…) — refusing to install"
                    ),
                })
                continue

            if dry_run:
                verified_only.append({"name": name, "file": base,
                                       "sha256": actual, "size": len(body)})
                continue

            try:
                os.makedirs(target_dir, exist_ok=True)
                target_path = os.path.join(target_dir, base)
                with open(target_path, "wb") as f:
                    f.write(body)
                installed.append({"name": name, "file": base,
                                   "path": target_path,
                                   "sha256": actual, "size": len(body)})
            except Exception as e:
                errors.append({"name": name,
                               "error": f"write failed: {e}"})

        # 5. Record subscription (skip on dry_run).
        nb_rappid = (rar.get("rar_for")
                     and f"see neighborhood.json at {_GATE_REPO}") or ""
        # Pull the actual rappid from neighborhood.json for an honest record
        nb_meta_bytes = _http_get(
            f"https://raw.githubusercontent.com/{_GATE_REPO}/main/neighborhood.json"
        )
        nb_display = "Bill Whalen's Agent Team"
        if nb_meta_bytes:
            try:
                nb_meta = json.loads(nb_meta_bytes.decode())
                nb_rappid = (nb_meta.get("neighborhood_rappid")
                             or nb_meta.get("rappid")
                             or nb_rappid)
                nb_display = nb_meta.get("display_name") or nb_display
            except Exception:
                pass

        subscription_added = False
        if not dry_run and not errors:
            subscription_added = _record_subscription(
                _brainstem_home(), _GATE_REPO, nb_rappid, nb_display)

        # 6. Return orientation.
        next_step = (
            "Ask your brainstem `BillTwin intro` on the next turn — the "
            "twin will personally walk you through the workflow."
            if installed and not errors else
            "Inspection complete. Re-run with dry_run=False to install."
            if dry_run else
            "Some installs failed — see the errors list. Fix the underlying "
            "issue (network, disk write permissions) and re-run."
        )

        return json.dumps({
            "schema": "bwat-starter-result/1.0",
            "ok": not errors,
            "dry_run": dry_run,
            "gate_repo": _GATE_REPO,
            "neighborhood_rappid": nb_rappid,
            "neighborhood_name": nb_display,
            "agents_dir": target_dir,
            "installed": installed,
            "verified_only": verified_only,
            "errors": errors,
            "subscription_added": subscription_added,
            "bill_says": _BILL_VOICE,
            "next_step": next_step,
        }, indent=2)
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
