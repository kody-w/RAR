---
name: "rar-cowork-cookbook-scheduled-brief-reconcile-bank-accounts"
description: "Builds a bank reconciliation morning brief from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions; drafts an unsent email to the owner plus"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_reconcile_bank_accounts", "rar_sha256": "7f7dee72f7056812586242c52b12de06af5202151ea73fef9b0a3d53dfd2a7fa", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
