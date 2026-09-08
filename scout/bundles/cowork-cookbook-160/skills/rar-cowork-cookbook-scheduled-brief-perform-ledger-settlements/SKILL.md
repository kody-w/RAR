---
name: "rar-cowork-cookbook-scheduled-brief-perform-ledger-settlements"
description: "Builds a morning brief on ledger settlements from Dynamics 365 ERP for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, saved as an email draft plus a Teams-ready summary."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_perform_ledger_settlements", "rar_sha256": "83e5777fe86c03cb4d9e9f6df8d6f27d126573ebf5e1d34c3f4c4797066a3c88", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_perform_ledger_settlements`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_perform_ledger_settlements_agent.py` and in the RCI capsule.

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

Perform ledger settlements Scheduled Email Brief — Builds a morning brief on ledger settlements from Dynamics 365 ERP for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, saved as an email draft plus a Teams-ready summary.

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-perform-ledger-settlements
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
      "description": "Dynamics 365 legal entity to query, e.g. USMF.",
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
      "description": "Responsible owner the brief is addressed to (email recipient of the draft).",
      "type": "string"
    },
    "schedule": {
      "description": "Optional cadence for the scheduled task, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_perform_ledger_settlements_agent.py` and embedded as the fenced Python below (sha256 83e5777fe86c03cb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_perform_ledger_settlements_agent.py` first:

```bash
python3 scheduled_brief_perform_ledger_settlements_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_perform_ledger_settlements_agent.py   # or on stdin
python3 scheduled_brief_perform_ledger_settlements_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Perform ledger settlements Scheduled Email Brief — Builds a morning brief on ledger settlements from Dynamics 365 ERP for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, saved as an email draft plus a Teams-ready summary.

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-perform-ledger-settlements
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_perform_ledger_settlements',
    "version": '3.0.3',
    "display_name": 'Perform ledger settlements Scheduled Email Brief',
    "description": 'Builds a morning brief on ledger settlements from Dynamics 365 ERP for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, saved as an email draft plus a Teams-ready summary.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-perform-ledger-settlements',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-perform-ledger-settlements',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f1da8c1fd644a69f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/close-financial-periods/perform-ledger-settlements'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/scheduled-brief-perform-ledger-settlements', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to query, e.g. USMF.', 'owner': 'Responsible owner the brief is addressed to (email recipient of the draft).', 'schedule': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where perform ledger settlements stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on perform ledger settlements for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads perform ledger settlements, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on ledger settlements from Dynamics 365 ERP for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, saved as an email draft plus a Teams-ready summary.', 'example_request': 'Draft my USMF ledger settlement morning brief for the owner and a Teams summary.', 'inputs': [{'description': 'Dynamics 365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner the brief is addressed to (email recipient of the draft).', 'name': 'owner'}, {'description': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a daily or weekly ledger settlement brief for the responsible owner, drafted as an email (not sent) and as a Teams channel post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefPerformLedgerSettlements(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefPerformLedgerSettlements'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner the brief is addressed to (email recipient of the draft).', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefPerformLedgerSettlements().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
