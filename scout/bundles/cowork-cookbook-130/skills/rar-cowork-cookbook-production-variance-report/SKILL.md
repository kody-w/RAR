---
name: "rar-cowork-cookbook-production-variance-report"
description: "Returns an Excel workbook comparing standard vs actual cost by category (material, routing, overhead) for production orders completed in the last 30 days, flagging variances over 5% of standard."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/production_variance_report", "rar_sha256": "449827a7cbcf3d9a31cf144cd855aa733b19514fca6ae6226113ca0b9b6adb4d", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/production_variance_report`. The original RAPP
agent is preserved byte-for-byte in `production_variance_report_agent.py` and in the RCI capsule.

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

Production Cost Variance Report — Returns an Excel workbook comparing standard vs actual cost by category (material, routing, overhead) for production orders completed in the last 30 days, flagging variances over 5% of standard.

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
  Upstream entry : https://coworkcookbook.com/recipes/production-variance-report
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `production_variance_report_agent.py` and embedded as the fenced Python below (sha256 449827a7cbcf3d9a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `production_variance_report_agent.py` first:

```bash
python3 production_variance_report_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 production_variance_report_agent.py   # or on stdin
python3 production_variance_report_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Production Cost Variance Report — Returns an Excel workbook comparing standard vs actual cost by category (material, routing, overhead) for production orders completed in the last 30 days, flagging variances over 5% of standard.

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
  Upstream entry : https://coworkcookbook.com/recipes/production-variance-report
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/production_variance_report',
    "version": '3.0.3',
    "display_name": 'Production Cost Variance Report',
    "description": 'Returns an Excel workbook comparing standard vs actual cost by category (material, routing, overhead) for production orders completed in the last 30 days, flagging variances over 5% of standard.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'production-variance-report',
        "upstream_url": 'https://coworkcookbook.com/recipes/production-variance-report',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8ad4bde553f47ae1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/run-production-operations'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/production-variance-report', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the Production role', 'Output matches: Workbook with variances by category.'], 'confidence': 1.0, 'deliverable': 'Workbook with variances by category.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Identifies where standards are drifting from reality so engineering and cost accounting can fix the root cause, not just absorb the variance.', 'expected_output': 'Workbook with variances by category.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the Production role'], 'prompt': "For production orders completed in the last 30 days, compute the variance between standard cost and actual cost by category (material, routing, overhead). Flag orders where the absolute variance is greater than 5% of standard. Output an Excel workbook with a 'Material variances' sheet and an 'All' sheet.", 'steps': ['Paste the prompt.', 'Review with the production controller.'], 'tenant_caveat': 'Validated against a live Cowork tenant on 2026-05-23 with USMF. Cowork found 134 completed production orders in the 30-day window 2016-11-22 to 2016-12-18 (most recent in tenant). Honesty result: the canonical D365 cost-variance entity (ProdCalcTrans) is NOT exposed as a queryable OData entity in this tenant, so only routing variance is computable (904 estimated route transactions, 1,550 realized route transactions). Material variance requires ProjectCostAmount on picking-list-journal lines which is 0 for every row. Overhead has no indirect/surcharge transaction entity exposed. Cowork offered three options (routing-only with real numbers, all-three-sheets with placeholders, or pause until an admin exposes ProdCalcTrans). The screenshot captures the coverage diagnosis table - itself a deliverable that a controller can hand to the F&O admin to scope the entity-exposure work needed for a complete variance report.', 'verified_against': 'm365.cloud.microsoft 2026-05-23', 'what_it_does': 'Quantifies and flags production cost variance for completed orders.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Returns an Excel workbook comparing standard vs actual cost by category (material, routing, overhead) for production orders completed in the last 30 days, flagging variances over 5% of standard.', 'example_request': 'Build me a production cost variance report for orders completed in the last 30 days.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a production cost variance report on recently completed production orders in Dynamics 365 F&SCM.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt.', 'Review with the production controller.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ProductionVarianceReport(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ProductionVarianceReport'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ProductionVarianceReport().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
