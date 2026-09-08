---
name: "rar-cowork-cookbook-dashboard-run-campaigns"
description: "Pulls run campaigns data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the ERP plugin and writes a standalone interactive HTML dashboard file to the output folder, read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_run_campaigns", "rar_sha256": "5bcb98ffe21a85a0a35e8f98bd9d787ce794907d6791734a1948f9e406b741eb", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_run_campaigns`. The original RAPP
agent is preserved byte-for-byte in `dashboard_run_campaigns_agent.py` and in the RCI capsule.

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

Run campaigns Interactive HTML Dashboard — Pulls run campaigns data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the ERP plugin and writes a standalone interactive HTML dashboard file to the output folder, read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-run-campaigns
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
      "description": "Name of the HTML file to write, e.g. dashboard-run-campaigns-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Folder where the HTML file is saved (Documents/Cowork/output/).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_run_campaigns_agent.py` and embedded as the fenced Python below (sha256 5bcb98ffe21a85a0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_run_campaigns_agent.py` first:

```bash
python3 dashboard_run_campaigns_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_run_campaigns_agent.py   # or on stdin
python3 dashboard_run_campaigns_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Run campaigns Interactive HTML Dashboard — Pulls run campaigns data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the ERP plugin and writes a standalone interactive HTML dashboard file to the output folder, read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-run-campaigns
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_run_campaigns',
    "version": '3.0.3',
    "display_name": 'Run campaigns Interactive HTML Dashboard',
    "description": 'Pulls run campaigns data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the ERP plugin and writes a standalone interactive HTML dashboard file to the output folder, read-only.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-run-campaigns',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-run-campaigns',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2e8c862b994bfb25',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/manage-marketing-campaigns/run-campaigns'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/dashboard-run-campaigns', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-run-campaigns-2026-05-24.html.', 'output_folder': 'Folder where the HTML file is saved (Documents/Cowork/output/).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of run campaigns with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull run campaigns data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-run-campaigns-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing run campaigns.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls run campaigns data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the ERP plugin and writes a standalone interactive HTML dashboard file to the output folder, read-only.', 'example_request': 'Build me an interactive HTML dashboard of run campaigns for USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-run-campaigns-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder where the HTML file is saved (Documents/Cowork/output/).', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of run campaigns data for viewers who have no D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardRunCampaigns(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardRunCampaigns'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-run-campaigns-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder where the HTML file is saved (Documents/Cowork/output/).', 'type': 'string'}},
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
    print(DashboardRunCampaigns().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
