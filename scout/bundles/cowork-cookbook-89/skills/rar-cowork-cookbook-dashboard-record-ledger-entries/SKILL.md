---
name: "rar-cowork-cookbook-dashboard-record-ledger-entries"
description: "Pulls record ledger entries from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (totals header, SVG charts, sortable table, RAG indicator) to the"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_record_ledger_entries", "rar_sha256": "fc4d70eefcf75cc2790cd0ddf0933252f6de158f0ebae1ce6efe2000f229f72a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
