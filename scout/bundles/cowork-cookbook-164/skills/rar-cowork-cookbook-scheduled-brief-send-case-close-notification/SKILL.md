---
name: "rar-cowork-cookbook-scheduled-brief-send-case-close-notification"
description: "Builds a morning brief on send case close notification from Dynamics 365 ERP (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then drafts an owner email (saved to"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_send_case_close_notification", "rar_sha256": "294ca509a0b79b3e63e19d5b1bdcfa83d6d90af68a6e35528e8cc30d6f72de8a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
