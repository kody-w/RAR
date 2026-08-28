---
name: "rar-cat-agent-skills-brand-template-enforcer"
description: "Ensure every generated PowerPoint deck or Word document starts from the correct bundled or SharePoint-hosted brand template."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/brand_template_enforcer", "rar_sha256": "ae1779f176150087d15edf582f1193947f2b3df165ad863d53759e62dd1e9061", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.2.0", "author": "Doug Bellingeri", "tags": ["branding", "powerpoint", "word", "templates", "documents", "presentations"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/brand_template_enforcer`. The original RAPP
agent is preserved byte-for-byte in `brand_template_enforcer_agent.py` and in the RCI capsule.

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
