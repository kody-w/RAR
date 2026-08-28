---
name: "rar-cowork-cookbook-report-document-warehouse-policies"
description: "Builds a structured summary report of document warehouse policies activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_document_warehouse_policies", "rar_sha256": "9175d05ec95d3de7534822d577ba0f46f4eb548bd487871152419df7735bbb18", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_document_warehouse_policies_agent.py` and embedded as the fenced Python below (sha256 9175d05ec95d3de7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_document_warehouse_policies_agent.py` first:

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
    "version": '2.0.0',
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
