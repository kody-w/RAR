---
name: "rar-cowork-cookbook-scheduled-brief-measure-frontline-worker-service-performance"
description: "Builds a morning brief on frontline worker service performance from Dynamics 365 ERP data for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; drafts an email to the o"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_measure_frontline_worker_service_performance", "rar_sha256": "1f7de1afec883e2b9d69552f31da8052073b28736333f1c9cd59e374f1a7de5e", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
