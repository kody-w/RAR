---
name: "rar-cowork-cookbook-dashboard-correct-ledger-vouchers"
description: "Pulls correct ledger vouchers data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder, r"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_correct_ledger_vouchers", "rar_sha256": "8558856e50b1dc20b9d88ab687c8527617f88a0db9f26f416d17d14bb78e2efa", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
