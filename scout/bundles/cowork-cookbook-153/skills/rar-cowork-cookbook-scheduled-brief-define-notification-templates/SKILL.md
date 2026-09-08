---
name: "rar-cowork-cookbook-scheduled-brief-define-notification-templates"
description: "Builds a morning brief on define notification templates from Dynamics 365 ERP (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions, then drafts an email t"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_notification_templates", "rar_sha256": "09ae0f71db9bdf18ccccb6f4deecafdd949612b39adc1279d131065a67603511", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_define_notification_templates`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_define_notification_templates_agent.py` and in the RCI capsule.

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

Define notification templates Scheduled Email Brief — Builds a morning brief on define notification templates from Dynamics 365 ERP (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions, then drafts an email t

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-notification-templates
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
      "description": "Dynamics 365 F&SCM legal entity to query; the recipe uses USMF.",
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
      "description": "When to run the brief, e.g. weekday mornings at 7am, daily or weekly.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_define_notification_templates_agent.py` and embedded as the fenced Python below (sha256 09ae0f71db9bdf18…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_define_notification_templates_agent.py` first:

```bash
python3 scheduled_brief_define_notification_templates_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_define_notification_templates_agent.py   # or on stdin
python3 scheduled_brief_define_notification_templates_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define notification templates Scheduled Email Brief — Builds a morning brief on define notification templates from Dynamics 365 ERP (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions, then drafts an email t

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-notification-templates
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_define_notification_templates',
    "version": '3.0.3',
    "display_name": 'Define notification templates Scheduled Email Brief',
    "description": 'Builds a morning brief on define notification templates from Dynamics 365 ERP (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions, then drafts an email t',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-define-notification-templates',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-define-notification-templates',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fdbafe8c8ef56ed1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-notifications-alerts/define-notification-templates'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-define-notification-templates', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 F&SCM legal entity to query; the recipe uses USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When to run the brief, e.g. weekday mornings at 7am, daily or weekly.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where define notification templates stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on define notification templates for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define notification templates, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on define notification templates from Dynamics 365 ERP (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions, then drafts an email t', 'example_request': 'Give me the 7am morning brief on define notification templates from USMF and draft the email to the owner.', 'inputs': [{'description': 'Dynamics 365 F&SCM legal entity to query; the recipe uses USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When to run the brief, e.g. weekday mornings at 7am, daily or weekly.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Use for a daily or weekly scheduled morning brief on define notification templates for the responsible owner, e.g. weekday mornings at 7am.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefDefineNotificationTemplates(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDefineNotificationTemplates'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 F&SCM legal entity to query; the recipe uses USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When to run the brief, e.g. weekday mornings at 7am, daily or weekly.', 'type': 'string'}},
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
    print(ScheduledBriefDefineNotificationTemplates().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
