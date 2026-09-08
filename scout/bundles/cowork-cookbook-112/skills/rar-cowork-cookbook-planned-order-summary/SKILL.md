---
name: "rar-cowork-cookbook-planned-order-summary"
description: "Returns an Excel workbook summarizing planned production orders for the next 4 weeks aggregated by primary resource and week, with planned load hours vs configured capacity and weeks over 90% flagged."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/planned_order_summary", "rar_sha256": "35c22e7c40cfa37c1e2dda0220c350f72ff2db55eeb59862bea8ee4dc891957c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/planned_order_summary`. The original RAPP
agent is preserved byte-for-byte in `planned_order_summary_agent.py` and in the RCI capsule.

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

Planned Order Summary by Resource — Returns an Excel workbook summarizing planned production orders for the next 4 weeks aggregated by primary resource and week, with planned load hours vs configured capacity and weeks over 90% flagged.

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
  Upstream entry : https://coworkcookbook.com/recipes/planned-order-summary
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `planned_order_summary_agent.py` and embedded as the fenced Python below (sha256 35c22e7c40cfa37c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `planned_order_summary_agent.py` first:

```bash
python3 planned_order_summary_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 planned_order_summary_agent.py   # or on stdin
python3 planned_order_summary_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Planned Order Summary by Resource — Returns an Excel workbook summarizing planned production orders for the next 4 weeks aggregated by primary resource and week, with planned load hours vs configured capacity and weeks over 90% flagged.

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
  Upstream entry : https://coworkcookbook.com/recipes/planned-order-summary
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/planned_order_summary',
    "version": '3.0.3',
    "display_name": 'Planned Order Summary by Resource',
    "description": 'Returns an Excel workbook summarizing planned production orders for the next 4 weeks aggregated by primary resource and week, with planned load hours vs configured capacity and weeks over 90% flagged.',
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
        "upstream_slug": 'planned-order-summary',
        "upstream_url": 'https://coworkcookbook.com/recipes/planned-order-summary',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b4ebe5ea87c70bfc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/plan-production-operations'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/planned-order-summary', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the Production role', 'Output matches: Workbook with data + summary sheet.'], 'confidence': 1.0, 'deliverable': 'Workbook with data + summary sheet.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives production planning a one-page view of where capacity is overcommitted, so the team can rebalance before missed promise dates pile up.', 'expected_output': 'Workbook with data + summary sheet.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the Production role'], 'prompt': 'List planned production orders for the next 4 weeks. Aggregate by primary resource and by week. Include the planned load in hours vs the configured capacity. Highlight any week where load > 90% of capacity. Produce an Excel workbook with a pivot-ready data sheet and a summary sheet.', 'steps': ['Paste the prompt.', 'Use the workbook in production planning meetings.'], 'tenant_caveat': "Validated end-to-end against a live Cowork tenant on 2026-05-23 with USMF (4-week window 2017-04-01 to 2017-04-28). Cowork ran all four plan steps and produced 'Planned-load-2026-05-23.xlsx' with a pivot-ready Data sheet and a Summary sheet (Resource x Week matrix). Findings: only two resources had planned-order capacity reservations - 1120 Cabinet assembly (80 hrs/wk, peak 3.5% utilization week 13) and 1220 Speaker test/packing (160 hrs/wk, peak 70.0% utilization weeks 14-15). No week exceeded the 90% threshold; the conditional red highlight rule is in place for future refreshes. Cowork deduplicated by RequirementPlanId=StaticPlan to avoid double-counting (StaticPlan and DynPlan mirror the same orders in USMF).", 'verified_against': 'm365.cloud.microsoft 2026-05-23', 'what_it_does': 'Capacity-and-load view of the planned production schedule.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Returns an Excel workbook summarizing planned production orders for the next 4 weeks aggregated by primary resource and week, with planned load hours vs configured capacity and weeks over 90% flagged.', 'example_request': 'Summarize planned production orders by resource for the next 4 weeks with load vs capacity in an Excel workbook.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Call when preparing production planning meetings and you need a 4-week planned order load vs capacity view by resource from Dynamics 365 F&SCM.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt.', 'Use the workbook in production planning meetings.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PlannedOrderSummary(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PlannedOrderSummary'
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
    print(PlannedOrderSummary().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
