---
name: "rar-cowork-cookbook-dashboard-record-ledger-entries"
description: "Pulls record ledger entries from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (totals header, SVG charts, sortable table, RAG indicator) to the"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_record_ledger_entries", "rar_sha256": "fc4d70eefcf75cc2790cd0ddf0933252f6de158f0ebae1ce6efe2000f229f72a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_record_ledger_entries`. The original RAPP
agent is preserved byte-for-byte in `dashboard_record_ledger_entries_agent.py` and in the RCI capsule.

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

Record ledger entries Interactive HTML Dashboard — Pulls record ledger entries from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (totals header, SVG charts, sortable table, RAG indicator) to the

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-record-ledger-entries
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
    "fiscal_period": {
      "description": "Fiscal period to pull; defaults to the most recent available.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to query, e.g. USMF.",
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
    "output_filename": {
      "description": "Name of the HTML file to write, e.g. dashboard-record-ledger-entries-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the generated HTML file (Documents/Cowork/output/).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_record_ledger_entries_agent.py` and embedded as the fenced Python below (sha256 fc4d70eefcf75cc2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_record_ledger_entries_agent.py` first:

```bash
python3 dashboard_record_ledger_entries_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_record_ledger_entries_agent.py   # or on stdin
python3 dashboard_record_ledger_entries_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record ledger entries Interactive HTML Dashboard — Pulls record ledger entries from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (totals header, SVG charts, sortable table, RAG indicator) to the

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-record-ledger-entries
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_record_ledger_entries',
    "version": '3.0.3',
    "display_name": 'Record ledger entries Interactive HTML Dashboard',
    "description": 'Pulls record ledger entries from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (totals header, SVG charts, sortable table, RAG indicator) to the',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-record-ledger-entries',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-record-ledger-entries',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bcfa1afdf7afc82b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/record-ledger-entries'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/dashboard-record-ledger-entries', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to pull; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-record-ledger-entries-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML file (Documents/Cowork/output/).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of record ledger entries with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull record ledger entries data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-record-ledger-entries-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing record ledger entries.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls record ledger entries from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (totals header, SVG charts, sortable table, RAG indicator) to the', 'example_request': 'Build me an HTML dashboard of record ledger entries for USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to pull; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-record-ledger-entries-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML file (Documents/Cowork/output/).', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants ledger entry data from D365 packaged as a browser-viewable HTML dashboard for people without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardRecordLedgerEntries(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardRecordLedgerEntries'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to pull; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-record-ledger-entries-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML file (Documents/Cowork/output/).', 'type': 'string'}},
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
    print(DashboardRecordLedgerEntries().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
