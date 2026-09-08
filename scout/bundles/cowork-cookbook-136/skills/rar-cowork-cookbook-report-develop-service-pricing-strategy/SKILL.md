---
name: "rar-cowork-cookbook-report-develop-service-pricing-strategy"
description: "Builds a read-only service pricing strategy summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_develop_service_pricing_strategy", "rar_sha256": "8bf730aac3bd9611ec16be50c340578447d5496913bd4b1b96b08fc3840618ee", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_develop_service_pricing_strategy`. The original RAPP
agent is preserved byte-for-byte in `report_develop_service_pricing_strategy_agent.py` and in the RCI capsule.

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

Develop service pricing strategy Summary Report — Builds a read-only service pricing strategy summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-develop-service-pricing-strategy
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
      "description": "Dynamics 365 legal entity to report against (default USMF).",
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
      "description": "Name of the Excel workbook to produce, e.g. report-develop-service-pricing-strategy-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to summarize; defaults to the most recent posted period available in the tenant.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_develop_service_pricing_strategy_agent.py` and embedded as the fenced Python below (sha256 8bf730aac3bd9611…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_develop_service_pricing_strategy_agent.py` first:

```bash
python3 report_develop_service_pricing_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_develop_service_pricing_strategy_agent.py   # or on stdin
python3 report_develop_service_pricing_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop service pricing strategy Summary Report — Builds a read-only service pricing strategy summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-develop-service-pricing-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_develop_service_pricing_strategy',
    "version": '3.0.3',
    "display_name": 'Develop service pricing strategy Summary Report',
    "description": 'Builds a read-only service pricing strategy summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-develop-service-pricing-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-develop-service-pricing-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '91774cf69a923a15',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/develop-service-pricing-strategy'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/report-develop-service-pricing-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report against (default USMF).', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-develop-service-pricing-strategy-2026-05-24.xlsx.', 'period': 'Posted period to summarize; defaults to the most recent posted period available in the tenant.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where develop service pricing strategy stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of develop service pricing strategy for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-develop-service-pricing-strategy-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads develop service pricing strategy records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only service pricing strategy summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': "Build the develop service pricing strategy summary report for USMF's latest posted period as an Excel workbook.", 'inputs': [{'description': 'Dynamics 365 legal entity to report against (default USMF).', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available in the tenant.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-develop-service-pricing-strategy-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write D365 ERP summary of develop service pricing strategy activity with totals, by-dimension breakdowns, and a Top 10 by value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportDevelopServicePricingStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDevelopServicePricingStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report against (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-develop-service-pricing-strategy-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to summarize; defaults to the most recent posted period available in the tenant.', 'type': 'string'}},
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
    print(ReportDevelopServicePricingStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
