---
name: "rar-cowork-cookbook-report-document-warehouse-policies"
description: "Builds a structured summary report of document warehouse policies activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_document_warehouse_policies", "rar_sha256": "9175d05ec95d3de7534822d577ba0f46f4eb548bd487871152419df7735bbb18", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_document_warehouse_policies_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-document-warehouse-policies:61fa004e103168aafd5fdfcec7e448cb0a81166d03e72760a3ad992dda019156", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_document_warehouse_policies`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_document_warehouse_policies_agent.py` is
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
