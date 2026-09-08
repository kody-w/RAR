---
name: "rar-cowork-cookbook-teams-update-reconcile-ledger-and-subledger"
description: "Summarizes ledger and subledger reconciliation status from the Dynamics 365 ERP plugin for a given legal entity and returns a draft Teams channel post plus an Adaptive Card JSON file saved for review, not posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_reconcile_ledger_and_subledger", "rar_sha256": "b8faff7a55cad9447188829e4d8c8d2300adc0f7663de5f8f76e9f46f62ef366", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_reconcile_ledger_and_subledger`. The original RAPP
agent is preserved byte-for-byte in `teams_update_reconcile_ledger_and_subledger_agent.py` and in the RCI capsule.

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

Reconcile ledger and subledger Teams Channel Update — Summarizes ledger and subledger reconciliation status from the Dynamics 365 ERP plugin for a given legal entity and returns a draft Teams channel post plus an Adaptive Card JSON file saved for review, not posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-reconcile-ledger-and-subledger
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
    "card_filename": {
      "description": "Filename for the Adaptive Card JSON artifact, e.g. teams-update-reconcile-ledger-and-subledger-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to reconcile against, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_reconcile_ledger_and_subledger_agent.py` and embedded as the fenced Python below (sha256 b8faff7a55cad944…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_reconcile_ledger_and_subledger_agent.py` first:

```bash
python3 teams_update_reconcile_ledger_and_subledger_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_reconcile_ledger_and_subledger_agent.py   # or on stdin
python3 teams_update_reconcile_ledger_and_subledger_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Reconcile ledger and subledger Teams Channel Update — Summarizes ledger and subledger reconciliation status from the Dynamics 365 ERP plugin for a given legal entity and returns a draft Teams channel post plus an Adaptive Card JSON file saved for review, not posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-reconcile-ledger-and-subledger
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_reconcile_ledger_and_subledger',
    "version": '3.0.3',
    "display_name": 'Reconcile ledger and subledger Teams Channel Update',
    "description": 'Summarizes ledger and subledger reconciliation status from the Dynamics 365 ERP plugin for a given legal entity and returns a draft Teams channel post plus an Adaptive Card JSON file saved for review, not posted.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-reconcile-ledger-and-subledger',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-reconcile-ledger-and-subledger',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8095e6ce0a318861',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/close-financial-periods/reconcile-ledger-and-subledger'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/teams-update-reconcile-ledger-and-subledger', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the Adaptive Card JSON artifact, e.g. teams-update-reconcile-ledger-and-subledger-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to reconcile against, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of reconcile ledger and subledger. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-reconcile-ledger-and-subledger-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads reconcile ledger and subledger, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes ledger and subledger reconciliation status from the Dynamics 365 ERP plugin for a given legal entity and returns a draft Teams channel post plus an Adaptive Card JSON file saved for review, not posted.', 'example_request': "Draft a Teams update on ledger and subledger reconciliation for USMF with an Adaptive Card, but don't post it.", 'inputs': [{'description': 'D365 legal entity to reconcile against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the Adaptive Card JSON artifact, e.g. teams-update-reconcile-ledger-and-subledger-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a ready-to-review Teams update on ledger/subledger reconciliation status in D365 F&SCM, with KPIs and quick-action buttons.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateReconcileLedgerAndSubledger(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateReconcileLedgerAndSubledger'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the Adaptive Card JSON artifact, e.g. teams-update-reconcile-ledger-and-subledger-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to reconcile against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateReconcileLedgerAndSubledger().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
