---
name: "rar-cowork-cookbook-scheduled-brief-plan-worker-retirement"
description: "Builds a morning brief on plan worker retirement from Dynamics 365 ERP data for a legal entity, covering top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the ow"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_plan_worker_retirement", "rar_sha256": "fc587753709dc6ab61cc121c35d64ffa0d98a2287767930a80f58ca82accaccc", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_plan_worker_retirement`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_plan_worker_retirement_agent.py` and in the RCI capsule.

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

Plan worker retirement Scheduled Email Brief — Builds a morning brief on plan worker retirement from Dynamics 365 ERP data for a legal entity, covering top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the ow

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-plan-worker-retirement
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
      "description": "Optional cadence for the brief, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_plan_worker_retirement_agent.py` and embedded as the fenced Python below (sha256 fc587753709dc6ab…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_plan_worker_retirement_agent.py` first:

```bash
python3 scheduled_brief_plan_worker_retirement_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_plan_worker_retirement_agent.py   # or on stdin
python3 scheduled_brief_plan_worker_retirement_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan worker retirement Scheduled Email Brief — Builds a morning brief on plan worker retirement from Dynamics 365 ERP data for a legal entity, covering top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the ow

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-plan-worker-retirement
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_plan_worker_retirement',
    "version": '3.0.3',
    "display_name": 'Plan worker retirement Scheduled Email Brief',
    "description": 'Builds a morning brief on plan worker retirement from Dynamics 365 ERP data for a legal entity, covering top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the ow',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-plan-worker-retirement',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-plan-worker-retirement',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ca5b339524e9dad1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/offboard-talent/plan-worker-retirement'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/scheduled-brief-plan-worker-retirement', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to query, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'Optional cadence for the brief, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where plan worker retirement stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on plan worker retirement for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads plan worker retirement, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on plan worker retirement from Dynamics 365 ERP data for a legal entity, covering top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the ow', 'example_request': 'Draft my weekday 7am plan worker retirement brief for USMF and email it to the owner as a draft.', 'inputs': [{'description': 'Dynamics 365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'Optional cadence for the brief, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a daily or weekly plan worker retirement brief drafted as an email (not sent) and a Teams channel summary from D365 F&SCM.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefPlanWorkerRetirement(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefPlanWorkerRetirement'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for the brief, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefPlanWorkerRetirement().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
