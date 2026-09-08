---
name: "rar-cowork-cookbook-dashboard-define-depreciation-and-amortization-policies"
description: "Pulls depreciation and amortization policy data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the out"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_depreciation_and_amortization_policies", "rar_sha256": "02713ddfaa76f548c2925e8cbfa901e3c65bc8079e88e2855b15a54ed97baee5", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_define_depreciation_and_amortization_policies`. The original RAPP
agent is preserved byte-for-byte in `dashboard_define_depreciation_and_amortization_policies_agent.py` and in the RCI capsule.

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

Define depreciation and amortization policies Interactive HTML Dashboard — Pulls depreciation and amortization policy data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the out

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-depreciation-and-amortization-policies
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
      "description": "Name of the HTML file to write, e.g. dashboard-define-depreciation-and-amortization-policies-2026-05-24.html.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_define_depreciation_and_amortization_policies_agent.py` and embedded as the fenced Python below (sha256 02713ddfaa76f548…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_define_depreciation_and_amortization_policies_agent.py` first:

```bash
python3 dashboard_define_depreciation_and_amortization_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_define_depreciation_and_amortization_policies_agent.py   # or on stdin
python3 dashboard_define_depreciation_and_amortization_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define depreciation and amortization policies Interactive HTML Dashboard — Pulls depreciation and amortization policy data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the out

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-depreciation-and-amortization-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_define_depreciation_and_amortization_policies',
    "version": '3.0.3',
    "display_name": 'Define depreciation and amortization policies Interactive HTML Dashboard',
    "description": 'Pulls depreciation and amortization policy data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the out',
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
        "upstream_slug": 'dashboard-define-depreciation-and-amortization-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-define-depreciation-and-amortization-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'aebc8e176aa5cfa4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/define-asset-strategy/define-depreciation-and-amortization-policies'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/dashboard-define-depreciation-and-amortization-policies', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-define-depreciation-and-amortization-policies-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML file (Documents/Cowork/output/).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of define depreciation and amortization policies with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull define depreciation and amortization policies data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-define-depreciation-and-amortization-policies-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing define depreciation and amortization policies.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls depreciation and amortization policy data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the out', 'example_request': 'Build me an interactive HTML dashboard of depreciation and amortization policies for USMF, latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-define-depreciation-and-amortization-policies-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML file (Documents/Cowork/output/).', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of D365 depreciation and amortization policies for viewers without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardDefineDepreciationAndAmortizationPolicies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDefineDepreciationAndAmortizationPolicies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-define-depreciation-and-amortization-policies-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML file (Documents/Cowork/output/).', 'type': 'string'}},
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
    print(DashboardDefineDepreciationAndAmortizationPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
