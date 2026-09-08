---
name: "rar-cowork-cookbook-adaptive-card-record-ledger-entries"
description: "Generates a read-only Adaptive Card JSON file summarizing ledger entry status for a Dynamics 365 legal entity, with header, 3-5 KPI tiles, a RAG row, and action buttons; call to embed in Teams, Outlook, or dashboards."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_record_ledger_entries", "rar_sha256": "a04fae722e3ea1d21988c015df1c9d8c88af7502926bbed293d0c1e925f039a8", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
