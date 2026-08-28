---
name: "rar-cowork-cookbook-report-document-warehouse-policies"
description: "Builds a structured summary report of document warehouse policies activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_document_warehouse_policies", "rar_sha256": "84a42807b9bec90ef4c226cafd72e71f509623e8a9076286241e0aac229bbdc5", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_document_warehouse_policies`. The original RAPP
agent is preserved byte-for-byte in `report_document_warehouse_policies_agent.py` and in the RCI capsule.

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

Document warehouse policies Summary Report — Builds a structured summary report of document warehouse policies activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-document-warehouse-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_document_warehouse_policies_agent.py` and embedded as the fenced Python below (sha256 84a42807b9bec90e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_document_warehouse_policies_agent.py` first:

```bash
python3 report_document_warehouse_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_document_warehouse_policies_agent.py   # or on stdin
python3 report_document_warehouse_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Document warehouse policies Summary Report — Builds a structured summary report of document warehouse policies activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-document-warehouse-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_document_warehouse_policies',
    "version": '2.0.1',
    "display_name": 'Document warehouse policies Summary Report',
    "description": 'Builds a structured summary report of document warehouse policies activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-document-warehouse-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-document-warehouse-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c45d22d69a916db4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-warehouse-operations/document-warehouse-policies'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/report-document-warehouse-policies', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.429, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:report', 'word:document'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class ReportDocumentWarehousePolicies(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDocumentWarehousePolicies'
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
    print(ReportDocumentWarehousePolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
