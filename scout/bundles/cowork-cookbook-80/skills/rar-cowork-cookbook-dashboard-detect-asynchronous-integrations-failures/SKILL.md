---
name: "rar-cowork-cookbook-dashboard-detect-asynchronous-integrations-failures"
description: "Pulls asynchronous integration failure data from Dynamics 365 F&SCM for a legal entity and fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output fold"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_detect_asynchronous_integrations_failures", "rar_sha256": "0d425bc4dbe1b51658e937884cff334715d8859139605a1a0c703ee01d17b464", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
