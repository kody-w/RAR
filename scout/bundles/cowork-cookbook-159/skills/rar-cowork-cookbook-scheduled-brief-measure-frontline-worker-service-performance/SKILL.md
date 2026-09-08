---
name: "rar-cowork-cookbook-scheduled-brief-measure-frontline-worker-service-performance"
description: "Builds a morning brief on frontline worker service performance from Dynamics 365 ERP data for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; drafts an email to the o"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_measure_frontline_worker_service_performance", "rar_sha256": "1f7de1afec883e2b9d69552f31da8052073b28736333f1c9cd59e374f1a7de5e", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_measure_frontline_worker_service_performance`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_measure_frontline_worker_service_performance_agent.py` and in the RCI capsule.

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

Measure frontline worker service performance Scheduled Email Brief — Builds a morning brief on frontline worker service performance from Dynamics 365 ERP data for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; drafts an email to the o

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-measure-frontline-worker-service-performance
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
      "description": "Dynamics 365 legal entity to query, e.g. USMF.",
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
      "description": "When the brief should run, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_measure_frontline_worker_service_performance_agent.py` and embedded as the fenced Python below (sha256 1f7de1afec883e2b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_measure_frontline_worker_service_performance_agent.py` first:

```bash
python3 scheduled_brief_measure_frontline_worker_service_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_measure_frontline_worker_service_performance_agent.py   # or on stdin
python3 scheduled_brief_measure_frontline_worker_service_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Measure frontline worker service performance Scheduled Email Brief — Builds a morning brief on frontline worker service performance from Dynamics 365 ERP data for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; drafts an email to the o

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-measure-frontline-worker-service-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_measure_frontline_worker_service_performance',
    "version": '3.0.3',
    "display_name": 'Measure frontline worker service performance Scheduled Email Brief',
    "description": 'Builds a morning brief on frontline worker service performance from Dynamics 365 ERP data for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; drafts an email to the o',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-measure-frontline-worker-service-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-measure-frontline-worker-service-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'af536321665e1401',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/analyze-service-performance/measure-frontline-worker-service-performance'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/scheduled-brief-measure-frontline-worker-service-performance', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to query, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When the brief should run, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where measure frontline worker service performance stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on measure frontline worker service performance for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads measure frontline worker service performance, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on frontline worker service performance from Dynamics 365 ERP data for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; drafts an email to the o', 'example_request': 'Draft my 7am weekday frontline worker service performance brief from D365 USMF and email it to the owner.', 'inputs': [{'description': 'Dynamics 365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a daily or weekly frontline worker service performance brief drafted for the responsible owner from D365 F&SCM data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefMeasureFrontlineWorkerServicePerformance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefMeasureFrontlineWorkerServicePerformance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefMeasureFrontlineWorkerServicePerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
