---
name: "rar-cowork-cookbook-scheduled-brief-plan-worker-retirement"
description: "Builds a morning brief on plan worker retirement from Dynamics 365 ERP data for a legal entity, covering top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the ow"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_plan_worker_retirement", "rar_sha256": "fc587753709dc6ab61cc121c35d64ffa0d98a2287767930a80f58ca82accaccc", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
