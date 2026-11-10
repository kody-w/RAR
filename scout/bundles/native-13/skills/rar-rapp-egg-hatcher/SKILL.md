---
name: "rar-rapp-egg-hatcher"
description: "Hatch any .egg cartridge \u2014 introspects the cartridge's schema and routes to the right destination (organism / rapplication / session / neighborhood / estate). Accepts a local file path OR a URL. Never guesses; refuses on unknown cartridge kinds. Use when the operator says 'hatch this egg', 'load this cartridge', 'open this .egg', etc."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/egg_hatcher", "rar_sha256": "ff966a1f1d4990900f4cc038a32fb2c94d1b92b5c8a2b691c76e5aa062e5cd29", "source_kind": "rar-agent", "source_commit": "484a10cb2d3d421f88727b762634e9dd41a11fb2", "version": "1.2.0", "author": "RAPP", "tags": ["egg", "cartridge", "hatch", "organism", "rapplication", "lifecycle"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `egg_hatcher_agent.py` and embedded as the fenced Python below (sha256 ff966a1f1d499090…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `egg_hatcher_agent.py` first:

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

import hashlib
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
    "version": "1.2.0",
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


RAPP1_EGG = "rapp/1-egg"


def _rapp1_files(manifest: dict, blob: bytes) -> dict:
    """Every file a rapp/1 egg lists, each checked against its hash. Any mismatch refuses the whole egg."""
    files = {}
    with zipfile.ZipFile(io.BytesIO(blob)) as z:
        names = set(z.namelist())
        for item in manifest.get("contents") or []:
            path, want = item["path"], item["hash"]
            if path not in names:
                raise ValueError(f"the egg lists {path} but does not carry it")
            octets = z.read(path)
            if hashlib.sha256(b"rapp/1:egg\n" + octets).hexdigest() != want:
                raise ValueError(f"{path} does not match the hash on the egg's label")
            files[path] = octets
    return files


def _twin_home(rappid: str) -> pathlib.Path:
    return pathlib.Path(os.path.expanduser("~/.rapp/twins")) / rappid.rsplit(":", 1)[-1]


def _route_rapp1(manifest: dict, blob: bytes, variant: str) -> str:
    """rapp/1 eggs: check every file, then hatch by `variant`. Never guesses, never overwrites."""
    rappid = manifest.get("rappid", "")
    try:
        files = _rapp1_files(manifest, blob)
    except Exception as e:
        return f"I refused this egg whole: {e}. Nothing was written."
    payload = manifest.get("payload") or {}
    if variant == "organism" and payload.get("kernel") and payload.get("run"):
        return (f"This egg is a whole Brainstem ({len(files)} files, every one checked). It runs on its own, "
                f"beside this one: {payload['run']}. Nothing was written.")
    if variant == "organism":
        try:
            from utils.bond import hatch_organism  # type: ignore
            return f"Egg hatched. rappid={rappid}\n{hatch_organism(blob)}"
        except ImportError:
            pass
        home = _twin_home(rappid)
        if home.exists():
            return f"This egg is already hatched at {home}. I never overwrite; nothing was written."
        root = home.resolve()
        for path in files:
            if not (root / path).resolve().is_relative_to(root):
                return f"I refused this egg whole: {path} would land outside its own folder. Nothing was written."
        for path, octets in files.items():
            dest = root / path
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(octets)
        agents = sum(1 for p in files if p.startswith("agents/") and p.endswith("_agent.py"))
        return (f"Egg hatched: {len(files)} files, every one checked against the egg's label, now at {home}. "
                f"It carries {agents} agents and its own soul. Undo is deleting that one folder.")
    if variant == "rapplication":
        return _route_rapplication(manifest, blob)
    if variant == "session":
        return _route_session(manifest)
    if variant in ("neighborhood", "invite"):
        return _route_neighborhood(manifest)
    if variant == "estate":
        return _route_estate(manifest)
    return (f"This is a rapp/1 egg of a kind I don't hatch yet: '{variant or 'none'}'. "
            f"Its {len(files)} files all checked out. Nothing was written.")


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
        kind = manifest.get("type", "") or manifest.get("variant", "")
        if schema == RAPP1_EGG:
            return _route_rapp1(manifest, blob, kind)
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
