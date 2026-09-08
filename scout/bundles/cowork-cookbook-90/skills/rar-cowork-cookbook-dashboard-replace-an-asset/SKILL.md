---
name: "rar-cowork-cookbook-dashboard-replace-an-asset"
description: "Pulls replace-an-asset data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the output folder, read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_replace_an_asset", "rar_sha256": "757faab9381692e4c6d83431ccb86b9eebca1744fab5409b91e0a49f5454d052", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
