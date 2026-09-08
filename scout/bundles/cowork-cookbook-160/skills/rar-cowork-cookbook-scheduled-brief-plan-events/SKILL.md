---
name: "rar-cowork-cookbook-scheduled-brief-plan-events"
description: "Builds a morning brief on plan events for a responsible owner from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions, saved as an em"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_plan_events", "rar_sha256": "7964ca7942789eea0ee7bff34bf9821594c35e19ea44ac0b49377983e34c90e2", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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
