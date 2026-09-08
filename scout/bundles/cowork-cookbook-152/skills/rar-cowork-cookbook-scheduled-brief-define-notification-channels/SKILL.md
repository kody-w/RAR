---
name: "rar-cowork-cookbook-scheduled-brief-define-notification-channels"
description: "Builds a morning brief on notification channels from Dynamics 365 ERP data for legal entity USMF: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to t"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_notification_channels", "rar_sha256": "245124d3ad9d22293a57ca52dc65d406e5396587bdcf45cc4baf0df6e4cbad36", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_define_notification_channels`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_define_notification_channels_agent.py` and in the RCI capsule.

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

Define notification channels Scheduled Email Brief — Builds a morning brief on notification channels from Dynamics 365 ERP data for legal entity USMF: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to t

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-notification-channels
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
      "description": "Responsible owner who receives the drafted brief email.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_define_notification_channels_agent.py` and embedded as the fenced Python below (sha256 245124d3ad9d2229…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_define_notification_channels_agent.py` first:

```bash
python3 scheduled_brief_define_notification_channels_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_define_notification_channels_agent.py   # or on stdin
python3 scheduled_brief_define_notification_channels_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define notification channels Scheduled Email Brief — Builds a morning brief on notification channels from Dynamics 365 ERP data for legal entity USMF: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to t

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-notification-channels
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_define_notification_channels',
    "version": '3.0.3',
    "display_name": 'Define notification channels Scheduled Email Brief',
    "description": 'Builds a morning brief on notification channels from Dynamics 365 ERP data for legal entity USMF: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to t',
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
        "upstream_slug": 'scheduled-brief-define-notification-channels',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-define-notification-channels',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '51f5af7b8ed74aae',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-notifications-alerts/define-notification-channels'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-define-notification-channels', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 F&SCM legal entity to query; the recipe uses USMF.', 'owner': 'Responsible owner who receives the drafted brief email.', 'schedule': 'When the brief should run, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where define notification channels stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on define notification channels for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define notification channels, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on notification channels from Dynamics 365 ERP data for legal entity USMF: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to t', 'example_request': 'Give me the 7am morning brief on notification channels in USMF and draft the email to the owner.', 'inputs': [{'description': 'Dynamics 365 F&SCM legal entity to query; the recipe uses USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted brief email.', 'name': 'owner'}, {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a responsible owner needs a daily or weekly ERP notification-channel brief with a drafted (unsent) email and a Teams channel post summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefDefineNotificationChannels(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDefineNotificationChannels'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 F&SCM legal entity to query; the recipe uses USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted brief email.', 'type': 'string'}, 'schedule': {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefDefineNotificationChannels().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
