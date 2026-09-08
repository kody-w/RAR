---
name: "rar-cowork-cookbook-planned-order-summary"
description: "Returns an Excel workbook summarizing planned production orders for the next 4 weeks aggregated by primary resource and week, with planned load hours vs configured capacity and weeks over 90% flagged."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/planned_order_summary", "rar_sha256": "35c22e7c40cfa37c1e2dda0220c350f72ff2db55eeb59862bea8ee4dc891957c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
