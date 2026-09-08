---
name: "rar-cowork-cookbook-dashboard-replace-an-asset"
description: "Pulls replace-an-asset data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the output folder, read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_replace_an_asset", "rar_sha256": "757faab9381692e4c6d83431ccb86b9eebca1744fab5409b91e0a49f5454d052", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_replace_an_asset`. The original RAPP
agent is preserved byte-for-byte in `dashboard_replace_an_asset_agent.py` and in the RCI capsule.

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

Replace an asset Interactive HTML Dashboard — Pulls replace-an-asset data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the output folder, read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-replace-an-asset
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
      "description": "D365 legal entity to query; defaults to USMF.",
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
      "description": "Name of the HTML file to write, e.g. dashboard-replace-an-asset-2026-05-24.html.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_replace_an_asset_agent.py` and embedded as the fenced Python below (sha256 757faab9381692e4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_replace_an_asset_agent.py` first:

```bash
python3 dashboard_replace_an_asset_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_replace_an_asset_agent.py   # or on stdin
python3 dashboard_replace_an_asset_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Replace an asset Interactive HTML Dashboard — Pulls replace-an-asset data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the output folder, read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-replace-an-asset
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_replace_an_asset',
    "version": '3.0.3',
    "display_name": 'Replace an asset Interactive HTML Dashboard',
    "description": 'Pulls replace-an-asset data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the output folder, read-only.',
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
        "upstream_slug": 'dashboard-replace-an-asset',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-replace-an-asset',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8b97d4476a9aaec9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/dispose-of-assets/replace-an-asset'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/dashboard-replace-an-asset', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query; defaults to USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-replace-an-asset-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML file (Documents/Cowork/output/).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of replace an asset with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull replace an asset data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-replace-an-asset-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing replace an asset.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls replace-an-asset data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the output folder, read-only.', 'example_request': 'Build me the replace-an-asset HTML dashboard from D365 USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-replace-an-asset-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML file (Documents/Cowork/output/).', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of replace-an-asset data from D365 that viewers can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardReplaceAnAsset(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardReplaceAnAsset'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-replace-an-asset-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML file (Documents/Cowork/output/).', 'type': 'string'}},
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
    print(DashboardReplaceAnAsset().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
