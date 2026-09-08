---
name: "rar-cowork-cookbook-field-service-daily-utilization"
description: "Reads scheduled field-service work orders for today and the next 7 days, computes per-technician daily utilization, and returns a saved (unsent) email draft plus a Teams-ready summary of overbooked, underbooked, and unas"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/field_service_daily_utilization", "rar_sha256": "232c84c9e357105df06e3d6dda8bdac62a6f3f84dbb72b445d972e84710ee878", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
