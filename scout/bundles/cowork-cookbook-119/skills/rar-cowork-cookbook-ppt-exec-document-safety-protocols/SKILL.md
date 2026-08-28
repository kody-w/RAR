---
name: "rar-cowork-cookbook-ppt-exec-document-safety-protocols"
description: "Generates an executive-ready PowerPoint deck on document safety protocols status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_document_safety_protocols", "rar_sha256": "32c8858f447749b3302d324417dbb09d31b6e725224e35aa685f38cca25d5ba1", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_document_safety_protocols`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_document_safety_protocols_agent.py` and in the RCI capsule.

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

Document safety protocols Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on document safety protocols status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-document-safety-protocols
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_document_safety_protocols_agent.py` and embedded as the fenced Python below (sha256 32c8858f447749b3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_document_safety_protocols_agent.py` first:

```bash
python3 ppt_exec_document_safety_protocols_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_document_safety_protocols_agent.py   # or on stdin
python3 ppt_exec_document_safety_protocols_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Document safety protocols Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on document safety protocols status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-document-safety-protocols
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_document_safety_protocols',
    "version": '2.0.1',
    "display_name": 'Document safety protocols Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on document safety protocols status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'ppt-exec-document-safety-protocols',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-document-safety-protocols',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd928ba84c5081e87',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-workplace-compliance/document-safety-protocols'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/ppt-exec-document-safety-protocols', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Microsoft 365 Copilot Cowork'],
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.5, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['word:deck', 'word:document'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class PptExecDocumentSafetyProtocols(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDocumentSafetyProtocols'
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
    print(PptExecDocumentSafetyProtocols().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
