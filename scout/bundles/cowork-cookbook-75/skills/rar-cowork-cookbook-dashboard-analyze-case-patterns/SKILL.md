---
name: "rar-cowork-cookbook-dashboard-analyze-case-patterns"
description: "Pulls analyze case patterns data for the most recent fiscal period from Dynamics 365 F&SCM (via the Cowork D365 ERP plugin) and saves a standalone interactive HTML dashboard file, read-only, to the output folder."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_analyze_case_patterns", "rar_sha256": "e5a9faf5acce66dd533dd8c67cc736b2f9420c80afdf829bf5aa23d03dcf49b3", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_analyze_case_patterns`. The original RAPP
agent is preserved byte-for-byte in `dashboard_analyze_case_patterns_agent.py` and in the RCI capsule.

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

Analyze case patterns Interactive HTML Dashboard — Pulls analyze case patterns data for the most recent fiscal period from Dynamics 365 F&SCM (via the Cowork D365 ERP plugin) and saves a standalone interactive HTML dashboard file, read-only, to the output folder.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-analyze-case-patterns
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
      "description": "Name of the HTML file to write, e.g. dashboard-analyze-case-patterns-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the saved HTML, e.g. Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_analyze_case_patterns_agent.py` and embedded as the fenced Python below (sha256 e5a9faf5acce66dd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_analyze_case_patterns_agent.py` first:

```bash
python3 dashboard_analyze_case_patterns_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_analyze_case_patterns_agent.py   # or on stdin
python3 dashboard_analyze_case_patterns_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze case patterns Interactive HTML Dashboard — Pulls analyze case patterns data for the most recent fiscal period from Dynamics 365 F&SCM (via the Cowork D365 ERP plugin) and saves a standalone interactive HTML dashboard file, read-only, to the output folder.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-analyze-case-patterns
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_analyze_case_patterns',
    "version": '3.0.3',
    "display_name": 'Analyze case patterns Interactive HTML Dashboard',
    "description": 'Pulls analyze case patterns data for the most recent fiscal period from Dynamics 365 F&SCM (via the Cowork D365 ERP plugin) and saves a standalone interactive HTML dashboard file, read-only, to the output folder.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-analyze-case-patterns',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-analyze-case-patterns',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7b2e7376952cc3b5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/analyze-case-performance/analyze-case-patterns'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/dashboard-analyze-case-patterns', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to pull; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-analyze-case-patterns-2026-05-24.html.', 'output_folder': 'Destination folder for the saved HTML, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of analyze case patterns with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull analyze case patterns data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-analyze-case-patterns-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing analyze case patterns.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls analyze case patterns data for the most recent fiscal period from Dynamics 365 F&SCM (via the Cowork D365 ERP plugin) and saves a standalone interactive HTML dashboard file, read-only, to the output folder.', 'example_request': 'Build the analyze case patterns HTML dashboard for USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to pull; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-analyze-case-patterns-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the saved HTML, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of analyze case patterns from D365 ERP data, without the viewer needing D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardAnalyzeCasePatterns(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardAnalyzeCasePatterns'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to pull; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-analyze-case-patterns-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the saved HTML, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardAnalyzeCasePatterns().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
