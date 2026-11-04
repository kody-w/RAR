---
name: "rar-rapp-egg-hatcher"
description: "Hatch any .egg cartridge \u2014 introspects the cartridge's schema and routes to the right destination (organism / rapplication / session / neighborhood / estate). Accepts a local file path OR a URL. Never guesses; refuses on unknown cartridge kinds. Use when the operator says 'hatch this egg', 'load this cartridge', 'open this .egg', etc."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/egg_hatcher", "rar_sha256": "7391fce3a02e8ee274332fbd71c5850495998d2e656732837b1ef104b99aef8e", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.1.1", "author": "RAPP", "tags": ["egg", "cartridge", "hatch", "organism", "rapplication", "lifecycle"]}
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
