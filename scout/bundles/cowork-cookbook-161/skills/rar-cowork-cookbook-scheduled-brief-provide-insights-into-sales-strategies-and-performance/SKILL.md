---
name: "rar-cowork-cookbook-scheduled-brief-provide-insights-into-sales-strategies-and-performance"
description: "Builds a sales strategy and performance morning brief from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and next actions, saved as an email draft plus a Teams-ready s"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_provide_insights_into_sales_strategies_and_performance", "rar_sha256": "eae5010eff15bf5fd6bd7e9ad4cdbbf0691642913f89e619e1737f28e1080318", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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
