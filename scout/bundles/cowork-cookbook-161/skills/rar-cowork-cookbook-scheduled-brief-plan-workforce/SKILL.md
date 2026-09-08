---
name: "rar-cowork-cookbook-scheduled-brief-plan-workforce"
description: "Builds a workforce-planning morning brief from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, plus an email saved to drafts and a Teams-ready summ"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_plan_workforce", "rar_sha256": "f7d14246ae16721787f11b3c6120b1033c8cb967ad76be7e3a878a18e05d4a73", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
