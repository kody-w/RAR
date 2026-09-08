---
name: "rar-cowork-cookbook-teams-update-reconcile-ledger-and-subledger"
description: "Summarizes ledger and subledger reconciliation status from the Dynamics 365 ERP plugin for a given legal entity and returns a draft Teams channel post plus an Adaptive Card JSON file saved for review, not posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_reconcile_ledger_and_subledger", "rar_sha256": "b8faff7a55cad9447188829e4d8c8d2300adc0f7663de5f8f76e9f46f62ef366", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
