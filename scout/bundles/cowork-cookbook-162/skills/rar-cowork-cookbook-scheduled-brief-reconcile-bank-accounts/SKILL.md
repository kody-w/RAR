---
name: "rar-cowork-cookbook-scheduled-brief-reconcile-bank-accounts"
description: "Builds a bank reconciliation morning brief from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions; drafts an unsent email to the owner plus"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_reconcile_bank_accounts", "rar_sha256": "7f7dee72f7056812586242c52b12de06af5202151ea73fef9b0a3d53dfd2a7fa", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_reconcile_bank_accounts`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_reconcile_bank_accounts_agent.py` and in the RCI capsule.

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

Reconcile bank accounts Scheduled Email Brief — Builds a bank reconciliation morning brief from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions; drafts an unsent email to the owner plus

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-reconcile-bank-accounts
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
      "description": "D365 legal entity to run against (recipe default: USMF).",
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
      "description": "When to run, e.g. weekday mornings at 7am, daily or weekly.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_reconcile_bank_accounts_agent.py` and embedded as the fenced Python below (sha256 7f7dee72f7056812…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_reconcile_bank_accounts_agent.py` first:

```bash
python3 scheduled_brief_reconcile_bank_accounts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_reconcile_bank_accounts_agent.py   # or on stdin
python3 scheduled_brief_reconcile_bank_accounts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Reconcile bank accounts Scheduled Email Brief — Builds a bank reconciliation morning brief from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions; drafts an unsent email to the owner plus

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-reconcile-bank-accounts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_reconcile_bank_accounts',
    "version": '3.0.3',
    "display_name": 'Reconcile bank accounts Scheduled Email Brief',
    "description": 'Builds a bank reconciliation morning brief from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions; drafts an unsent email to the owner plus',
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
        "upstream_slug": 'scheduled-brief-reconcile-bank-accounts',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-reconcile-bank-accounts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f73276a5c38af0e2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-cash/reconcile-bank-accounts'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/scheduled-brief-reconcile-bank-accounts', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (recipe default: USMF).', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When to run, e.g. weekday mornings at 7am, daily or weekly.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where reconcile bank accounts stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on reconcile bank accounts for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads reconcile bank accounts, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a bank reconciliation morning brief from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions; drafts an unsent email to the owner plus', 'example_request': 'Give me the 7am bank reconciliation brief for USMF and draft the email to the owner.', 'inputs': [{'description': 'D365 legal entity to run against (recipe default: USMF).', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When to run, e.g. weekday mornings at 7am, daily or weekly.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you want a daily or weekly bank reconciliation brief for the responsible owner, saved as an email draft and a Teams-postable summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefReconcileBankAccounts(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefReconcileBankAccounts'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (recipe default: USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When to run, e.g. weekday mornings at 7am, daily or weekly.', 'type': 'string'}},
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
    print(ScheduledBriefReconcileBankAccounts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
