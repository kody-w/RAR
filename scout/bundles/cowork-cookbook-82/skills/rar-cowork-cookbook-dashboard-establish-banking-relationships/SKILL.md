---
name: "rar-cowork-cookbook-dashboard-establish-banking-relationships"
description: "Pulls establish-banking-relationships data from Dynamics 365 F&SCM (legal entity USMF, most recent fiscal period) and writes a standalone interactive HTML dashboard with charts, a sortable table, and a RAG indicator to t"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_establish_banking_relationships", "rar_sha256": "e458c38e55ac5441c7cd334b9311356a43a79b8cc298e4c72a7fb12863f32765", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_establish_banking_relationships`. The original RAPP
agent is preserved byte-for-byte in `dashboard_establish_banking_relationships_agent.py` and in the RCI capsule.

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

Establish banking relationships Interactive HTML Dashboard — Pulls establish-banking-relationships data from Dynamics 365 F&SCM (legal entity USMF, most recent fiscal period) and writes a standalone interactive HTML dashboard with charts, a sortable table, and a RAG indicator to t

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-establish-banking-relationships
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
      "description": "Fiscal period to report on; defaults to the most recent available.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to query; defaults to USMF.",
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
      "description": "Name of the HTML file to write, e.g. dashboard-establish-banking-relationships-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the generated HTML, e.g. Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_establish_banking_relationships_agent.py` and embedded as the fenced Python below (sha256 e458c38e55ac5441…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_establish_banking_relationships_agent.py` first:

```bash
python3 dashboard_establish_banking_relationships_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_establish_banking_relationships_agent.py   # or on stdin
python3 dashboard_establish_banking_relationships_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Establish banking relationships Interactive HTML Dashboard — Pulls establish-banking-relationships data from Dynamics 365 F&SCM (legal entity USMF, most recent fiscal period) and writes a standalone interactive HTML dashboard with charts, a sortable table, and a RAG indicator to t

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-establish-banking-relationships
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_establish_banking_relationships',
    "version": '3.0.3',
    "display_name": 'Establish banking relationships Interactive HTML Dashboard',
    "description": 'Pulls establish-banking-relationships data from Dynamics 365 F&SCM (legal entity USMF, most recent fiscal period) and writes a standalone interactive HTML dashboard with charts, a sortable table, and a RAG indicator to t',
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
        "upstream_slug": 'dashboard-establish-banking-relationships',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-establish-banking-relationships',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '03b50cfb910e1e35',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-cash/establish-banking-relationships'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/dashboard-establish-banking-relationships', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query; defaults to USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-establish-banking-relationships-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of establish banking relationships with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull establish banking relationships data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-establish-banking-relationships-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing establish banking relationships.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls establish-banking-relationships data from Dynamics 365 F&SCM (legal entity USMF, most recent fiscal period) and writes a standalone interactive HTML dashboard with charts, a sortable table, and a RAG indicator to t', 'example_request': 'Build the establish banking relationships HTML dashboard for USMF from the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-establish-banking-relationships-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when someone needs a shareable browser-viewable dashboard of establish banking relationships from D365, without giving the viewer D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardEstablishBankingRelationships(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardEstablishBankingRelationships'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-establish-banking-relationships-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardEstablishBankingRelationships().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
