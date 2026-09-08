---
name: "rar-cowork-cookbook-scheduled-brief-send-case-close-notification"
description: "Builds a morning brief on send case close notification from Dynamics 365 ERP (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then drafts an owner email (saved to"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_send_case_close_notification", "rar_sha256": "294ca509a0b79b3e63e19d5b1bdcfa83d6d90af68a6e35528e8cc30d6f72de8a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_send_case_close_notification`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_send_case_close_notification_agent.py` and in the RCI capsule.

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

Send case close notification Scheduled Email Brief — Builds a morning brief on send case close notification from Dynamics 365 ERP (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then drafts an owner email (saved to

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-send-case-close-notification
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
      "description": "Dynamics 365 legal entity to query; defaults to USMF.",
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
      "description": "When to run it, e.g. weekday mornings at 7am, daily or weekly.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_send_case_close_notification_agent.py` and embedded as the fenced Python below (sha256 294ca509a0b79b3e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_send_case_close_notification_agent.py` first:

```bash
python3 scheduled_brief_send_case_close_notification_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_send_case_close_notification_agent.py   # or on stdin
python3 scheduled_brief_send_case_close_notification_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Send case close notification Scheduled Email Brief — Builds a morning brief on send case close notification from Dynamics 365 ERP (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then drafts an owner email (saved to

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-send-case-close-notification
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_send_case_close_notification',
    "version": '3.0.3',
    "display_name": 'Send case close notification Scheduled Email Brief',
    "description": 'Builds a morning brief on send case close notification from Dynamics 365 ERP (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then drafts an owner email (saved to',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-send-case-close-notification',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-send-case-close-notification',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '091342490622e55a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/send-case-close-notification'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/scheduled-brief-send-case-close-notification', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When to run it, e.g. weekday mornings at 7am, daily or weekly.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where send case close notification stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on send case close notification for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads send case close notification, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on send case close notification from Dynamics 365 ERP (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then drafts an owner email (saved to', 'example_request': 'Give me the 7am morning brief on send case close notification for USMF and draft the email to the owner.', 'inputs': [{'description': 'Dynamics 365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When to run it, e.g. weekday mornings at 7am, daily or weekly.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a daily or weekly send case close notification brief for the responsible owner, as an email draft and Teams post summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefSendCaseCloseNotification(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefSendCaseCloseNotification'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When to run it, e.g. weekday mornings at 7am, daily or weekly.', 'type': 'string'}},
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
    print(ScheduledBriefSendCaseCloseNotification().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
