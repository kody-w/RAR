---
name: "rar-cowork-cookbook-dashboard-define-performance-strategy"
description: "Pulls define-performance-strategy data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the outp"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_performance_strategy", "rar_sha256": "67d360abf3420837d03cc216fe6758477724d6086eba83bf8f4164c4b5ef8165", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_define_performance_strategy`. The original RAPP
agent is preserved byte-for-byte in `dashboard_define_performance_strategy_agent.py` and in the RCI capsule.

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

Define performance strategy Interactive HTML Dashboard — Pulls define-performance-strategy data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the outp

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-performance-strategy
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
      "description": "D365 legal entity to pull data from (e.g. USMF).",
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
      "description": "Name of the HTML file to write, e.g. dashboard-define-performance-strategy-2026-05-24.html.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_define_performance_strategy_agent.py` and embedded as the fenced Python below (sha256 67d360abf3420837…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_define_performance_strategy_agent.py` first:

```bash
python3 dashboard_define_performance_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_define_performance_strategy_agent.py   # or on stdin
python3 dashboard_define_performance_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define performance strategy Interactive HTML Dashboard — Pulls define-performance-strategy data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the outp

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-performance-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_define_performance_strategy',
    "version": '3.0.3',
    "display_name": 'Define performance strategy Interactive HTML Dashboard',
    "description": 'Pulls define-performance-strategy data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the outp',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-define-performance-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-define-performance-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b4fd47c1f60b947a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/define-performance-strategy'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-define-performance-strategy', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to pull data from (e.g. USMF).', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-define-performance-strategy-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML file (Documents/Cowork/output/).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of define performance strategy with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull define performance strategy data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-define-performance-strategy-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing define performance strategy.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls define-performance-strategy data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the outp', 'example_request': 'Build an interactive HTML dashboard for define performance strategy in USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to pull data from (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-define-performance-strategy-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML file (Documents/Cowork/output/).', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of define performance strategy data from D365 without giving the viewer D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardDefinePerformanceStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDefinePerformanceStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull data from (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-define-performance-strategy-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML file (Documents/Cowork/output/).', 'type': 'string'}},
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
    print(DashboardDefinePerformanceStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
