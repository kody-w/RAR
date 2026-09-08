---
name: "rar-cowork-cookbook-scheduled-brief-plan-workforce"
description: "Builds a workforce-planning morning brief from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, plus an email saved to drafts and a Teams-ready summ"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_plan_workforce", "rar_sha256": "f7d14246ae16721787f11b3c6120b1033c8cb967ad76be7e3a878a18e05d4a73", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_plan_workforce`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_plan_workforce_agent.py` and in the RCI capsule.

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

Plan workforce Scheduled Email Brief — Builds a workforce-planning morning brief from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, plus an email saved to drafts and a Teams-ready summ

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-plan-workforce
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
      "description": "D365 legal entity to query; defaults to USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_plan_workforce_agent.py` and embedded as the fenced Python below (sha256 f7d14246ae167217…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_plan_workforce_agent.py` first:

```bash
python3 scheduled_brief_plan_workforce_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_plan_workforce_agent.py   # or on stdin
python3 scheduled_brief_plan_workforce_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan workforce Scheduled Email Brief — Builds a workforce-planning morning brief from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, plus an email saved to drafts and a Teams-ready summ

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-plan-workforce
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_plan_workforce',
    "version": '3.0.3',
    "display_name": 'Plan workforce Scheduled Email Brief',
    "description": 'Builds a workforce-planning morning brief from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, plus an email saved to drafts and a Teams-ready summ',
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
        "upstream_slug": 'scheduled-brief-plan-workforce',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-plan-workforce',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5a1b04b5204bdf4f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/develop-people-strategy/plan-workforce'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/scheduled-brief-plan-workforce', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When the brief should run, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where plan workforce stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on plan workforce for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads plan workforce, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a workforce-planning morning brief from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, plus an email saved to drafts and a Teams-ready summ', 'example_request': "Give me the USMF workforce plan morning brief for the owner and draft the email — don't send it.", 'inputs': [{'description': 'D365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Use for a recurring (daily/weekly, e.g. weekday 7am) workforce plan brief for the responsible owner, drafted as email and a Teams channel post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefPlanWorkforce(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefPlanWorkforce'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefPlanWorkforce().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
