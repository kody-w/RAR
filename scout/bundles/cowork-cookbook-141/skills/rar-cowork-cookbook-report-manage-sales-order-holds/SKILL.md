---
name: "rar-cowork-cookbook-report-manage-sales-order-holds"
description: "Builds a structured summary report of manage sales order holds activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_sales_order_holds", "rar_sha256": "91c39dcab6ecb97e59a2e0e71d89b89be0c12e3da80062dc8d2ce831d18fab95", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_manage_sales_order_holds`. The original RAPP
agent is preserved byte-for-byte in `report_manage_sales_order_holds_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_manage_sales_order_holds_agent.py` and embedded as the fenced Python below (sha256 91c39dcab6ecb97e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_manage_sales_order_holds_agent.py` first:

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
    "version": '2.0.1',
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
