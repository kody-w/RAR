---
name: "rar-cowork-cookbook-scheduled-brief-provide-insights-into-sales-strategies-and-performance"
description: "Builds a sales strategy and performance morning brief from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and next actions, saved as an email draft plus a Teams-ready s"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_provide_insights_into_sales_strategies_and_performance", "rar_sha256": "eae5010eff15bf5fd6bd7e9ad4cdbbf0691642913f89e619e1737f28e1080318", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_provide_insights_into_sales_strategies_and_performance`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_provide_insights_into_sales_strategies_and_performance_agent.py` and in the RCI capsule.

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

Provide insights into sales strategies and performance Scheduled Email Brief — Builds a sales strategy and performance morning brief from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and next actions, saved as an email draft plus a Teams-ready s

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-provide-insights-into-sales-strategies-and-performance
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
      "description": "Dynamics 365 F&SCM legal entity to query; defaults to USMF.",
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
    "owner": {
      "description": "Responsible owner who receives the drafted email brief.",
      "type": "string"
    },
    "schedule": {
      "description": "When to run, e.g. weekday mornings at 7am, daily, or weekly.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_provide_insights_into_sales_strategies_and_performance_agent.py` and embedded as the fenced Python below (sha256 eae5010eff15bf5f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_provide_insights_into_sales_strategies_and_performance_agent.py` first:

```bash
python3 scheduled_brief_provide_insights_into_sales_strategies_and_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_provide_insights_into_sales_strategies_and_performance_agent.py   # or on stdin
python3 scheduled_brief_provide_insights_into_sales_strategies_and_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Provide insights into sales strategies and performance Scheduled Email Brief — Builds a sales strategy and performance morning brief from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and next actions, saved as an email draft plus a Teams-ready s

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-provide-insights-into-sales-strategies-and-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_provide_insights_into_sales_strategies_and_performance',
    "version": '3.0.3',
    "display_name": 'Provide insights into sales strategies and performance Scheduled Email Brief',
    "description": 'Builds a sales strategy and performance morning brief from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and next actions, saved as an email draft plus a Teams-ready s',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-provide-insights-into-sales-strategies-and-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-provide-insights-into-sales-strategies-and-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a033d143b9f1a002',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/analyze-sales/provide-insights-into-sales-strategies-and-performance'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/scheduled-brief-provide-insights-into-sales-strategies-and-performance', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 F&SCM legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When to run, e.g. weekday mornings at 7am, daily, or weekly.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where provide insights into sales strategies and performance stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on provide insights into sales strategies and performance for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads provide insights into sales strategies and performance, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a sales strategy and performance morning brief from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and next actions, saved as an email draft plus a Teams-ready s', 'example_request': 'Draft my USMF sales performance morning brief for weekday 7am and save it to drafts.', 'inputs': [{'description': 'Dynamics 365 F&SCM legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When to run, e.g. weekday mornings at 7am, daily, or weekly.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a sales owner wants a daily or weekly D365 sales performance brief drafted (not sent) for email and a Teams channel post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefProvideInsightsIntoSalesStrategiesAndPerformance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefProvideInsightsIntoSalesStrategiesAndPerformance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 F&SCM legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When to run, e.g. weekday mornings at 7am, daily, or weekly.', 'type': 'string'}},
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
    print(ScheduledBriefProvideInsightsIntoSalesStrategiesAndPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
