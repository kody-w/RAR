---
name: "rar-cowork-cookbook-dashboard-define-performance-strategy"
description: "Pulls define-performance-strategy data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the outp"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_performance_strategy", "rar_sha256": "67d360abf3420837d03cc216fe6758477724d6086eba83bf8f4164c4b5ef8165", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
