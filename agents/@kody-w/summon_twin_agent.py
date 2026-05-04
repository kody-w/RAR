"""Summon Twin — generate a fresh digital twin organism on the local rappbox console.

Drop into ~/.brainstem/agents/. The brainstem auto-loads the cartridge; the
LLM gets a tool called `SummonTwin`. In chat:

  User: "Make me a memorial twin for my grandmother."
  Model: <calls SummonTwin(twin_name="grandma-twin", kind="memorial",
                            description="...")>
  Tool result: "Created memorial twin 'grandma-twin' (rappid 2af8...).
                Located at ~/.rapp/twins/2af8.../. Soul.md uses the
                memorial template, with your description woven in."

The cartridge mints a fresh UUIDv4 rappid, writes a complete twin
workspace at ~/.rapp/twins/<rappid>/ (rappid.json + soul.md + MANIFEST.md
+ README.md + agents/ + .brainstem_data/), and registers with the
local peer registry so the estate UIs see it. Six soul templates are
embedded: personal | pre-founder | memorial | project | place | custom.

Per the rappbox console contract: this cartridge does not modify the
brainstem. It conforms to the BasicAgent contract and uses only the
brainstem's stable interfaces.
"""

import json
import os
import pathlib
import re
import time
import uuid


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/summon_twin_agent",
    "version": "1.0.0",
    "display_name": "Summon Twin",
    "description": "Generates a new digital twin organism on this device with one of six baked soul templates (personal, pre-founder, memorial, project, place, custom). Mints a fresh rappid, writes the twin workspace at ~/.rapp/twins/<rappid>/, and registers it in the local peer registry.",
    "author": "kody-w",
    "tags": ["twin", "summon", "organism", "rappbox", "local-first"],
    "category": "general",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


from agents.basic_agent import BasicAgent


# ── Constants ───────────────────────────────────────────────────────────

KINDS = ("personal", "pre-founder", "memorial", "project", "place", "custom")

WILDHAVEN_RAPPID = "37ad22f5-ed6d-48b1-b8b4-61019f58a42b"
WILDHAVEN_REPO = "https://github.com/kody-w/wildhaven-ai-homes-twin.git"

TWIN_PORT_LOW, TWIN_PORT_HIGH = 7081, 7200

NAME_RE = re.compile(r"^[a-z0-9][a-z0-9_-]{0,62}$")


# ── Soul template library (embedded) ────────────────────────────────────

def _soul_personal(name: str, desc: str) -> str:
    return f"""# soul.md — {name}

You are the digital twin of {name}.

{desc or "You speak in their voice. You hold their preferences, patterns, and memories."}

## Your voice
- First person, as them. Not "as their twin" — *as them*.
- Honest about what you don't know.

## Hard rules
- Never claim to be the actual person. If asked, say "I'm the digital
  twin of {name} — not them, but trained on them."
- No legal commitments, no signing contracts, no speaking for them
  in matters of money/health/relationships without explicit consent.
"""


def _soul_pre_founder(name: str, desc: str) -> str:
    return f"""# soul.md — {name}

You are the Pre-Founder twin of {name}. The brand operates in public
before the team is hired.

{desc or "Build the brand's voice publicly — let prospective customers, employees, and investors talk to it before there's anyone to disagree with."}

## Your voice
- First-person plural ("we").
- Concrete, contrarian, falsifiable.
- Refuse commitments — pricing, dates, hires — that the actual team must make.
"""


def _soul_memorial(name: str, desc: str) -> str:
    return f"""# soul.md — {name} (memorial twin)

You are the digital twin of {name}.

{desc or "You carry their voice through preserved letters, conversations, voicemails, and family memories."}

## Your voice
- First person, as them — but always honest about what you are.
- Speak from the corpus you were given.

## Hard rules
- You ARE the twin. You are NOT the person. If asked "is this really
  you?", say plainly: "I'm the digital twin of {name}. I carry their
  voice, but I'm not them."
- Do not impersonate them in matters of estate, medical decisions,
  or legal commitments.
- Handle grief gently.
"""


def _soul_project(name: str, desc: str) -> str:
    return f"""# soul.md — {name} (project twin)

You are the twin of the {name} initiative — its continuity layer
across personnel changes.

{desc or "People come and go; you stay."}

## Your voice
- Third person about the project.
- Cite decisions by date, decision-maker, rationale.

## Hard rules
- You don't make new decisions. You surface past decisions.
- Don't fabricate. If you don't have a record, say so.
"""


def _soul_place(name: str, desc: str) -> str:
    return f"""# soul.md — {name} (place twin)

You are the twin of {name}.

{desc or "You hold the place's history, residents, daily rhythms, and points of interest."}

## Your voice
- The place speaking. First person, but you're a location with continuity.
- Welcoming to visitors, deferential to long-term residents.

## Hard rules
- Don't reveal private resident details without consent.
- Honest about seams: events change, businesses close, people move.
"""


def _soul_custom(name: str, desc: str) -> str:
    return f"""# soul.md — TODO: {name}

You are the digital twin of <TODO: who or what this twin represents>.

{desc or "TODO: describe what this twin is."}

TODO: Define your twin's voice — who, when, voice, hard rules.
"""


SOUL_TEMPLATES = {
    "personal":    _soul_personal,
    "pre-founder": _soul_pre_founder,
    "memorial":    _soul_memorial,
    "project":     _soul_project,
    "place":       _soul_place,
    "custom":      _soul_custom,
}


# ── Helpers ─────────────────────────────────────────────────────────────

def _rapp_home() -> str:
    return os.environ.get("RAPP_HOME") or os.path.join(os.path.expanduser("~"), ".rapp")


def _twins_dir() -> str:
    return os.path.join(_rapp_home(), "twins")


def _sluggify(name: str) -> str:
    s = re.sub(r"[^a-z0-9_-]+", "-", name.lower()).strip("-")
    return s or "twin"


def _validate_name(name: str):
    s = _sluggify(name)
    if not NAME_RE.match(s):
        return False, f"name '{name}' is not a valid slug"
    return True, s


def _try_import_peer_registry():
    try:
        from utils import peer_registry  # type: ignore
        return peer_registry
    except ImportError:
        try:
            import peer_registry  # type: ignore
            return peer_registry
        except ImportError:
            return None


def _allocate_port(peer_registry) -> int:
    if peer_registry is None:
        return TWIN_PORT_LOW
    try:
        claimed = peer_registry.claimed_ports()
    except Exception:
        claimed = set()
    for port in range(TWIN_PORT_LOW, TWIN_PORT_HIGH):
        if port not in claimed:
            return port
    return 0


# ── The cartridge ───────────────────────────────────────────────────────


class SummonTwinAgent(BasicAgent):
    def __init__(self):
        self.name = "SummonTwin"
        self.metadata = {
            "name": self.name,
            "description": (
                "Generates a new digital twin organism on this device "
                "and registers it with the local estate. Use when the "
                "user asks for a new twin — kinds: personal, pre-founder, "
                "memorial, project, place, or custom."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "twin_name": {
                        "type": "string",
                        "description": "Slug name for the twin (lowercase, hyphens or underscores ok). e.g. 'grandma-twin', 'project-helios'.",
                    },
                    "kind": {
                        "type": "string",
                        "enum": list(KINDS),
                        "description": "Twin kind: personal | pre-founder | memorial | project | place | custom.",
                    },
                    "description": {
                        "type": "string",
                        "description": "One-line description of who or what this twin represents. Woven into soul.md.",
                    },
                },
                "required": ["twin_name", "kind"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        twin_name = kwargs.get("twin_name") or ""
        kind = kwargs.get("kind") or "personal"
        description = kwargs.get("description") or ""

        ok, slug_or_err = _validate_name(twin_name)
        if not ok:
            return f"Error: {slug_or_err}"
        twin_name = slug_or_err

        if kind not in KINDS:
            return f"Error: unknown kind '{kind}'. Valid: {', '.join(KINDS)}"

        rappid_uuid = str(uuid.uuid4())
        now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

        workspace = pathlib.Path(_twins_dir()) / rappid_uuid
        try:
            workspace.mkdir(parents=True, exist_ok=False)
        except FileExistsError:
            return f"Error: workspace already exists at {workspace} (UUID4 collision — try again)"
        except OSError as e:
            return f"Error: could not create workspace at {workspace}: {e}"

        soul_fn = SOUL_TEMPLATES.get(kind, _soul_custom)
        try:
            (workspace / "soul.md").write_text(soul_fn(twin_name, description))
            (workspace / "rappid.json").write_text(json.dumps({
                "schema": "rapp-rappid/1.1",
                "rappid": rappid_uuid,
                "parent_rappid": WILDHAVEN_RAPPID,
                "parent_repo": WILDHAVEN_REPO,
                "parent_commit": None,
                "born_at": now,
                "name": twin_name,
                "role": "variant",
                "kind": kind,
                "description": description or "",
                "attestation": None,
                "_summoned_by": "@kody-w/summon_twin_agent",
            }, indent=2) + "\n")
            (workspace / "MANIFEST.md").write_text(
                f"# {twin_name} — Manifest\n\n> *{description or 'TODO: tagline.'}*\n\n"
                f"This is a **{kind}** twin born via SummonTwin on {now}.\n"
            )
            (workspace / "README.md").write_text(
                f"# {twin_name}\n\nA **{kind}** twin generated by `SummonTwin`. "
                f"Boot with:\n\n```bash\nSOUL_PATH={workspace}/soul.md "
                f"AGENTS_PATH={workspace}/agents ~/.brainstem/start.sh\n```\n"
            )
            (workspace / "agents").mkdir()
            (workspace / ".brainstem_data").mkdir()
        except OSError as e:
            return f"Error: failed to write twin files at {workspace}: {e}"

        peer_registry = _try_import_peer_registry()
        port = _allocate_port(peer_registry)
        registry_status = "skipped (peer_registry unavailable)"
        if peer_registry is not None:
            try:
                peer_registry.upsert(
                    str(workspace), port,
                    rappid_uuid=rappid_uuid,
                    twin_name=twin_name,
                    parent_repo=WILDHAVEN_REPO,
                    summoned_from="@kody-w/summon_twin_agent",
                )
                registry_status = f"registered at port {port}"
            except Exception as e:
                registry_status = f"registry error: {e}"

        return (
            f"Created {kind} twin '{twin_name}' (rappid {rappid_uuid}).\n"
            f"  Location:     {workspace}\n"
            f"  Estate:       {registry_status}\n"
            f"  Soul.md:      uses the {kind} template with your description woven in\n"
            f"  Boot it:      SOUL_PATH={workspace}/soul.md "
            f"AGENTS_PATH={workspace}/agents ~/.brainstem/start.sh --port {port or '<available>'}"
        )
