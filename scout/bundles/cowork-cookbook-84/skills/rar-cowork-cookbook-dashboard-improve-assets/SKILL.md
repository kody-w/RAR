---
name: "rar-cowork-cookbook-dashboard-improve-assets"
description: "Pulls improve assets data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder, rea"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_improve_assets", "rar_sha256": "a1cf741dc2978d530a61ab1ef78f8cc04ec537f3769fcc3a8106822324471715", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
