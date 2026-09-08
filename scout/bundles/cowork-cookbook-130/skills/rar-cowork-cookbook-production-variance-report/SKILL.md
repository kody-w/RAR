---
name: "rar-cowork-cookbook-production-variance-report"
description: "Returns an Excel workbook comparing standard vs actual cost by category (material, routing, overhead) for production orders completed in the last 30 days, flagging variances over 5% of standard."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/production_variance_report", "rar_sha256": "449827a7cbcf3d9a31cf144cd855aa733b19514fca6ae6226113ca0b9b6adb4d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
