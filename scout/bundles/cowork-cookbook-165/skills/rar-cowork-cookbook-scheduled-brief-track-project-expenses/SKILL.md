---
name: "rar-cowork-cookbook-scheduled-brief-track-project-expenses"
description: "Builds a morning brief on project expenses from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a Teams-"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_track_project_expenses", "rar_sha256": "3406d863198d19f0bdf38b99d7c2c3cbe997fd141b9b9c339ddec2031b49dc1e", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_track_project_expenses`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_track_project_expenses_agent.py` and in the RCI capsule.

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

Track project expenses Scheduled Email Brief — Builds a morning brief on project expenses from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a Teams-

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-track-project-expenses
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_track_project_expenses_agent.py` and embedded as the fenced Python below (sha256 3406d863198d19f0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_track_project_expenses_agent.py` first:

```bash
python3 scheduled_brief_track_project_expenses_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_track_project_expenses_agent.py   # or on stdin
python3 scheduled_brief_track_project_expenses_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track project expenses Scheduled Email Brief — Builds a morning brief on project expenses from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a Teams-

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-track-project-expenses
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_track_project_expenses',
    "version": '3.0.3',
    "display_name": 'Track project expenses Scheduled Email Brief',
    "description": 'Builds a morning brief on project expenses from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a Teams-',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-track-project-expenses',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-track-project-expenses',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4b41793bc83ccd1d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/track-project-expenses'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/scheduled-brief-track-project-expenses', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 F&SCM legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When the brief should run, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where track project expenses stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on track project expenses for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads track project expenses, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on project expenses from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a Teams-', 'example_request': 'Draft my 7am weekday project expense brief from D365 USMF and email it to the owner as a draft.', 'inputs': [{'description': 'Dynamics 365 F&SCM legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a recurring (daily/weekly, e.g. weekday 7am) project-expense brief for the responsible owner, drafted as an email and a Teams channel post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefTrackProjectExpenses(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefTrackProjectExpenses'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 F&SCM legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefTrackProjectExpenses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
