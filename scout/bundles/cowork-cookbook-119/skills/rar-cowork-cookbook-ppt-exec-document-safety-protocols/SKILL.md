---
name: "rar-cowork-cookbook-ppt-exec-document-safety-protocols"
description: "Generates an executive-ready PowerPoint deck on document safety protocols status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_document_safety_protocols", "rar_sha256": "b85b5717a5151d0c70af8a8ba2978ce705410fb46610884d6b1d7968ad01cb90", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_document_safety_protocols_agent.py` and embedded as the fenced Python below (sha256 b85b5717a5151d0c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_document_safety_protocols_agent.py` first:

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
    "version": '2.0.0',
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
