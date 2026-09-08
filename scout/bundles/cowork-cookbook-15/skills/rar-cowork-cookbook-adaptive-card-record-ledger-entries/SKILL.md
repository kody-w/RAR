---
name: "rar-cowork-cookbook-adaptive-card-record-ledger-entries"
description: "Generates a read-only Adaptive Card JSON file summarizing ledger entry status for a Dynamics 365 legal entity, with header, 3-5 KPI tiles, a RAG row, and action buttons; call to embed in Teams, Outlook, or dashboards."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_record_ledger_entries", "rar_sha256": "a04fae722e3ea1d21988c015df1c9d8c88af7502926bbed293d0c1e925f039a8", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_record_ledger_entries`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_record_ledger_entries_agent.py` and in the RCI capsule.

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

Record ledger entries Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing ledger entry status for a Dynamics 365 legal entity, with header, 3-5 KPI tiles, a RAG row, and action buttons; call to embed in Teams, Outlook, or dashboards.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-record-ledger-entries
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
    "as_of_date": {
      "description": "Date used for the snapshot and in the output file name.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to report on, e.g. USMF.",
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
    "output_file_name": {
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-record-ledger-entries-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_record_ledger_entries_agent.py` and embedded as the fenced Python below (sha256 a04fae722e3ea1d2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_record_ledger_entries_agent.py` first:

```bash
python3 adaptive_card_record_ledger_entries_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_record_ledger_entries_agent.py   # or on stdin
python3 adaptive_card_record_ledger_entries_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record ledger entries Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing ledger entry status for a Dynamics 365 legal entity, with header, 3-5 KPI tiles, a RAG row, and action buttons; call to embed in Teams, Outlook, or dashboards.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-record-ledger-entries
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_record_ledger_entries',
    "version": '3.0.2',
    "display_name": 'Record ledger entries Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing ledger entry status for a Dynamics 365 legal entity, with header, 3-5 KPI tiles, a RAG row, and action buttons; call to embed in Teams, Outlook, or dashboards.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'adaptive-card-record-ledger-entries',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-record-ledger-entries',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2cb068caaaabc9c6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/record-ledger-entries'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/adaptive-card-record-ledger-entries', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date used for the snapshot and in the output file name.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'output_file_name': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-record-ledger-entries-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical record ledger entries status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-record-ledger-entries-2026-05-24-card.json' that visualizes the current state of record ledger entries. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current record ledger entries KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing ledger entry status for a Dynamics 365 legal entity, with header, 3-5 KPI tiles, a RAG row, and action buttons; call to embed in Teams, Outlook, or dashboards.', 'example_request': 'Make an Adaptive Card JSON of ledger entry status for USMF as of 2026-05-24.', 'inputs': [{'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date used for the snapshot and in the output file name.', 'name': 'as_of_date'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-record-ledger-entries-2026-05-24-card.json.', 'name': 'output_file_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need a shareable Adaptive Card snapshot of record ledger entries status from Dynamics 365 F&SCM, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardRecordLedgerEntries(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardRecordLedgerEntries'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date used for the snapshot and in the output file name.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_file_name': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-record-ledger-entries-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardRecordLedgerEntries().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
