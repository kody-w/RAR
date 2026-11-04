---
name: "rar-rapp-egg-hatcher"
description: "Hatch any .egg cartridge \u2014 introspects the cartridge's schema and routes to the right destination (organism / rapplication / session / neighborhood / estate). Accepts a local file path OR a URL. Never guesses; refuses on unknown cartridge kinds. Use when the operator says 'hatch this egg', 'load this cartridge', 'open this .egg', etc."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/egg_hatcher", "rar_sha256": "7391fce3a02e8ee274332fbd71c5850495998d2e656732837b1ef104b99aef8e", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.1.1", "author": "RAPP", "tags": ["egg", "cartridge", "hatch", "organism", "rapplication", "lifecycle"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@rapp/egg_hatcher`. The original RAPP
agent is preserved byte-for-byte in `egg_hatcher_agent.py` and in the RCI capsule.

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

egg_hatcher_agent.py — universal hatcher for the .egg cartridge family.

The kernel-level agent that introspects ANY .egg cartridge and routes it
to the right destination based on what's inside. Drop into a brainstem,
restart, and the LLM gets a `HatchEgg` tool that does the right thing
without the operator having to know which kind of cartridge they're
holding.

The .egg cartridge family (per kody-w/rappterbox/carts/SCHEMA.md):

  brainstem-egg/2.2-organism       → hatch into ~/.rapp/twins/<rappid>/
  brainstem-egg/2.2-rapplication   → install as a planted rapp
  brainstem-egg/2.3-session        → mount in rappterbox console iframe
  brainstem-egg/2.3-neighborhood   → mint a new GitHub repo (planned)
  brainstem-egg/2.3-estate         → re-anchor estate on substrate (planned)

Routing is BY INTROSPECTION — the hatcher reads the cartridge's manifest
and dispatches by `schema` / `type`. Never guesses. Unknown kinds get a
clear "I don't know how to hatch this" reply, never a destructive
fallback.

How the routing works:
  1. Open file (or fetch URL) → bytes
  2. Try JSON parse first (session cartridges are bare JSON)
  3. If not JSON → try ZIP, read manifest.json
  4. Read manifest['schema'] and manifest['type']
  5. Switch and route

Sneakernet portable: the docstring IS the readme. Drop the .py into
~/.brainstem/agents/, restart, ask in chat: "hatch /path/to/file.egg"
or "hatch https://example.com/foo.egg". The LLM tool-routes to HatchEgg.

For session cartridges specifically: the hatcher CAN'T mount them itself
(no iframe in a Python brainstem) — instead it returns the URL to the
rappterbox console and a one-line instruction. The console drag-drops
the .egg in and mounts the embedded runtime.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "egg_path": {
      "description": "Local file path (e.g. /Volumes/usb/dad.egg, ~/Downloads/foo.egg) or HTTP/HTTPS URL to a .egg cartridge.",
      "type": "string"
    }
  },
  "required": [
    "egg_path"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `egg_hatcher_agent.py` and embedded as the fenced Python below (sha256 7391fce3a02e8ee2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `egg_hatcher_agent.py` first:

```bash
python3 egg_hatcher_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 egg_hatcher_agent.py   # or on stdin
python3 egg_hatcher_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@rapp/egg_hatcher_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/egg_hatcher_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@rapp/egg_hatcher/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
egg_hatcher_agent.py — universal hatcher for the .egg cartridge family.

The kernel-level agent that introspects ANY .egg cartridge and routes it
to the right destination based on what's inside. Drop into a brainstem,
restart, and the LLM gets a `HatchEgg` tool that does the right thing
without the operator having to know which kind of cartridge they're
holding.

The .egg cartridge family (per kody-w/rappterbox/carts/SCHEMA.md):

  brainstem-egg/2.2-organism       → hatch into ~/.rapp/twins/<rappid>/
  brainstem-egg/2.2-rapplication   → install as a planted rapp
  brainstem-egg/2.3-session        → mount in rappterbox console iframe
  brainstem-egg/2.3-neighborhood   → mint a new GitHub repo (planned)
  brainstem-egg/2.3-estate         → re-anchor estate on substrate (planned)

Routing is BY INTROSPECTION — the hatcher reads the cartridge's manifest
and dispatches by `schema` / `type`. Never guesses. Unknown kinds get a
clear "I don't know how to hatch this" reply, never a destructive
fallback.

How the routing works:
  1. Open file (or fetch URL) → bytes
  2. Try JSON parse first (session cartridges are bare JSON)
  3. If not JSON → try ZIP, read manifest.json
  4. Read manifest['schema'] and manifest['type']
  5. Switch and route

Sneakernet portable: the docstring IS the readme. Drop the .py into
~/.brainstem/agents/, restart, ask in chat: "hatch /path/to/file.egg"
or "hatch https://example.com/foo.egg". The LLM tool-routes to HatchEgg.

For session cartridges specifically: the hatcher CAN'T mount them itself
(no iframe in a Python brainstem) — instead it returns the URL to the
rappterbox console and a one-line instruction. The console drag-drops
the .egg in and mounts the embedded runtime.
"""

from __future__ import annotations

import io
import json
import os
import pathlib
import urllib.request
import zipfile

from agents.basic_agent import BasicAgent


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@rapp/egg_hatcher",
    "version": "1.1.1",
    "display_name": "EggHatcher",
    "description": "Introspects any .egg cartridge (local path or URL) and routes it by manifest schema/type to hatch, install, or mount; refuses unknown kinds.",
    "author": "RAPP",
    "tags": ["egg", "cartridge", "hatch", "organism", "rapplication", "lifecycle"],
    "category": "core",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    "example_call": {"args": {"egg_path": "~/Downloads/dad.egg"}},
}


RAPPTERBOX_CONSOLE_URL = "https://kody-w.github.io/rappterbox/console.html"
VBRAINSTEM_URL = "https://kody-w.github.io/RAPP/pages/vbrainstem.html"


def _read_bytes(egg_path: str) -> bytes:
    """Load egg bytes from a local path or URL. Hatcher accepts both."""
    if egg_path.startswith(("http://", "https://")):
        with urllib.request.urlopen(egg_path, timeout=30) as r:
            return r.read()
    p = pathlib.Path(os.path.expanduser(egg_path))
    if not p.exists():
        raise FileNotFoundError(f"egg not found: {egg_path}")
    return p.read_bytes()


def _introspect(blob: bytes) -> dict:
    """Sniff the egg shape: JSON-only (session) vs ZIP (organism/rapplication/etc)."""
    # Try JSON first — session cartridges are bare JSON
    try:
        text = blob.decode("utf-8")
        manifest = json.loads(text)
        if isinstance(manifest, dict) and manifest.get("schema", "").startswith("brainstem-egg/") \
                or manifest.get("schema") == "rappterbox-cart/0.1":
            return {"container": "json", "manifest": manifest}
    except (UnicodeDecodeError, json.JSONDecodeError):
        pass
    # Else try ZIP
    try:
        with zipfile.ZipFile(io.BytesIO(blob)) as z:
            with z.open("manifest.json") as f:
                manifest = json.loads(f.read().decode("utf-8"))
            return {"container": "zip", "manifest": manifest, "zip_bytes": blob}
    except (zipfile.BadZipFile, KeyError) as e:
        raise ValueError(f"egg has no recognizable manifest (not JSON, not a ZIP with manifest.json): {e}")


def _route_session(manifest: dict) -> str:
    """Session cartridges mount in rappterbox console — Python brainstem can't iframe."""
    name = manifest.get("name") or "session"
    title = manifest.get("title") or name
    rappid = manifest.get("rappid", "(no rappid)")
    runtime = manifest.get("runtime") or {}
    sha = runtime.get("sha256", "(no sha)")[:16]
    runtime_size = len(runtime.get("payload", ""))
    transcript_n = len(manifest.get("transcript") or [])
    parts = manifest.get("participants") or []
    parts_str = ", ".join(p.get("name", "?") for p in parts) or "(none)"
    return (
        f"Session cartridge identified: '{title}' ({name})\n"
        f"  rappid: {rappid}\n"
        f"  runtime: {runtime.get('type','?')} · sha256={sha}… · {runtime_size:,} bytes\n"
        f"  transcript: {transcript_n} events\n"
        f"  participants: {parts_str}\n"
        f"\n"
        f"Session cartridges run in a console (browser iframe), not in the Python brainstem.\n"
        f"To mount this cartridge:\n"
        f"  1. Open {RAPPTERBOX_CONSOLE_URL} (or {VBRAINSTEM_URL})\n"
        f"  2. Go to the 'Tether Carts' blade (rappterbox) or just drag the file onto the page\n"
        f"  3. Click 'Load .cart.json' / drop the .egg file in\n"
        f"  4. The runtime mounts in a sandboxed iframe; sha256 is verified against the manifest\n"
    )


def _route_organism(manifest: dict, blob: bytes) -> str:
    """Organism cartridges hatch into ~/.rapp/twins/<rappid>/ via utils.bond."""
    rappid = manifest.get("rappid", "(no rappid)")
    try:
        from utils.bond import hatch_organism  # type: ignore
    except ImportError:
        return (
            f"Organism cartridge identified: rappid={rappid}\n"
            f"This brainstem doesn't have utils.bond.hatch_organism available. "
            f"Run a kernel that does (rapp_brainstem v0.4+) or extract the ZIP manually:\n"
            f"  unzip the .egg into ~/.rapp/twins/<rappid>/\n"
            f"  then: bash ~/.brainstem/start.sh --port <free-port> with SOUL_PATH/AGENTS_PATH "
            f"pointed at that twin dir."
        )
    try:
        out = hatch_organism(blob)
        return f"Organism cartridge hatched. rappid={rappid}\n{out}"
    except Exception as e:
        return f"Organism hatch failed: {e}"


def _route_rapplication(manifest: dict, blob: bytes) -> str:
    """Rapplication cartridges install as a planted rapp under host brainstem."""
    rappid = manifest.get("rappid", "(no rappid)")
    try:
        from utils.bond import hatch_rapplication  # type: ignore
    except ImportError:
        return (
            f"Rapplication cartridge identified: rappid={rappid}\n"
            f"This brainstem doesn't have utils.bond.hatch_rapplication available. "
            f"Run a kernel that does (rapp_brainstem v0.4+) or extract the ZIP into "
            f"~/.brainstem/rapps/<name>/ manually."
        )
    try:
        out = hatch_rapplication(blob)
        return f"Rapplication cartridge installed. rappid={rappid}\n{out}"
    except Exception as e:
        return f"Rapplication hatch failed: {e}"


def _route_neighborhood(manifest: dict) -> str:
    """Neighborhood eggs are JOIN invites — they append the operator's two-tier
    estate's `member[]` with `{rappid, added_at, via: "egg"}` per Article XLVI.
    The egg carries the neighborhood's canonical URLs; the operator's brainstem
    fetches the full neighborhood.json from there going forward.
    """
    import datetime as _dt
    rappid = manifest.get("rappid")
    if not rappid:
        return "Neighborhood egg invalid: no rappid in manifest. Refusing to join."
    # Light format check — Article XLVI forbids fallback parsers, but the
    # real parser is in the RAPP-side tools/door_address.py; if available we
    # use it, otherwise we accept any non-empty string and let the brainstem's
    # own validator reject malformed entries on next estate rebuild.
    try:
        from door_address import door_from_rappid, InvalidRappidError  # type: ignore
        try:
            door_from_rappid(rappid)
        except InvalidRappidError as e:
            return f"Neighborhood egg invalid: malformed rappid '{rappid}' — {e}"
    except ImportError:
        pass

    name = manifest.get("display_name") or manifest.get("name") or rappid
    url = manifest.get("neighborhood_url") or ""
    nbhd_json = manifest.get("neighborhood_json") or ""
    tether = manifest.get("tether_url") or ""
    soul_summary = manifest.get("soul_summary") or ""

    # Locate the operator's two-tier estate file.
    estate_path = os.path.expanduser("~/.brainstem/estate.json")
    estate_dir = os.path.dirname(estate_path)
    try:
        os.makedirs(estate_dir, exist_ok=True)
    except Exception as e:
        return f"Could not create {estate_dir}: {e}"

    # Load existing estate or seed a minimal skeleton. The skeleton is
    # incomplete (no owner.rappid until the operator's identity is known),
    # so we don't write a skeleton unilaterally — instead we ask the operator
    # to bootstrap their estate first via `tools/rebuild_estate.py`.
    if not os.path.exists(estate_path):
        return (
            f"No estate file at {estate_path}. Bootstrap yours first:\n"
            f"  python3 tools/rebuild_estate.py --handle <your-gh> --apply\n"
            f"Then re-hatch this neighborhood egg to join {name}.\n"
        )

    try:
        estate = json.loads(pathlib.Path(estate_path).read_text())
    except Exception as e:
        return f"Couldn't read {estate_path}: {e}"

    member = estate.get("member") or []
    if not isinstance(member, list):
        return f"Estate file shape unexpected: 'member' is {type(member).__name__}, expected list."

    # Idempotent: already joined?
    if any(isinstance(m, dict) and m.get("rappid") == rappid for m in member):
        msg = f"Already a member of {name} (rappid={rappid})."
        if tether:
            msg += f"\nTether: {tether}"
        return msg

    # Append per Article XLVI: ONLY rappid + added_at + via.
    member.append({
        "rappid":   rappid,
        "added_at": _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z"),
        "via":      "egg",
    })
    estate["member"] = member
    estate["updated_at"] = _dt.datetime.now(_dt.timezone.utc).isoformat().replace("+00:00", "Z")

    try:
        pathlib.Path(estate_path).write_text(json.dumps(estate, indent=2) + "\n")
    except Exception as e:
        return f"Joined in-memory but could not write {estate_path}: {e}"

    lines = [
        f"Joined neighborhood: {name}",
        f"  rappid:    {rappid}",
    ]
    if url:
        lines.append(f"  homepage:  {url}")
    if nbhd_json:
        lines.append(f"  manifest:  {nbhd_json}")
    if tether:
        lines.append(f"  tether:    {tether}  ← go here to chat with the neighborhood")
    if soul_summary:
        lines.append("")
        lines.append(f"  {soul_summary}")
    lines.append("")
    lines.append(f"Wrote {estate_path}. Total memberships: {len(member)}.")
    return "\n".join(lines)


def _route_estate(manifest: dict) -> str:
    """Estate cartridges re-anchor on a new substrate. Planned — not yet wired."""
    rappid = manifest.get("rappid", "(no rappid)")
    return (
        f"Estate cartridge identified: rappid={rappid}\n"
        f"Estate hatching is on the v0.4 roadmap (kody-w/rappterbox/carts/SCHEMA.md).\n"
        f"Estate eggs carry the operator's whole multi-tier identity (public discovery + "
        f"private bones pointer + sealed PII pointer) for substrate migration "
        f"(GitHub → GitLab, GitHub → Codeberg, etc.).\n"
        f"For now, manual migration: see PUBLIC_PRIVATE_BOUNDARY.md §1.6 override paths."
    )


def _route_unknown(manifest: dict) -> str:
    schema = manifest.get("schema", "(unknown)")
    kind = manifest.get("type", "(no type)")
    return (
        f"Unknown egg cartridge: schema='{schema}' type='{kind}'.\n"
        f"This hatcher knows: organism, rapplication, session, neighborhood.\n"
        f"Planned: estate.\n"
        f"See kody-w/rappterbox/carts/SCHEMA.md for the cartridge family.\n"
        f"NOT routing — refusing to guess. Operator action required."
    )


class EggHatcherAgent(BasicAgent):
    def __init__(self):
        self.name = "HatchEgg"
        self.metadata = {
            "name": self.name,
            "description": (
                "Hatch any .egg cartridge — introspects the cartridge's schema and routes "
                "to the right destination (organism / rapplication / session / neighborhood "
                "/ estate). Accepts a local file path OR a URL. Never guesses; refuses on "
                "unknown cartridge kinds. Use when the operator says 'hatch this egg', "
                "'load this cartridge', 'open this .egg', etc."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "egg_path": {
                        "type": "string",
                        "description": (
                            "Local file path (e.g. /Volumes/usb/dad.egg, ~/Downloads/foo.egg) "
                            "or HTTP/HTTPS URL to a .egg cartridge."
                        ),
                    },
                },
                "required": ["egg_path"],
            },
        }
        super().__init__(self.name, self.metadata)

    def perform(self, **kwargs) -> str:
        egg_path = kwargs.get("egg_path", "").strip()
        if not egg_path:
            return "egg_path is required (local file or URL)"
        try:
            blob = _read_bytes(egg_path)
        except Exception as e:
            return f"Couldn't read egg: {e}"
        try:
            info = _introspect(blob)
        except Exception as e:
            return f"Couldn't introspect egg: {e}"
        manifest = info["manifest"]
        schema = manifest.get("schema", "")
        kind = manifest.get("type", "")
        # Session cartridges: schema is brainstem-egg/2.3-session OR legacy rappterbox-cart/0.1
        if schema in ("brainstem-egg/2.3-session", "rappterbox-cart/0.1") or kind == "session":
            return _route_session(manifest)
        if "organism" in schema or kind == "organism":
            return _route_organism(manifest, blob)
        if "rapplication" in schema or kind == "rapplication":
            return _route_rapplication(manifest, blob)
        if "neighborhood" in schema or kind == "neighborhood":
            return _route_neighborhood(manifest)
        if "estate" in schema or kind == "estate":
            return _route_estate(manifest)
        return _route_unknown(manifest)
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
