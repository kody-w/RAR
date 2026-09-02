---
name: "rar-cat-agent-skills-brand-template-enforcer"
description: "Ensure every generated PowerPoint deck or Word document starts from the correct bundled or SharePoint-hosted brand template."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/brand_template_enforcer", "rar_sha256": "ae1779f176150087d15edf582f1193947f2b3df165ad863d53759e62dd1e9061", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "brand_template_enforcer_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/brand-template-enforcer:df95a977c3bc8ac3c0b6d938705e6374e3d2a657a9702fa20b9884044907e687", "kind": "skill"}, "version": "2.2.0", "author": "Doug Bellingeri", "tags": ["branding", "powerpoint", "word", "templates", "documents", "presentations"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/brand_template_enforcer`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `brand_template_enforcer_agent.py` is
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

Brand Template Enforcer — Ensure every generated PowerPoint deck or Word document starts from the correct bundled or SharePoint-hosted brand template.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#brand-template-enforcer
  Upstream author: Doug Bellingeri
  Upstream version: 1.2.0
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `brand_template_enforcer_agent.py` and embedded as the fenced Python below (sha256 ae1779f176150087…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `brand_template_enforcer_agent.py` first:

```bash
python3 brand_template_enforcer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 brand_template_enforcer_agent.py   # or on stdin
python3 brand_template_enforcer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Brand Template Enforcer — Ensure every generated PowerPoint deck or Word document starts from the correct bundled or SharePoint-hosted brand template.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#brand-template-enforcer
  Upstream author: Doug Bellingeri
  Upstream version: 1.2.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/brand_template_enforcer',
    "version": '2.2.0',
    "display_name": 'Brand Template Enforcer',
    "description": 'Ensure every generated PowerPoint deck or Word document starts from the correct bundled or SharePoint-hosted brand template.',
    "author": 'Doug Bellingeri',
    "tags": ['branding', 'powerpoint', 'word', 'templates', 'documents', 'presentations'],
    "category": 'productivity',
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
        "upstream_slug": 'brand-template-enforcer',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#brand-template-enforcer',
        "upstream_version": '1.2.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '5bd07a11a05931f7',
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 1.0, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:documents', 'tag:powerpoint', 'tag:presentations', 'tag:word', 'word:deck', 'word:document'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class BrandTemplateEnforcer(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BrandTemplateEnforcer'
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
    print(BrandTemplateEnforcer().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
