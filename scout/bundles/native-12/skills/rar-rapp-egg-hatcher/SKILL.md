---
name: "rar-rapp-egg-hatcher"
description: "Hatch any .egg cartridge \u2014 introspects the cartridge's schema and routes to the right destination (organism / rapplication / session / neighborhood / estate). Accepts a local file path OR a URL. Never guesses; refuses on unknown cartridge kinds. Use when the operator says 'hatch this egg', 'load this cartridge', 'open this .egg', etc."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/egg_hatcher", "rar_sha256": "bba2848c59de6883ad0f3d190ff0fe4e9f44f595016c95f4453d2764d3f4e78f", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "egg_hatcher_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@rapp/egg-hatcher:f95763924a0732ac22a4ca9128b5270be8ee82e6cd4ba96c939d04d5736c4f7f", "kind": "skill"}, "version": "1.1.1", "author": "RAPP", "tags": ["egg", "cartridge", "hatch", "organism", "rapplication", "lifecycle"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@rapp/egg_hatcher`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `egg_hatcher_agent.py` is
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
