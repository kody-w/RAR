---
name: "rar-cowork-cookbook-scheduled-brief-plan-events"
description: "Builds a morning brief on plan events for a responsible owner from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions, saved as an em"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_plan_events", "rar_sha256": "7964ca7942789eea0ee7bff34bf9821594c35e19ea44ac0b49377983e34c90e2", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_plan_events`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_plan_events_agent.py` and in the RCI capsule.

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

Plan events Scheduled Email Brief — Builds a morning brief on plan events for a responsible owner from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions, saved as an em

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-plan-events
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
      "description": "D365 F&SCM legal entity to query; defaults to USMF.",
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
      "description": "Responsible owner who receives the brief email draft.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_plan_events_agent.py` and embedded as the fenced Python below (sha256 7964ca7942789eea…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_plan_events_agent.py` first:

```bash
python3 scheduled_brief_plan_events_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_plan_events_agent.py   # or on stdin
python3 scheduled_brief_plan_events_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan events Scheduled Email Brief — Builds a morning brief on plan events for a responsible owner from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions, saved as an em

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-plan-events
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_plan_events',
    "version": '3.0.3',
    "display_name": 'Plan events Scheduled Email Brief',
    "description": 'Builds a morning brief on plan events for a responsible owner from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions, saved as an em',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-plan-events',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-plan-events',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '13ce6a56c61d719b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/plan-events'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/scheduled-brief-plan-events', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 F&SCM legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the brief email draft.', 'schedule': 'When the brief should run, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where plan events stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on plan events for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads plan events, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on plan events for a responsible owner from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions, saved as an em', 'example_request': 'Give me the plan events morning brief for USMF and draft it to the owner.', 'inputs': [{'description': 'D365 F&SCM legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the brief email draft.', 'name': 'owner'}, {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a daily or weekly plan-events brief for the responsible owner in D365 USMF, drafted as an email and a Teams channel post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefPlanEvents(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefPlanEvents'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the brief email draft.', 'type': 'string'}, 'schedule': {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefPlanEvents().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
