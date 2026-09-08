---
name: "rar-cowork-cookbook-eco-impact-analysis"
description: "Returns a read-only engineering change impact analysis for a given item number: active BOMs using it, open sales order lines, on-hand inventory by warehouse, and open purchase order lines, packaged as an Excel workbook."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/eco_impact_analysis", "rar_sha256": "fd387df1a2443852bb2fc4b378ef95312c86a03d8a9ea551113c4801246e2d16", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
