---
name: "rar-cowork-cookbook-scheduled-brief-calculate-sales-commissions"
description: "Builds a sales-commission morning brief from Dynamics 365 ERP data for legal entity USMF \u2014 top 5 items by impact, anomalies vs the 7-day rolling average, and next actions \u2014 then saves a draft email to the owner plus a Te"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_calculate_sales_commissions", "rar_sha256": "b49371843ffe4220a159c917574c40bbe736b87027e4e29bbe309be4da883f96", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_calculate_sales_commissions`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_calculate_sales_commissions_agent.py` and in the RCI capsule.

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

Calculate sales commissions Scheduled Email Brief — Builds a sales-commission morning brief from Dynamics 365 ERP data for legal entity USMF — top 5 items by impact, anomalies vs the 7-day rolling average, and next actions — then saves a draft email to the owner plus a Te

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-calculate-sales-commissions
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
      "description": "When the brief should run, e.g. weekday mornings at 7am.",
      "type": "string"
    },
    "teams_channel": {
      "description": "Optional Teams channel the summary post is intended for.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_calculate_sales_commissions_agent.py` and embedded as the fenced Python below (sha256 b49371843ffe4220…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_calculate_sales_commissions_agent.py` first:

```bash
python3 scheduled_brief_calculate_sales_commissions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_calculate_sales_commissions_agent.py   # or on stdin
python3 scheduled_brief_calculate_sales_commissions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Calculate sales commissions Scheduled Email Brief — Builds a sales-commission morning brief from Dynamics 365 ERP data for legal entity USMF — top 5 items by impact, anomalies vs the 7-day rolling average, and next actions — then saves a draft email to the owner plus a Te

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-calculate-sales-commissions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_calculate_sales_commissions',
    "version": '3.0.3',
    "display_name": 'Calculate sales commissions Scheduled Email Brief',
    "description": 'Builds a sales-commission morning brief from Dynamics 365 ERP data for legal entity USMF — top 5 items by impact, anomalies vs the 7-day rolling average, and next actions — then saves a draft email to the owner plus a Te',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-calculate-sales-commissions',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-calculate-sales-commissions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'aa4ef85ea7486ff3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/calculate-sales-commissions'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/scheduled-brief-calculate-sales-commissions', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When the brief should run, e.g. weekday mornings at 7am.', 'teams_channel': 'Optional Teams channel the summary post is intended for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where calculate sales commissions stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on calculate sales commissions for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads calculate sales commissions, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a sales-commission morning brief from Dynamics 365 ERP data for legal entity USMF — top 5 items by impact, anomalies vs the 7-day rolling average, and next actions — then saves a draft email to the owner plus a Te', 'example_request': 'Give me the daily sales commission brief for USMF and draft the email to the owner.', 'inputs': [{'description': 'Dynamics 365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'name': 'schedule'}, {'description': 'Optional Teams channel the summary post is intended for.', 'name': 'teams_channel'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a recurring (daily or weekday-morning) commission brief for the responsible owner, drafted as an email and a Teams channel post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefCalculateSalesCommissions(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefCalculateSalesCommissions'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'type': 'string'}, 'teams_channel': {'description': 'Optional Teams channel the summary post is intended for.', 'type': 'string'}},
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
    print(ScheduledBriefCalculateSalesCommissions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
