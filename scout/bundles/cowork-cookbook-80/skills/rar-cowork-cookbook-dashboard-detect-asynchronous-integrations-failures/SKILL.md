---
name: "rar-cowork-cookbook-dashboard-detect-asynchronous-integrations-failures"
description: "Pulls asynchronous integration failure data from Dynamics 365 F&SCM for a legal entity and fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output fold"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_detect_asynchronous_integrations_failures", "rar_sha256": "0d425bc4dbe1b51658e937884cff334715d8859139605a1a0c703ee01d17b464", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_detect_asynchronous_integrations_failures`. The original RAPP
agent is preserved byte-for-byte in `dashboard_detect_asynchronous_integrations_failures_agent.py` and in the RCI capsule.

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

Detect asynchronous integrations failures Interactive HTML Dashboard — Pulls asynchronous integration failure data from Dynamics 365 F&SCM for a legal entity and fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output fold

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-detect-asynchronous-integrations-failures
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
      "description": "Name of the HTML file to produce, e.g. dashboard-detect-asynchronous-integrations-failures-2026-05-24.html.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_detect_asynchronous_integrations_failures_agent.py` and embedded as the fenced Python below (sha256 0d425bc4dbe1b516…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_detect_asynchronous_integrations_failures_agent.py` first:

```bash
python3 dashboard_detect_asynchronous_integrations_failures_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_detect_asynchronous_integrations_failures_agent.py   # or on stdin
python3 dashboard_detect_asynchronous_integrations_failures_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Detect asynchronous integrations failures Interactive HTML Dashboard — Pulls asynchronous integration failure data from Dynamics 365 F&SCM for a legal entity and fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output fold

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-detect-asynchronous-integrations-failures
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_detect_asynchronous_integrations_failures',
    "version": '3.0.3',
    "display_name": 'Detect asynchronous integrations failures Interactive HTML Dashboard',
    "description": 'Pulls asynchronous integration failure data from Dynamics 365 F&SCM for a legal entity and fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output fold',
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
        "upstream_slug": 'dashboard-detect-asynchronous-integrations-failures',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-detect-asynchronous-integrations-failures',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4cf7a375ff30abff',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/monitor-systems-environments-and-capacity/detect-asynchronous-integrations-failures'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-detect-asynchronous-integrations-failures', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to pull; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to produce, e.g. dashboard-detect-asynchronous-integrations-failures-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML file (Documents/Cowork/output/).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of detect asynchronous integrations failures with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull detect asynchronous integrations failures data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-detect-asynchronous-integrations-failures-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing detect asynchronous integrations failures.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls asynchronous integration failure data from Dynamics 365 F&SCM for a legal entity and fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output fold', 'example_request': 'Build an HTML dashboard of asynchronous integration failures for USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to pull; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to produce, e.g. dashboard-detect-asynchronous-integrations-failures-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML file (Documents/Cowork/output/).', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of D365 asynchronous integration failures without giving the viewer D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardDetectAsynchronousIntegrationsFailures(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDetectAsynchronousIntegrationsFailures'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to pull; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to produce, e.g. dashboard-detect-asynchronous-integrations-failures-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML file (Documents/Cowork/output/).', 'type': 'string'}},
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
    print(DashboardDetectAsynchronousIntegrationsFailures().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
