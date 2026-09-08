---
name: "rar-cowork-cookbook-dashboard-install-and-commission-assets"
description: "Pulls install and commission asset data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard to the output folder; read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_install_and_commission_assets", "rar_sha256": "a086fe504df84ec161b817cedc991e0a511453641ee325dc4d638fa0d9f11939", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
