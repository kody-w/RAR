---
name: "rar-cowork-cookbook-scheduled-brief-calculate-sales-commissions"
description: "Builds a sales-commission morning brief from Dynamics 365 ERP data for legal entity USMF \u2014 top 5 items by impact, anomalies vs the 7-day rolling average, and next actions \u2014 then saves a draft email to the owner plus a Te"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_calculate_sales_commissions", "rar_sha256": "b49371843ffe4220a159c917574c40bbe736b87027e4e29bbe309be4da883f96", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
