---
name: "rar-cowork-cookbook-ppt-exec-develop-sales-pricing-strategy"
description: "Builds a read-only executive PowerPoint deck on sales pricing strategy from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_develop_sales_pricing_strategy", "rar_sha256": "d4535d43b7700096917da4a7024e29cc18bb4b2a58145c998d2df0ad4363303a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_develop_sales_pricing_strategy`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_develop_sales_pricing_strategy_agent.py` and in the RCI capsule.

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

Develop sales pricing strategy Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on sales pricing strategy from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-sales-pricing-strategy
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
    "comparison_period": {
      "description": "Prior period to trend against in the chart.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to pull data from, e.g. USMF.",
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
      "description": "Target .pptx filename, e.g. ppt-exec-develop-sales-pricing-strategy-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Length/cadence of the review the deck must fit, e.g. 15-minute monthly review.",
      "type": "string"
    },
    "topic": {
      "description": "Subject of the deck, e.g. develop sales pricing strategy.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_develop_sales_pricing_strategy_agent.py` and embedded as the fenced Python below (sha256 d4535d43b7700096…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_develop_sales_pricing_strategy_agent.py` first:

```bash
python3 ppt_exec_develop_sales_pricing_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_develop_sales_pricing_strategy_agent.py   # or on stdin
python3 ppt_exec_develop_sales_pricing_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop sales pricing strategy Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on sales pricing strategy from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-sales-pricing-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_develop_sales_pricing_strategy',
    "version": '3.0.3',
    "display_name": 'Develop sales pricing strategy Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on sales pricing strategy from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-develop-sales-pricing-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-develop-sales-pricing-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4438d8c65f699b19',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/develop-sales-policies/develop-sales-pricing-strategy'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/ppt-exec-develop-sales-pricing-strategy', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to trend against in the chart.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to pull data from, e.g. USMF.', 'output_filename': 'Target .pptx filename, e.g. ppt-exec-develop-sales-pricing-strategy-2026-05-24.pptx.', 'review_length': 'Length/cadence of the review the deck must fit, e.g. 15-minute monthly review.', 'topic': 'Subject of the deck, e.g. develop sales pricing strategy.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for develop sales pricing strategy reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on develop sales pricing strategy for a 15-minute monthly review. Produce 'ppt-exec-develop-sales-pricing-strategy-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads develop sales pricing strategy data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on sales pricing strategy from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.', 'example_request': 'Build an exec PowerPoint on our sales pricing strategy from D365 USMF for the 15-minute monthly review.', 'inputs': [{'description': 'D365 legal entity to pull data from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Subject of the deck, e.g. develop sales pricing strategy.', 'name': 'topic'}, {'description': 'Target .pptx filename, e.g. ppt-exec-develop-sales-pricing-strategy-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length/cadence of the review the deck must fit, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to trend against in the chart.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready pricing-strategy deck for a short monthly review, sourced from D365 F&SCM without modifying data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecDevelopSalesPricingStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDevelopSalesPricingStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to trend against in the chart.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull data from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Target .pptx filename, e.g. ppt-exec-develop-sales-pricing-strategy-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length/cadence of the review the deck must fit, e.g. 15-minute monthly review.', 'type': 'string'}, 'topic': {'description': 'Subject of the deck, e.g. develop sales pricing strategy.', 'type': 'string'}},
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
    print(PptExecDevelopSalesPricingStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
