---
name: "rar-cowork-cookbook-dashboard-correct-ledger-vouchers"
description: "Pulls correct ledger vouchers data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder, r"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_correct_ledger_vouchers", "rar_sha256": "8558856e50b1dc20b9d88ab687c8527617f88a0db9f26f416d17d14bb78e2efa", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_correct_ledger_vouchers`. The original RAPP
agent is preserved byte-for-byte in `dashboard_correct_ledger_vouchers_agent.py` and in the RCI capsule.

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

Correct ledger vouchers Interactive HTML Dashboard — Pulls correct ledger vouchers data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder, r

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-correct-ledger-vouchers
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
      "description": "Name of the HTML file to write, e.g. dashboard-correct-ledger-vouchers-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Folder where the HTML file is saved (Documents/Cowork/output).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_correct_ledger_vouchers_agent.py` and embedded as the fenced Python below (sha256 8558856e50b1dc20…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_correct_ledger_vouchers_agent.py` first:

```bash
python3 dashboard_correct_ledger_vouchers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_correct_ledger_vouchers_agent.py   # or on stdin
python3 dashboard_correct_ledger_vouchers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Correct ledger vouchers Interactive HTML Dashboard — Pulls correct ledger vouchers data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder, r

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-correct-ledger-vouchers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_correct_ledger_vouchers',
    "version": '3.0.3',
    "display_name": 'Correct ledger vouchers Interactive HTML Dashboard',
    "description": 'Pulls correct ledger vouchers data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder, r',
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
        "upstream_slug": 'dashboard-correct-ledger-vouchers',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-correct-ledger-vouchers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3e0416b7f38d1787',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/correct-ledger-vouchers'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/dashboard-correct-ledger-vouchers', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to pull; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-correct-ledger-vouchers-2026-05-24.html.', 'output_folder': 'Folder where the HTML file is saved (Documents/Cowork/output).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of correct ledger vouchers with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull correct ledger vouchers data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-correct-ledger-vouchers-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing correct ledger vouchers.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls correct ledger vouchers data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder, r', 'example_request': 'Build me an interactive HTML dashboard of correct ledger vouchers for USMF, latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to pull; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-correct-ledger-vouchers-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder where the HTML file is saved (Documents/Cowork/output).', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of correct ledger vouchers from D365 that viewers can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardCorrectLedgerVouchers(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardCorrectLedgerVouchers'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to pull; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-correct-ledger-vouchers-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder where the HTML file is saved (Documents/Cowork/output).', 'type': 'string'}},
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
    print(DashboardCorrectLedgerVouchers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
