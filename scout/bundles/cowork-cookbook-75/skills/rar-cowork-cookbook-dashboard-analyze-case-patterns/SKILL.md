---
name: "rar-cowork-cookbook-dashboard-analyze-case-patterns"
description: "Pulls analyze case patterns data for the most recent fiscal period from Dynamics 365 F&SCM (via the Cowork D365 ERP plugin) and saves a standalone interactive HTML dashboard file, read-only, to the output folder."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_analyze_case_patterns", "rar_sha256": "e5a9faf5acce66dd533dd8c67cc736b2f9420c80afdf829bf5aa23d03dcf49b3", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
