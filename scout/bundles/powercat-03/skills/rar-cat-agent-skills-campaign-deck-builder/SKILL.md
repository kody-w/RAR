---
name: "rar-cat-agent-skills-campaign-deck-builder"
description: "Turn a short interview into a charming, vibrant 3-slide marketing-campaign deck by filling a bundled PowerPoint template."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/campaign_deck_builder", "rar_sha256": "9eaee36124c834b7c71a49853abb992be0a0ca4f7db6ab125621475019ee15de", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "campaign_deck_builder_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/campaign-deck-builder:eb33c4b9ae8c076a026fce680fa815219afa34c9f0a7ad484dd58999d91f0b24", "kind": "skill"}, "version": "2.0.0", "author": "Adi Leibowitz", "tags": ["marketing", "presentations", "powerpoint", "automation", "scripts"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/campaign_deck_builder`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `campaign_deck_builder_agent.py` is
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

Campaign Deck Builder — Turn a short interview into a charming, vibrant 3-slide marketing-campaign deck by filling a bundled PowerPoint template.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#campaign-deck-builder
  Upstream author: Adi Leibowitz
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "audience": {
      "description": "Optional. Who reads it \u2014 this drives register, length and what can be assumed.",
      "type": "string"
    },
    "operation": {
      "description": "What to do: run, plan, checklist, describe.",
      "enum": [
        "run",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "subject": {
      "description": "What to produce, and about what.",
      "type": "string"
    }
  },
  "required": [
    "operation"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `campaign_deck_builder_agent.py` and embedded as the fenced Python below (sha256 9eaee36124c834b7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `campaign_deck_builder_agent.py` first:

```bash
python3 campaign_deck_builder_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 campaign_deck_builder_agent.py   # or on stdin
python3 campaign_deck_builder_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Campaign Deck Builder — Turn a short interview into a charming, vibrant 3-slide marketing-campaign deck by filling a bundled PowerPoint template.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#campaign-deck-builder
  Upstream author: Adi Leibowitz
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/campaign_deck_builder',
    "version": '2.0.0',
    "display_name": 'Campaign Deck Builder',
    "description": 'Turn a short interview into a charming, vibrant 3-slide marketing-campaign deck by filling a bundled PowerPoint template.',
    "author": 'Adi Leibowitz',
    "tags": ['marketing', 'presentations', 'powerpoint', 'automation', 'scripts'],
    "category": 'devtools',
    "quality_tier": "frontier",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cat-agent-skills',
        "source_name": 'CAT Agent Skills',
        "source_url": 'https://microsoft.github.io/cat-agent-skills/',
        "upstream_slug": 'campaign-deck-builder',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#campaign-deck-builder',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '23b22be138aae9b6',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Copilot Studio'],
}


try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.5, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:powerpoint', 'tag:presentations', 'word:deck'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class CampaignDeckBuilder(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CampaignDeckBuilder'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'audience': {'description': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to produce, and about what.', 'type': 'string'}},
                "required": ["operation"],
            },
        }
        super().__init__(self.name, self.metadata)

    # ── helpers ─────────────────────────────────────────────────────────

    def _subject(self, kwargs):
        for key in ("subject", "input", "target", "topic"):
            value = str(kwargs.get(key) or "").strip()
            if value:
                return value
        return ""

    def _header(self, subject):
        label = subject or f"<no {_SPEC['subject_label']} supplied>"
        return f"{_SPEC['verb']}: {label}"

    def _context(self, kwargs):
        extras = []
        for key in _SPEC["params"]:
            if key == "subject":
                continue
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _plan(self, subject, kwargs):
        lines = [self._header(subject)]
        extras = self._context(kwargs)
        if extras:
            lines += ["", "Context:"] + [f"  {e}" for e in extras]
        lines += ["", "Procedure:"]
        lines += [f"  {i}. {step}" for i, step in enumerate(_SPEC["steps"], 1)]
        if not subject:
            lines += [
                "",
                f"Pass subject=\u0022...\u0022 to bind this procedure to a "
                f"specific {_SPEC['subject_label']}.",
            ]
        return lines

    def _checklist(self):
        return ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]]

    def _provenance(self):
        src = __manifest__["source"]
        lines = [
            f"{__manifest__['display_name']} (v{__manifest__['version']})",
            "",
            __manifest__["description"],
            "",
            f"Capability shape: {_SPEC['archetype']} "
            f"(confidence {_SPEC['confidence']})",
        ]
        platforms = __manifest__.get("platforms") or []
        if platforms:
            lines.append("Runs on:          " + ", ".join(platforms))
        lines += [
            "",
            f"Indexed from:     {src['source_name']}",
            f"Upstream entry:   {src['upstream_url']}",
            f"Upstream author:  {__manifest__['author']}",
            "",
            "RAR indexes this capability and implements its method; the "
            "upstream library remains the authority for its own instructions. "
            "Open the link above to get those from the source.",
        ]
        return lines

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if op == "describe":
            return "\n".join(self._provenance())

        if op == "checklist":
            return "\n".join([self._header(subject), ""] + self._checklist())

        if op == "plan":
            return "\n".join(self._plan(subject, kwargs))

        if op == "run":
            lines = self._plan(subject, kwargs)
            lines += [""] + self._checklist()
            lines += ["", f"Deliverable: {_SPEC['deliverable']}"]
            lines += ["", f"Source: {__manifest__['source']['upstream_url']}"]
            return "\n".join(lines)

        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )


if __name__ == "__main__":
    print(CampaignDeckBuilder().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
