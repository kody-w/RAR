---
name: "rar-rapp-egg-hatcher"
description: "Hatch any .egg cartridge \u2014 introspects the cartridge's schema and routes to the right destination (organism / rapplication / session / neighborhood / estate). Accepts a local file path OR a URL. Never guesses; refuses on unknown cartridge kinds. Use when the operator says 'hatch this egg', 'load this cartridge', 'open this .egg', etc."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/egg_hatcher", "rar_sha256": "c4b31f7bb445324c13b54bac009d2bb4f34de8212a3c6ca60757602254b348cf", "source_kind": "rar-agent", "source_commit": "14dedfd3910bd8d703499d911d4a919253e3f890", "version": "1.2.1", "author": "RAPP", "tags": ["egg", "cartridge", "hatch", "organism", "rapplication", "lifecycle"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `egg_hatcher_agent.py` and embedded as the fenced Python below (sha256 c4b31f7bb445324c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `egg_hatcher_agent.py` first:

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
    "version": "1.2.1",
    "display_name": "EggHatcher",
    "description": "Introspects any .egg cartridge (local path or URL) and routes it by manifest schema/type to hatch, install, or mount; refuses unknown kinds.",
    "author": "RAPP",
    "tags": ["egg", "cartridge", "hatch", "organism", "rapplication", "lifecycle"],
    "category": "core",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    "distinct_from": {"@kody-w/twin_egg_hatcher": "That agent builds one twin from a repo, a folder or an egg. This one opens any kind of egg, checks every file against the egg's label, and routes it by kind."},
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
