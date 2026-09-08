---
name: "rar-cowork-cookbook-dashboard-maintain-asset-leases"
description: "Pulls maintain asset leases data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indica"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_maintain_asset_leases", "rar_sha256": "957b7fec09e1401bd0cd3eeaba4545d4087a7c7745b376a85306ef1d49cdf192", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_maintain_asset_leases`. The original RAPP
agent is preserved byte-for-byte in `dashboard_maintain_asset_leases_agent.py` and in the RCI capsule.

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

Maintain asset leases Interactive HTML Dashboard — Pulls maintain asset leases data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indica

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-maintain-asset-leases
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
      "description": "D365 legal entity to pull from, e.g. USMF.",
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
      "description": "Name of the HTML file to write, e.g. dashboard-maintain-asset-leases-2026-05-24.html.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_maintain_asset_leases_agent.py` and embedded as the fenced Python below (sha256 957b7fec09e1401b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_maintain_asset_leases_agent.py` first:

```bash
python3 dashboard_maintain_asset_leases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_maintain_asset_leases_agent.py   # or on stdin
python3 dashboard_maintain_asset_leases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain asset leases Interactive HTML Dashboard — Pulls maintain asset leases data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indica

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-maintain-asset-leases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_maintain_asset_leases',
    "version": '3.0.3',
    "display_name": 'Maintain asset leases Interactive HTML Dashboard',
    "description": 'Pulls maintain asset leases data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indica',
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
        "upstream_slug": 'dashboard-maintain-asset-leases',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-maintain-asset-leases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '852ba15cffda3b5d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/manage-active-assets/maintain-asset-leases'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/dashboard-maintain-asset-leases', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to pull from, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-maintain-asset-leases-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of maintain asset leases with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull maintain asset leases data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-maintain-asset-leases-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing maintain asset leases.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls maintain asset leases data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indica', 'example_request': 'Build an interactive HTML dashboard of maintain asset leases for USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to pull from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-maintain-asset-leases-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of maintain asset leases data from D365 for viewers without D365 access. Read-only; no data is modified.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardMaintainAssetLeases(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardMaintainAssetLeases'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-maintain-asset-leases-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardMaintainAssetLeases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
