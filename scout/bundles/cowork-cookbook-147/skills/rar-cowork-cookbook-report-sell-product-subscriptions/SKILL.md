---
name: "rar-cowork-cookbook-report-sell-product-subscriptions"
description: "Builds a read-only summary report of sell product subscriptions from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_sell_product_subscriptions", "rar_sha256": "a9e4e62cf8f7601d040a1b81e2c37dbec6743b961007267e551f9854ef10e4ee", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
