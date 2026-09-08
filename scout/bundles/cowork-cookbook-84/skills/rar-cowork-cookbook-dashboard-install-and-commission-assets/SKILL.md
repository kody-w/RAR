---
name: "rar-cowork-cookbook-dashboard-install-and-commission-assets"
description: "Pulls install and commission asset data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard to the output folder; read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_install_and_commission_assets", "rar_sha256": "a086fe504df84ec161b817cedc991e0a511453641ee325dc4d638fa0d9f11939", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_install_and_commission_assets`. The original RAPP
agent is preserved byte-for-byte in `dashboard_install_and_commission_assets_agent.py` and in the RCI capsule.

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

Install and commission assets Interactive HTML Dashboard — Pulls install and commission asset data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard to the output folder; read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-install-and-commission-assets
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
      "description": "Name of the HTML file to produce, e.g. dashboard-install-and-commission-assets-2026-05-24.html.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_install_and_commission_assets_agent.py` and embedded as the fenced Python below (sha256 a086fe504df84ec1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_install_and_commission_assets_agent.py` first:

```bash
python3 dashboard_install_and_commission_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_install_and_commission_assets_agent.py   # or on stdin
python3 dashboard_install_and_commission_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Install and commission assets Interactive HTML Dashboard — Pulls install and commission asset data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard to the output folder; read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-install-and-commission-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_install_and_commission_assets',
    "version": '3.0.3',
    "display_name": 'Install and commission assets Interactive HTML Dashboard',
    "description": 'Pulls install and commission asset data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard to the output folder; read-only.',
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
        "upstream_slug": 'dashboard-install-and-commission-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-install-and-commission-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6cc38541da636877',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/install-and-commission-assets'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/dashboard-install-and-commission-assets', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to produce, e.g. dashboard-install-and-commission-assets-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML file (Documents/Cowork/output/).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of install and commission assets with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull install and commission assets data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-install-and-commission-assets-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing install and commission assets.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls install and commission asset data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard to the output folder; read-only.', 'example_request': 'Build an interactive HTML dashboard of install and commission assets from D365 USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to produce, e.g. dashboard-install-and-commission-assets-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML file (Documents/Cowork/output/).', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of install and commission assets from D365 without giving the viewer D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardInstallAndCommissionAssets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardInstallAndCommissionAssets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to produce, e.g. dashboard-install-and-commission-assets-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML file (Documents/Cowork/output/).', 'type': 'string'}},
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
    print(DashboardInstallAndCommissionAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
