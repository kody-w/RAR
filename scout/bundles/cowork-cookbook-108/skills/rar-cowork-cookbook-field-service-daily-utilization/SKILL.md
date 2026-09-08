---
name: "rar-cowork-cookbook-field-service-daily-utilization"
description: "Reads scheduled field-service work orders for today and the next 7 days, computes per-technician daily utilization, and returns a saved (unsent) email draft plus a Teams-ready summary of overbooked, underbooked, and unas"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/field_service_daily_utilization", "rar_sha256": "232c84c9e357105df06e3d6dda8bdac62a6f3f84dbb72b445d972e84710ee878", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/field_service_daily_utilization`. The original RAPP
agent is preserved byte-for-byte in `field_service_daily_utilization_agent.py` and in the RCI capsule.

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

Field Service Resource Utilization Daily Email — Reads scheduled field-service work orders for today and the next 7 days, computes per-technician daily utilization, and returns a saved (unsent) email draft plus a Teams-ready summary of overbooked, underbooked, and unas

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
  Upstream entry : https://coworkcookbook.com/recipes/field-service-daily-utilization
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
    "date_range": {
      "description": "Coverage window; defaults to today plus the next 7 days.",
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
    "overbooked_threshold": {
      "description": "Utilization percent above which a technician counts as overbooked; default 100%.",
      "type": "string"
    },
    "recipient": {
      "description": "The service operations manager the email draft is addressed to.",
      "type": "string"
    },
    "teams_channel": {
      "description": "Channel the Communications-ready summary is written for.",
      "type": "string"
    },
    "underbooked_threshold": {
      "description": "Utilization percent below which a technician counts as slack; default 50%.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `field_service_daily_utilization_agent.py` and embedded as the fenced Python below (sha256 232c84c9e357105d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `field_service_daily_utilization_agent.py` first:

```bash
python3 field_service_daily_utilization_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 field_service_daily_utilization_agent.py   # or on stdin
python3 field_service_daily_utilization_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Field Service Resource Utilization Daily Email — Reads scheduled field-service work orders for today and the next 7 days, computes per-technician daily utilization, and returns a saved (unsent) email draft plus a Teams-ready summary of overbooked, underbooked, and unas

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
  Upstream entry : https://coworkcookbook.com/recipes/field-service-daily-utilization
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/field_service_daily_utilization',
    "version": '3.0.3',
    "display_name": 'Field Service Resource Utilization Daily Email',
    "description": 'Reads scheduled field-service work orders for today and the next 7 days, computes per-technician daily utilization, and returns a saved (unsent) email draft plus a Teams-ready summary of overbooked, underbooked, and unas',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'field-service-daily-utilization',
        "upstream_url": 'https://coworkcookbook.com/recipes/field-service-daily-utilization',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c88ce0341ddceb53',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/manage-service-work'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/field-service-daily-utilization', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 Field Service or F&SCM Service module access', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: One email draft and one Communications summary covering technician utilization for the coming week.'], 'confidence': 1.0, 'deliverable': 'One email draft and one Communications summary covering technician utilization for the coming week.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_range': 'Coverage window; defaults to today plus the next 7 days.', 'overbooked_threshold': 'Utilization percent above which a technician counts as overbooked; default 100%.', 'recipient': 'The service operations manager the email draft is addressed to.', 'teams_channel': 'Channel the Communications-ready summary is written for.', 'underbooked_threshold': 'Utilization percent below which a technician counts as slack; default 50%.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic morning brief so dispatchers walk into standup already knowing who is overbooked, who has slack, and which jobs are at risk.', 'expected_output': 'One email draft and one Communications summary covering technician utilization for the coming week.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 Field Service or F&SCM Service module access', 'Cowork D365 ERP plugin enabled'], 'prompt': 'For each field-service technician, read scheduled work orders for today and the next 7 days. Compute: scheduled hours per day, configured working hours per day, and utilization percent. Identify: (a) technicians with utilization >100% on any day (overbooked), (b) technicians with utilization <50% on any day (slack), (c) work orders without an assigned technician. Draft an email to the service operations manager with three sections matching (a)/(b)/(c). Save the draft; do not send. Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong Cowork scheduled-task candidate — schedule for 6am each weekday.', 'steps': ['Paste the prompt in Cowork.', 'Review the email draft and Teams summary.', '(Optional) Schedule the task in Cowork to run at 6am weekdays.'], 'tenant_caveat': 'Validated end-to-end against a live Cowork tenant on 2026-05-23 with USMF. Cowork found the latest scheduled service date is 2016-12-30 and used the window 2016-12-01 to 2016-12-30. Roster: 2 technicians (Charlie Carson #000002, Ted Howard #000003). Real findings: (a) Overbooked - Charlie scheduled on Sat 2016-12-10 (1 hr on a non-working day against the 8h Mon-Fri baseline); (b) Slack - every weekday with scheduled work is at 12.5% or 0%, both technicians have ~18-21 weekdays in the window with zero scheduled work; (c) Unassigned - 0 of the 21 service order lines (all assigned). Email draft saved to Outlook (recipient blank since no service-ops-manager address is in the worker directory). Honesty notes: USMF has no published per-technician work calendar so the 8h Mon-Fri baseline is assumed; USMF has the Service Management module, not a dedicated Field Service module.', 'verified_against': 'm365.cloud.microsoft 2026-05-23', 'what_it_does': 'Builds a daily dispatch-ready utilization brief covering overbookings, slack, and unassigned work.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads scheduled field-service work orders for today and the next 7 days, computes per-technician daily utilization, and returns a saved (unsent) email draft plus a Teams-ready summary of overbooked, underbooked, and unas', 'example_request': "Draft my 6am field service utilization email for this week — who's overbooked, who's slack, and any unassigned work orders.", 'inputs': [{'description': 'The service operations manager the email draft is addressed to.', 'name': 'recipient'}, {'description': 'Coverage window; defaults to today plus the next 7 days.', 'name': 'date_range'}, {'description': 'Utilization percent above which a technician counts as overbooked; default 100%.', 'name': 'overbooked_threshold'}, {'description': 'Utilization percent below which a technician counts as slack; default 50%.', 'name': 'underbooked_threshold'}, {'description': 'Channel the Communications-ready summary is written for.', 'name': 'teams_channel'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a service operations team needs a daily or weekly technician utilization check covering overbooked resources, slack capacity, and unassigned work orders.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt in Cowork.', 'Review the email draft and Teams summary.', '(Optional) Schedule the task in Cowork to run at 6am weekdays.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class FieldServiceDailyUtilization(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'FieldServiceDailyUtilization'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_range': {'description': 'Coverage window; defaults to today plus the next 7 days.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'overbooked_threshold': {'description': 'Utilization percent above which a technician counts as overbooked; default 100%.', 'type': 'string'}, 'recipient': {'description': 'The service operations manager the email draft is addressed to.', 'type': 'string'}, 'teams_channel': {'description': 'Channel the Communications-ready summary is written for.', 'type': 'string'}, 'underbooked_threshold': {'description': 'Utilization percent below which a technician counts as slack; default 50%.', 'type': 'string'}},
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
    print(FieldServiceDailyUtilization().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
