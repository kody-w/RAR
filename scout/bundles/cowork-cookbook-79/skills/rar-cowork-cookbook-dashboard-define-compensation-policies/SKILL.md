---
name: "rar-cowork-cookbook-dashboard-define-compensation-policies"
description: "Pulls compensation policy data from Dynamics 365 F&SCM (legal entity USMF, most recent fiscal period) read-only and saves a standalone interactive HTML dashboard with totals header, two inline SVG charts, sortable table,"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_compensation_policies", "rar_sha256": "64a1459ae93374a2f6507142635a1497f3f1777ab96cacec4ec7b404601593ba", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_define_compensation_policies`. The original RAPP
agent is preserved byte-for-byte in `dashboard_define_compensation_policies_agent.py` and in the RCI capsule.

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

Define compensation policies Interactive HTML Dashboard — Pulls compensation policy data from Dynamics 365 F&SCM (legal entity USMF, most recent fiscal period) read-only and saves a standalone interactive HTML dashboard with totals header, two inline SVG charts, sortable table,

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-compensation-policies
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
      "description": "D365 legal entity to pull from; the recipe uses USMF.",
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
      "description": "Name of the HTML file to write, e.g. dashboard-define-compensation-policies-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the file; defaults to Documents/Cowork/output/ in OneDrive.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_define_compensation_policies_agent.py` and embedded as the fenced Python below (sha256 64a1459ae93374a2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_define_compensation_policies_agent.py` first:

```bash
python3 dashboard_define_compensation_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_define_compensation_policies_agent.py   # or on stdin
python3 dashboard_define_compensation_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define compensation policies Interactive HTML Dashboard — Pulls compensation policy data from Dynamics 365 F&SCM (legal entity USMF, most recent fiscal period) read-only and saves a standalone interactive HTML dashboard with totals header, two inline SVG charts, sortable table,

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-compensation-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_define_compensation_policies',
    "version": '3.0.3',
    "display_name": 'Define compensation policies Interactive HTML Dashboard',
    "description": 'Pulls compensation policy data from Dynamics 365 F&SCM (legal entity USMF, most recent fiscal period) read-only and saves a standalone interactive HTML dashboard with totals header, two inline SVG charts, sortable table,',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-define-compensation-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-define-compensation-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '013090a79fe50bd6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-compensation-and-benefits/define-compensation-policies'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/dashboard-define-compensation-policies', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to pull from; the recipe uses USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-define-compensation-policies-2026-05-24.html.', 'output_folder': 'Destination folder for the file; defaults to Documents/Cowork/output/ in OneDrive.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of define compensation policies with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull define compensation policies data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-define-compensation-policies-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing define compensation policies.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls compensation policy data from Dynamics 365 F&SCM (legal entity USMF, most recent fiscal period) read-only and saves a standalone interactive HTML dashboard with totals header, two inline SVG charts, sortable table,', 'example_request': 'Build me an interactive HTML dashboard of compensation policies from D365 USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to pull from; the recipe uses USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-define-compensation-policies-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the file; defaults to Documents/Cowork/output/ in OneDrive.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of D365 compensation policy data for someone without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardDefineCompensationPolicies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDefineCompensationPolicies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull from; the recipe uses USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-define-compensation-policies-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the file; defaults to Documents/Cowork/output/ in OneDrive.', 'type': 'string'}},
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
    print(DashboardDefineCompensationPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
