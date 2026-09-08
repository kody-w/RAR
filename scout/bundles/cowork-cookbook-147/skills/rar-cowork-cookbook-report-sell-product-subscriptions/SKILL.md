---
name: "rar-cowork-cookbook-report-sell-product-subscriptions"
description: "Builds a read-only summary report of sell product subscriptions from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_sell_product_subscriptions", "rar_sha256": "a9e4e62cf8f7601d040a1b81e2c37dbec6743b961007267e551f9854ef10e4ee", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_sell_product_subscriptions`. The original RAPP
agent is preserved byte-for-byte in `report_sell_product_subscriptions_agent.py` and in the RCI capsule.

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

Sell product subscriptions Summary Report — Builds a read-only summary report of sell product subscriptions from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-sell-product-subscriptions
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
    "legal_entity": {
      "description": "D365 legal entity to report against (default USMF).",
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
    },
    "output_filename": {
      "description": "Excel workbook name, e.g. report-sell-product-subscriptions-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to summarize; defaults to the most recent posted period available.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_sell_product_subscriptions_agent.py` and embedded as the fenced Python below (sha256 a9e4e62cf8f7601d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_sell_product_subscriptions_agent.py` first:

```bash
python3 report_sell_product_subscriptions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_sell_product_subscriptions_agent.py   # or on stdin
python3 report_sell_product_subscriptions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Sell product subscriptions Summary Report — Builds a read-only summary report of sell product subscriptions from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-sell-product-subscriptions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_sell_product_subscriptions',
    "version": '3.0.3',
    "display_name": 'Sell product subscriptions Summary Report',
    "description": 'Builds a read-only summary report of sell product subscriptions from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.',
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
        "upstream_slug": 'report-sell-product-subscriptions',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-sell-product-subscriptions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3d398fdb338a119a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-sales-orders/sell-product-subscriptions'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/report-sell-product-subscriptions', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against (default USMF).', 'output_filename': 'Excel workbook name, e.g. report-sell-product-subscriptions-2026-05-24.xlsx.', 'period': 'Posted period to summarize; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where sell product subscriptions stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of sell product subscriptions for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-sell-product-subscriptions-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads sell product subscriptions records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of sell product subscriptions from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': "Build a sell product subscriptions summary report for USMF's latest posted period as an Excel workbook.", 'inputs': [{'description': 'D365 legal entity to report against (default USMF).', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Excel workbook name, e.g. report-sell-product-subscriptions-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write summary of sell product subscriptions activity in D365 ERP with totals, dimension breakdowns, and a Top 10 by value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportSellProductSubscriptions(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportSellProductSubscriptions'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook name, e.g. report-sell-product-subscriptions-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportSellProductSubscriptions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
