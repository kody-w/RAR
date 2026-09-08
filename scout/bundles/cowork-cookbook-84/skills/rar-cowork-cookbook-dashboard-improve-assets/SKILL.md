---
name: "rar-cowork-cookbook-dashboard-improve-assets"
description: "Pulls improve assets data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder, rea"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_improve_assets", "rar_sha256": "a1cf741dc2978d530a61ab1ef78f8cc04ec537f3769fcc3a8106822324471715", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_improve_assets`. The original RAPP
agent is preserved byte-for-byte in `dashboard_improve_assets_agent.py` and in the RCI capsule.

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

Improve assets Interactive HTML Dashboard — Pulls improve assets data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder, rea

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-improve-assets
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
      "description": "Name of the HTML file to write, e.g. dashboard-improve-assets-2026-05-24.html.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_improve_assets_agent.py` and embedded as the fenced Python below (sha256 a1cf741dc2978d53…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_improve_assets_agent.py` first:

```bash
python3 dashboard_improve_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_improve_assets_agent.py   # or on stdin
python3 dashboard_improve_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Improve assets Interactive HTML Dashboard — Pulls improve assets data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder, rea

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-improve-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_improve_assets',
    "version": '3.0.3',
    "display_name": 'Improve assets Interactive HTML Dashboard',
    "description": 'Pulls improve assets data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder, rea',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-improve-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-improve-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e819be424d16e07d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/manage-active-assets/improve-assets'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/dashboard-improve-assets', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-improve-assets-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of improve assets with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull improve assets data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-improve-assets-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing improve assets.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls improve assets data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder, rea', 'example_request': 'Build an improve assets HTML dashboard from D365 for USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-improve-assets-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone needs a shareable browser-viewable dashboard of improve assets data from D365 that viewers can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardImproveAssets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardImproveAssets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-improve-assets-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardImproveAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
