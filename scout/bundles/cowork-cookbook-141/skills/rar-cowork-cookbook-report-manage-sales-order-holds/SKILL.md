---
name: "rar-cowork-cookbook-report-manage-sales-order-holds"
description: "Builds a structured summary report of manage sales order holds activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_sales_order_holds", "rar_sha256": "9cc3b71330a539be9cc1787c9785e12004011d4c6451f2597599899d4ef5fd3b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_manage_sales_order_holds_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-manage-sales-order-holds:5c8627f572e0ee89c266bd8b8ab49d86ac11a0a062a23a89888d4254b97d68d8", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_manage_sales_order_holds`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_manage_sales_order_holds_agent.py` is
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

Manage sales order holds Summary Report — Builds a structured summary report of manage sales order holds activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-sales-order-holds
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_manage_sales_order_holds_agent.py` and embedded as the fenced Python below (sha256 9cc3b71330a539be…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_manage_sales_order_holds_agent.py` first:

```bash
python3 report_manage_sales_order_holds_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_manage_sales_order_holds_agent.py   # or on stdin
python3 report_manage_sales_order_holds_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage sales order holds Summary Report — Builds a structured summary report of manage sales order holds activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-sales-order-holds
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_manage_sales_order_holds',
    "version": '2.0.0',
    "display_name": 'Manage sales order holds Summary Report',
    "description": 'Builds a structured summary report of manage sales order holds activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-manage-sales-order-holds',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-manage-sales-order-holds',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0e5f564bb9f7b3db',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-sales-orders/manage-sales-order-holds'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/report-manage-sales-order-holds', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.333, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:report'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class ReportManageSalesOrderHolds(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportManageSalesOrderHolds'
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
    print(ReportManageSalesOrderHolds().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
