---
name: "rar-cowork-cookbook-ppt-exec-document-safety-protocols"
description: "Generates an executive-ready PowerPoint deck on document safety protocols status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_document_safety_protocols", "rar_sha256": "b85b5717a5151d0c70af8a8ba2978ce705410fb46610884d6b1d7968ad01cb90", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_document_safety_protocols_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-document-safety-protocols:2e54f84ecdd256d8ac8eec73c93465606ac2ff79877dec9aae5f15d2630e54ad", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_document_safety_protocols`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_document_safety_protocols_agent.py` is
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
