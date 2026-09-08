---
name: "rar-cowork-cookbook-scheduled-brief-track-project-expenses"
description: "Builds a morning brief on project expenses from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a Teams-"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_track_project_expenses", "rar_sha256": "3406d863198d19f0bdf38b99d7c2c3cbe997fd141b9b9c339ddec2031b49dc1e", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
