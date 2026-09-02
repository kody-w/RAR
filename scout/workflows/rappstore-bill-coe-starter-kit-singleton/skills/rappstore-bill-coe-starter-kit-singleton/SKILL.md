---
name: "rappstore-bill-coe-starter-kit-singleton"
description: "One-shot onboarding for Bill Whalen's Agent Team (BWAT) neighborhood. Fetches Bill's team's 5 workflow agents over plain HTTPS (no auth), sha256-verifies each against the published manifest, installs them into your local agents/ directory, records the subscription, and returns a friendly Bill-voice orientation. After running, your brainstem has OutcomeFramer / Intake / OutcomeValidator / PM / BillTwin all callable. Use this when a solution engineer in the field wants to be set up for BWAT in one move. Default dry_run=False."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@bill/coe-starter-kit-singleton", "rar_sha256": "50a04db67238b2bedd3817fa3ab4225032fb050531671b5dde126881efac4fbe", "source_kind": "federated-rapplication", "source_commit": null, "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "coe_starter_kit_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@bill/coe-starter-kit-singleton:2bcdf05bb883c499cf5272990009814460d0138b301fac5af893029d1df68e64", "kind": "skill"}}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@bill/coe-starter-kit-singleton`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `coe_starter_kit_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
