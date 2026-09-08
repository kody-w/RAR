---
name: "rar-cowork-cookbook-scheduled-brief-perform-ledger-settlements"
description: "Builds a morning brief on ledger settlements from Dynamics 365 ERP for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, saved as an email draft plus a Teams-ready summary."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_perform_ledger_settlements", "rar_sha256": "83e5777fe86c03cb4d9e9f6df8d6f27d126573ebf5e1d34c3f4c4797066a3c88", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
