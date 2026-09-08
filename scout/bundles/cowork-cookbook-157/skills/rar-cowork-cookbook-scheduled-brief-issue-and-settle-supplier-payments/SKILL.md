---
name: "rar-cowork-cookbook-scheduled-brief-issue-and-settle-supplier-payments"
description: "Builds a morning brief on issuing and settling supplier payments from Dynamics 365 ERP for a legal entity, with top 5 items by impact, anomalies vs the 7-day average, next actions, an email draft, and a Teams-ready summa"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_issue_and_settle_supplier_payments", "rar_sha256": "ec60a0eff83ab658e32c80cd134f74ade5ccba33cb21ddbedd477c9923a8285c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_issue_and_settle_supplier_payments`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_issue_and_settle_supplier_payments_agent.py` and in the RCI capsule.

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

Issue and settle supplier payments Scheduled Email Brief — Builds a morning brief on issuing and settling supplier payments from Dynamics 365 ERP for a legal entity, with top 5 items by impact, anomalies vs the 7-day average, next actions, an email draft, and a Teams-ready summa

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-issue-and-settle-supplier-payments
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
      "description": "D365 legal entity to run against, e.g. USMF.",
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
      "description": "Optional cadence for the brief, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_issue_and_settle_supplier_payments_agent.py` and embedded as the fenced Python below (sha256 ec60a0eff83ab658…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_issue_and_settle_supplier_payments_agent.py` first:

```bash
python3 scheduled_brief_issue_and_settle_supplier_payments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_issue_and_settle_supplier_payments_agent.py   # or on stdin
python3 scheduled_brief_issue_and_settle_supplier_payments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Issue and settle supplier payments Scheduled Email Brief — Builds a morning brief on issuing and settling supplier payments from Dynamics 365 ERP for a legal entity, with top 5 items by impact, anomalies vs the 7-day average, next actions, an email draft, and a Teams-ready summa

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-issue-and-settle-supplier-payments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_issue_and_settle_supplier_payments',
    "version": '3.0.3',
    "display_name": 'Issue and settle supplier payments Scheduled Email Brief',
    "description": 'Builds a morning brief on issuing and settling supplier payments from Dynamics 365 ERP for a legal entity, with top 5 items by impact, anomalies vs the 7-day average, next actions, an email draft, and a Teams-ready summa',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-issue-and-settle-supplier-payments',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-issue-and-settle-supplier-payments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a944e50b29469cb4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-accounts-payable/issue-and-settle-supplier-payments'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/scheduled-brief-issue-and-settle-supplier-payments', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'Optional cadence for the brief, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where issue and settle supplier payments stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on issue and settle supplier payments for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads issue and settle supplier payments, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on issuing and settling supplier payments from Dynamics 365 ERP for a legal entity, with top 5 items by impact, anomalies vs the 7-day average, next actions, an email draft, and a Teams-ready summa', 'example_request': 'Give me the 7am supplier payment brief for USMF and draft the email to the owner.', 'inputs': [{'description': 'D365 legal entity to run against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'Optional cadence for the brief, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a daily or weekly supplier payment brief for the responsible owner, drafted as an email and a Teams channel post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefIssueAndSettleSupplierPayments(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefIssueAndSettleSupplierPayments'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for the brief, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefIssueAndSettleSupplierPayments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
