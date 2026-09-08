---
name: "rar-cowork-cookbook-eco-impact-analysis"
description: "Returns a read-only engineering change impact analysis for a given item number: active BOMs using it, open sales order lines, on-hand inventory by warehouse, and open purchase order lines, packaged as an Excel workbook."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/eco_impact_analysis", "rar_sha256": "fd387df1a2443852bb2fc4b378ef95312c86a03d8a9ea551113c4801246e2d16", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/eco_impact_analysis`. The original RAPP
agent is preserved byte-for-byte in `eco_impact_analysis_agent.py` and in the RCI capsule.

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

Engineering Change Order Impact Analysis — Returns a read-only engineering change impact analysis for a given item number: active BOMs using it, open sales order lines, on-hand inventory by warehouse, and open purchase order lines, packaged as an Excel workbook.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/eco-impact-analysis
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
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "item_number": {
      "description": "The item to analyze (defaults to M0001 'Wiring Harness' if not specified).",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 company/legal entity context (defaults to USMF).",
      "type": "string"
    },
    "operation": {
      "description": "What to do: run, prompt, plan, checklist, describe.",
      "enum": [
        "run",
        "prompt",
        "plan",
        "checklist",
        "describe"
      ],
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `eco_impact_analysis_agent.py` and embedded as the fenced Python below (sha256 fd387df1a2443852…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `eco_impact_analysis_agent.py` first:

```bash
python3 eco_impact_analysis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 eco_impact_analysis_agent.py   # or on stdin
python3 eco_impact_analysis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Engineering Change Order Impact Analysis — Returns a read-only engineering change impact analysis for a given item number: active BOMs using it, open sales order lines, on-hand inventory by warehouse, and open purchase order lines, packaged as an Excel workbook.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/eco-impact-analysis
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/eco_impact_analysis',
    "version": '3.0.3',
    "display_name": 'Engineering Change Order Impact Analysis',
    "description": 'Returns a read-only engineering change impact analysis for a given item number: active BOMs using it, open sales order lines, on-hand inventory by warehouse, and open purchase order lines, packaged as an Excel workbook.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'eco-impact-analysis',
        "upstream_url": 'https://coworkcookbook.com/recipes/eco-impact-analysis',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '39a03fc4bee22289',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/manage-active-products'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/eco-impact-analysis', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the Production or Item maintainer role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: Workbook with BOM/SO/PO/inventory impact sheets and a summary.'], 'confidence': 1.0, 'deliverable': 'Workbook with BOM/SO/PO/inventory impact sheets and a summary.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'item_number': "The item to analyze (defaults to M0001 'Wiring Harness' if not specified).", 'legal_entity': 'D365 company/legal entity context (defaults to USMF).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'didn't realize that part is in 14 other BOMs' surprise by surfacing the full blast radius of a proposed engineering change before it is approved.", 'expected_output': 'Workbook with BOM/SO/PO/inventory impact sheets and a summary.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the Production or Item maintainer role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Given an item number (default to M0001 'Wiring Harness' in USMF if not specified), produce an impact analysis: (a) every active BOM where the item is a component, with the parent item and the quantity per; (b) every open sales order line for the item with quantity and expected ship date; (c) on-hand inventory by warehouse; (d) any open purchase order lines for the item with expected receipt date. Output an Excel workbook 'ECO-impact-<item>-<YYYY-MM-DD>.xlsx' with one sheet per category and a summary sheet. Do not change anything.", 'steps': ['Paste the prompt and provide the item number when asked.', 'Review the workbook with the engineering change board.'], 'tenant_caveat': "Validated end-to-end against a live Cowork tenant on 2026-05-23 with USMF item M0001 (Wiring Harness). Cowork ran all five plan steps and produced 'ECO-impact-M0001-2026-05-23.xlsx' with 5 sheets. Findings: 12 active BOM rows use M0001 as a component (plus a flagged sub-section of 3 BOMs - 000020, 000022, 000121 - that contain M0001 but have no active version); 0 open sales orders (M0001 is a purchased component, not a finished good); 956 units total on-hand across 3 warehouses (884 at 1/wh 11, 72 at 1/wh 12); 3 open purchase order lines totalling 2,492 units and $9,594.20. No data was modified.", 'verified_against': 'm365.cloud.microsoft 2026-05-23', 'what_it_does': 'Builds a complete pre-change impact report (BOM usage, open orders, inventory, inbound POs) for a single item.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Returns a read-only engineering change impact analysis for a given item number: active BOMs using it, open sales order lines, on-hand inventory by warehouse, and open purchase order lines, packaged as an Excel workbook.', 'example_request': 'Run an ECO impact analysis for item M0001 in USMF and give me the Excel workbook.', 'inputs': [{'description': "The item to analyze (defaults to M0001 'Wiring Harness' if not specified).", 'name': 'item_number'}, {'description': 'D365 company/legal entity context (defaults to USMF).', 'name': 'legal_entity'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a proposed item change needs downstream impact quantified across BOMs, sales orders, inventory, and purchase orders before a change board review.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt and provide the item number when asked.', 'Review the workbook with the engineering change board.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class EcoImpactAnalysis(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'EcoImpactAnalysis'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'item_number': {'description': "The item to analyze (defaults to M0001 'Wiring Harness' if not specified).", 'type': 'string'}, 'legal_entity': {'description': 'D365 company/legal entity context (defaults to USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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

    # ── recipe entries: the upstream recipe, verbatim, deterministic ─────

    def _recipe_context(self, kwargs):
        extras = []
        subject = self._subject(kwargs)
        if subject:
            extras.append(f"subject: {subject}")
        for key in _SPEC["params"]:
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _recipe_prompt(self, kwargs):
        r = _SPEC["recipe"]
        lines = [r["prompt"]]
        extras = self._recipe_context(kwargs)
        if extras:
            lines += ["", "Context supplied by the caller:"] + [f"- {e}" for e in extras]
        return lines

    def _recipe_attribution(self):
        src = __manifest__["source"]
        r = _SPEC["recipe"]
        who = ", ".join(r.get("authors") or []) or __manifest__["author"]
        return [
            f"Recipe: {__manifest__['display_name']} — by {who}, {src['source_name']} "
            f"({src['license']}). Source: {src['upstream_url']}",
        ]

    def _perform_recipe(self, op, kwargs):
        r = _SPEC["recipe"]
        ref = _SPEC.get("refinement") or {}
        if op == "prompt":
            return "\n".join(self._recipe_prompt(kwargs) + [""] + self._recipe_attribution())
        if op == "plan":
            lines = [f"Steps for {__manifest__['display_name']} on {r['platform']}:"]
            lines += [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "checklist":
            lines = ["Before you run it:"] + [f"  [ ] {p}" for p in r["prerequisites"]]
            if r.get("expected_output"):
                lines += ["", "Done when:", f"  [ ] {r['expected_output']}"]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "describe":
            lines = self._provenance()
            if ref.get("when_to_use"):
                lines += ["", f"When to use: {ref['when_to_use']}"]
            if ref.get("example_request"):
                lines += [f"Ask for it like: {ref['example_request']}"]
            if ref.get("inputs"):
                lines += ["", "It will ask you for:"] + [f"  - {i['name']}: {i['description']}" for i in ref["inputs"]]
            if r.get("business_value"):
                lines += ["", f"Why it matters: {r['business_value']}"]
            return "\n".join(lines)
        if op == "run":
            lines = [f"{__manifest__['display_name']} — run on {r['platform']}", ""]
            if r.get("what_it_does"):
                lines += [r["what_it_does"], ""]
            lines += [f"Prompt (paste into {r['platform']}):", ""] + self._recipe_prompt(kwargs) + [""]
            lines += ["Procedure:"] + [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)] + [""]
            lines += ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]] + [""]
            lines += [f"Deliverable: {_SPEC['deliverable']}", ""]
            if r.get("tenant_caveat"):
                lines += [f"Verified upstream: {r['tenant_caveat']}", ""]
            return "\n".join(lines + self._recipe_attribution())
        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if _SPEC.get("recipe"):
            return self._perform_recipe(op, kwargs)

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
    print(EcoImpactAnalysis().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
