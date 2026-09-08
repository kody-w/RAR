---
name: "rar-cowork-cookbook-scheduled-brief-define-notification-channels"
description: "Builds a morning brief on notification channels from Dynamics 365 ERP data for legal entity USMF: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to t"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_notification_channels", "rar_sha256": "245124d3ad9d22293a57ca52dc65d406e5396587bdcf45cc4baf0df6e4cbad36", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
