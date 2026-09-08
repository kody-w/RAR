---
name: "rar-cowork-cookbook-dashboard-maintain-asset-leases"
description: "Pulls maintain asset leases data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indica"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_maintain_asset_leases", "rar_sha256": "957b7fec09e1401bd0cd3eeaba4545d4087a7c7745b376a85306ef1d49cdf192", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
