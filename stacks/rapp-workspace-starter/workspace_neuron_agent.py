"""WorkspaceNeuron — portable, PII-free base knowledge for a rapp-workspace/1.1 vault.

Drop this one .py file into agents/@rapp/. It gives the brainstem a compact
[Knowledge Base] block of the workspace-spec's operating rules — mint-once
identity, the egg contract, the frame-authority lease protocol, the world
boundary, the PII posture — WITHOUT that knowledge living as prose in every
planted workspace's CLAUDE.md/README.md. One file, versioned, tag-filterable,
~40% cheaper in tokens than the same facts as free-text markdown.

Ground rule for what belongs here vs. in a workspace's own .md files: this
file holds GENERIC knowledge — true of every rapp-workspace/1.1 instance,
never PII, never owner-specific. A workspace's CLAUDE.md/PERSONA.md/etc. hold
the OWNER-specific facts (who they are, what they're working on). Neurons are
the base layer every planted workspace shares; the .md files are the thin
instance-specific layer on top. Never put a customer name, a person's name,
or an owner's real data in a NEURONS entry — if it's specific to one
workspace, it does not belong in this file.

Same shape as @bill/neuron_agent.py (portable memory packs, no neurons/
folder, no install script, the file IS the registry) — this is the
rapp-workspace-starter stack's neuron instead of the Copilot Studio one.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@rapp/workspace_neuron_agent",
    "version": "1.0.0",
    "display_name": "WorkspaceNeuron",
    "description": "Injects a compact, PII-free Knowledge Base of rapp-workspace/1.1 setup and operating rules into the brainstem prompt — so a planted workspace's own .md files don't have to carry that generic knowledge as prose.",
    "author": "RAPP",
    "tags": ["memory", "neuron", "knowledge-base", "bootstrap", "rapp-workspace", "rapp-1", "egg", "frames"],
    "category": "core",
    "quality_tier": "reference",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

from agents.basic_agent import BasicAgent


NEURONS = [
    {
        "id": "rapp_workspace_anatomy",
        "name": "rapp-workspace/1.1 — required anatomy",
        "version": "1.1.0",
        "category": "rapp-workspace",
        "description": "What files a conformant workspace must have and why, per SPEC.md §3.",
        "memories": [
            {
                "memory_type": "fact",
                "content": "A conformant rapp-workspace/1.1 vault requires exactly six things at its root: CLAUDE.md (or the equivalent operating file for whatever assistant runs it), HOME.md (the one dashboard), a PERSONA.md-shaped owner profile, where-everything-lives.md (the estate map), README.md carrying a loud PRIVATE/NEVER PUBLISH guard, and rappid.json (the identity). Standard sections (strategy/, portfolio/, projects/, reference/, people/, meetings/) are added as the world needs them, not required.",
                "tags": ["anatomy", "required-files", "spec-3"],
            },
            {
                "memory_type": "fact",
                "content": "A workspace is scoped to exactly ONE world (one use-case domain). An owner running more than one world runs a SEPARATE workspace per world, never one workspace with mixed content. Cross-world content leakage is the single most common conformance failure.",
                "tags": ["world-boundary", "spec-5", "conformance"],
            },
            {
                "memory_type": "gotcha",
                "content": "A workspace is conformant if it keeps §3 (anatomy), §4 (two-faces data layer), §5 (world boundary), and §6 (privacy/sovereignty). A hive-mode workspace additionally MUST keep §9 (distributed operation). Don't call a workspace 'done' on file presence alone — check these four/five sections.",
                "tags": ["conformance", "checklist", "hive"],
            },
            {
                "memory_type": "pattern",
                "content": "When asked 'is this workspace compliant with rapp-workspace/1.1', check in this order: (1) rappid.json has a valid rappid:@owner/slug:64hex and was mint-once (never regenerated), (2) all six §3 files present, (3) README has the PRIVATE guard, (4) no git remote, or if one exists it's private + gated, (5) if rapp-projects/ exists, every stream chain-verifies with the rapp/1 reference implementation.",
                "tags": ["conformance", "audit", "pattern"],
            },
        ],
    },
    {
        "id": "rapp_workspace_identity",
        "name": "rapp-workspace/1.1 — identity (rappid, §2/§6)",
        "version": "1.1.0",
        "category": "rapp-workspace",
        "description": "Minting, mint-once, and the rappid grammar.",
        "memories": [
            {
                "memory_type": "fact",
                "content": "A rappid has the exact grammar rappid:@<owner>/<slug>:<64hex>, where owner and slug are lowercase, hyphen-separated labels ([a-z0-9]+(-[a-z0-9]+)*) and the tail is 64 lowercase hex characters. Keyless minting: sha256('rapp/1:rappid\\n' + uuid4_bytes).hexdigest(). Never derive a rappid from a name or any PII — it must be random, unguessable, keyless-by-default.",
                "tags": ["rappid", "identity", "grammar", "minting"],
            },
            {
                "memory_type": "gotcha",
                "content": "Mint-once is absolute: on reading an existing rappid.json, ALWAYS reuse the stored rappid — never regenerate it, even to 'fix' something. The only time a NEW rappid is minted is when planting a brand-new workspace instance from a template (a template's own rappid.json ships an intentional placeholder that the planting tool replaces exactly once).",
                "tags": ["rappid", "mint-once", "gotcha"],
            },
            {
                "memory_type": "fact",
                "content": "A template meant for reuse (e.g. a starter stack) should ship an OBVIOUSLY-placeholder rappid.json value (like 'REPLACE_ME_MINT_A_FRESH_RAPPID_BEFORE_USE') rather than a fake-looking valid hash, so nobody accidentally treats an unminted template as a live identity.",
                "tags": ["rappid", "template", "placeholder"],
            },
        ],
    },
    {
        "id": "rapp_workspace_privacy",
        "name": "rapp-workspace/1.1 — privacy & sovereignty (§6)",
        "version": "1.1.0",
        "category": "rapp-workspace",
        "description": "The non-negotiable privacy posture every workspace must hold.",
        "memories": [
            {
                "memory_type": "fact",
                "content": "Local-only is the default and the safest state for any workspace holding PII: no git remote at all. If a remote is ever added, it MUST be private, access-controlled, scoped to the workspace's own world, and gated by a fail-closed pre-push scan (secret scan + PII scan + world-boundary check).",
                "tags": ["privacy", "remote", "pre-push-gate"],
            },
            {
                "memory_type": "gotcha",
                "content": "A rapp-workspace instance is NEVER meant to be publicly hosted — it holds the owner's real, PII-bearing operating data by design. A planting/factory tool for workspaces should REFUSE a 'public' materialization mode outright, not just warn about it. Only a workspace's own generic STARTER TEMPLATE (PII-free, placeholder identity) is safe to publish.",
                "tags": ["privacy", "public-mode", "refusal", "gotcha"],
            },
            {
                "memory_type": "fact",
                "content": "The AI operating a workspace organizes and proposes; the owner decides and executes anything irreversible or outward-facing (a push, a publish, an external send). This sovereignty rule is not optional configuration — it's part of §6 conformance.",
                "tags": ["sovereignty", "owner-consent"],
            },
        ],
    },
    {
        "id": "rapp1_egg_contract",
        "name": "rapp/1 §9 — the egg contract",
        "version": "1.0.0",
        "category": "rapp-1",
        "description": "How to pack, address, and verify a portable rapp/1 egg — used to ship workspace templates, twins, and other organisms as one verifiable file.",
        "memories": [
            {
                "memory_type": "fact",
                "content": "An egg is a ZIP (stored, not deflated) with manifest.json first, containing exactly 7 keys: schema ('rapp/1-egg'), variant, rappid, created_utc, contents (a sorted list of {path, hash}), payload, sig. Two conformant packers of the same manifest value produce byte-identical eggs.",
                "tags": ["egg", "manifest", "spec-9.1"],
            },
            {
                "memory_type": "fact",
                "content": "Egg variants: organism (MUST include rappid.json + soul.md), rapplication (MUST include rappid.json + exactly one root agent.py), session/invite (JSON-only, no packed files), neighborhood, estate. Pick the variant that matches what's actually inside — 'organism' is the right choice for a workspace template.",
                "tags": ["egg", "variant", "organism"],
            },
            {
                "memory_type": "gotcha",
                "content": "verify_egg() checks integrity (contents hash-match, sorted paths, no path traversal / zip-slip, schema+variant sanity) — it does NOT check whether the CONTENTS are wholesome. A tool that plants/unpacks an egg should always call verify_egg() first and refuse to unpack on any failure, but that's a floor, not a full content review.",
                "tags": ["egg", "verify_egg", "security", "gotcha"],
            },
            {
                "memory_type": "pattern",
                "content": "To make a PII-free, reusable template out of a real, PII-bearing workspace: rebuild a fresh scaffold with generic {{token}} placeholders (not real names/customers/dates), pack it as an organism egg, grep-sweep the packed source for every real name before calling it done, then verify_egg() before shipping. Never just zip the real workspace and hope stripping happens later.",
                "tags": ["egg", "template", "pii-sweep", "pattern"],
            },
        ],
    },
    {
        "id": "rapp_projects_frame_authority",
        "name": "rapp-workspace/1.1 §8/§9 — the rapp-projects frame authority",
        "version": "1.1.0",
        "category": "rapp-workspace",
        "description": "Frames-as-authority, leases, and fork recovery for multi-operator project state.",
        "memories": [
            {
                "memory_type": "fact",
                "content": "Project state lives as append-only rapp/1 frame streams under rapp-projects/projects/<slug>/frames/*.json, hash-chained by prev. Boards, indexes, and status docs are DERIVED projections — regenerate them from the frames, never hand-edit them out of sync with the chain.",
                "tags": ["frames", "authority", "projection"],
            },
            {
                "memory_type": "fact",
                "content": "Frame kinds: project.genesis, work.punchin, work.heartbeat, work.checkpoint, work.status, work.handoff, work.takeover, work.punchout, project.verify. Every one of these is itself a frame in the chain — leases and their history are auditable, not a side-channel.",
                "tags": ["frames", "kinds", "leases"],
            },
            {
                "memory_type": "gotcha",
                "content": "A hive workspace (mode: hive) forces RAPP_REQUIRE_LEASE=1 — strict mode is mandatory, not optional, once more than one operator can write to the same store. Solo-mode workspaces don't need this, but should still punch in/out cleanly if they ever add a second operator later.",
                "tags": ["leases", "hive", "strict-mode", "gotcha"],
            },
            {
                "memory_type": "pattern",
                "content": "Sync loop for a hive: pull (rebase) → verify all chains → punchin → work (frame at every phase boundary) → punchout → pre-push gate → commit → push. Push soon after punchin — an unpushed lease protects nobody. A fork (two operators pushing frames sharing a seq) is caught deterministically by chain verification; recovery is append-only (quarantine the losing frame into frames/_forked/, never delete it, re-append with recovered_from).",
                "tags": ["sync-loop", "fork-recovery", "pattern"],
            },
        ],
    },
]


class WorkspaceNeuronAgent(BasicAgent):
    def __init__(self):
        self.name = "WorkspaceNeuron"
        self.metadata = {
            "name": self.name,
            "description": "Returns a compact [Knowledge Base] block of rapp-workspace/1.1 + rapp/1 setup and operating rules for system-prompt injection. Generic, PII-free — never owner-specific.",
            "parameters": {
                "type": "object",
                "properties": {
                    "category": {
                        "type": "string",
                        "description": "Filter to one neuron category (e.g., 'rapp-workspace', 'rapp-1'). Omit for all.",
                    },
                    "tags": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Filter individual memories by tag. ANY-match.",
                    },
                    "memory_type": {
                        "type": "string",
                        "description": "Filter by memory_type ('fact', 'gotcha', 'pattern'). Omit for all.",
                    },
                    "list": {
                        "type": "boolean",
                        "description": "If true, just list the installed neurons instead of the full Knowledge Base block.",
                    },
                },
                "required": [],
            },
        }
        self._cached_default = None
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        if kwargs.get("list"):
            return self._list_neurons()

        category = kwargs.get("category")
        tags = set(kwargs.get("tags") or [])
        memory_type = kwargs.get("memory_type")

        if not category and not tags and not memory_type and self._cached_default:
            return self._cached_default

        block = self._format(category=category, tags=tags, memory_type=memory_type)

        if not category and not tags and not memory_type:
            self._cached_default = block
        return block

    def _list_neurons(self):
        lines = [f"{len(NEURONS)} neuron(s) installed:"]
        for n in NEURONS:
            lines.append(f"  \u2022 {n['id']} ({n['category']}) \u2014 {len(n['memories'])} memories \u2014 v{n['version']}")
        return "\n".join(lines)

    def _format(self, category=None, tags=None, memory_type=None):
        sections = []
        total = 0
        for neuron in NEURONS:
            if category and neuron.get("category") != category:
                continue
            section_lines = []
            for mem in neuron.get("memories", []):
                if memory_type and mem.get("memory_type") != memory_type:
                    continue
                if tags and not (tags & set(mem.get("tags", []))):
                    continue
                mt = mem.get("memory_type", "fact")
                section_lines.append(f"  - [{mt}] {mem.get('content', '')}")
                total += 1
            if section_lines:
                sections.append(f"## {neuron['name']} (v{neuron['version']})\n" + "\n".join(section_lines))

        if not sections:
            return "[Knowledge Base]\n(no neurons matched the filter)"
        header = f"[Knowledge Base] \u2014 {total} memories across {len(sections)} neuron(s)"
        return header + "\n\n" + "\n\n".join(sections)


if __name__ == "__main__":
    a = WorkspaceNeuronAgent()
    print(a.perform())
