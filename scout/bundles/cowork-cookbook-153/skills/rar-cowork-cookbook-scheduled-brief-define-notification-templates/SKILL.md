---
name: "rar-cowork-cookbook-scheduled-brief-define-notification-templates"
description: "Builds a morning brief on define notification templates from Dynamics 365 ERP (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions, then drafts an email t"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_notification_templates", "rar_sha256": "09ae0f71db9bdf18ccccb6f4deecafdd949612b39adc1279d131065a67603511", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
