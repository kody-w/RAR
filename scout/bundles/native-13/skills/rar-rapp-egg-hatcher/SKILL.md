---
name: "rar-rapp-egg-hatcher"
description: "Hatch any .egg cartridge \u2014 introspects the cartridge's schema and routes to the right destination (organism / rapplication / session / neighborhood / estate). Accepts a local file path OR a URL. Never guesses; refuses on unknown cartridge kinds. Use when the operator says 'hatch this egg', 'load this cartridge', 'open this .egg', etc."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/egg_hatcher", "rar_sha256": "bba2848c59de6883ad0f3d190ff0fe4e9f44f595016c95f4453d2764d3f4e78f", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.1.1", "author": "RAPP", "tags": ["egg", "cartridge", "hatch", "organism", "rapplication", "lifecycle"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `egg_hatcher_agent.py` and embedded as the fenced Python below (sha256 bba2848c59de6883…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `egg_hatcher_agent.py` first:

```bash
python3 egg_hatcher_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 egg_hatcher_agent.py   # or on stdin
python3 egg_hatcher_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
