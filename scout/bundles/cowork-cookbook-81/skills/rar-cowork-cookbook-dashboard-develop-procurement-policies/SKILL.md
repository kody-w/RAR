---
name: "rar-cowork-cookbook-dashboard-develop-procurement-policies"
description: "Pulls procurement policy data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and produces a standalone interactive HTML dashboard file, read-only, saved to the output folder."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_develop_procurement_policies", "rar_sha256": "84e1427066ad7f581781b6b65ff3b4b398047dda7c37a3bd8f81b13f0a1b8e1e", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_develop_procurement_policies`. The original RAPP
agent is preserved byte-for-byte in `dashboard_develop_procurement_policies_agent.py` and in the RCI capsule.

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

Develop procurement policies Interactive HTML Dashboard — Pulls procurement policy data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and produces a standalone interactive HTML dashboard file, read-only, saved to the output folder.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-procurement-policies
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
      "description": "Name of the generated HTML file, e.g. dashboard-develop-procurement-policies-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the HTML file, e.g. Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_develop_procurement_policies_agent.py` and embedded as the fenced Python below (sha256 84e1427066ad7f58…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_develop_procurement_policies_agent.py` first:

```bash
python3 dashboard_develop_procurement_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_develop_procurement_policies_agent.py   # or on stdin
python3 dashboard_develop_procurement_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop procurement policies Interactive HTML Dashboard — Pulls procurement policy data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and produces a standalone interactive HTML dashboard file, read-only, saved to the output folder.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-procurement-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_develop_procurement_policies',
    "version": '3.0.3',
    "display_name": 'Develop procurement policies Interactive HTML Dashboard',
    "description": 'Pulls procurement policy data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and produces a standalone interactive HTML dashboard file, read-only, saved to the output folder.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-develop-procurement-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-develop-procurement-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a91ec23c13eea143',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/develop-procurement-and-sourcing-strategy/develop-procurement-policies'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/dashboard-develop-procurement-policies', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to pull from, e.g. USMF.', 'output_filename': 'Name of the generated HTML file, e.g. dashboard-develop-procurement-policies-2026-05-24.html.', 'output_folder': 'Destination folder for the HTML file, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of develop procurement policies with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull develop procurement policies data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-develop-procurement-policies-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing develop procurement policies.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls procurement policy data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and produces a standalone interactive HTML dashboard file, read-only, saved to the output folder.', 'example_request': 'Build an interactive HTML dashboard of procurement policies from D365 USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to pull from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the generated HTML file, e.g. dashboard-develop-procurement-policies-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the HTML file, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of D365 procurement policy data for viewers who have no D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardDevelopProcurementPolicies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDevelopProcurementPolicies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the generated HTML file, e.g. dashboard-develop-procurement-policies-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the HTML file, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardDevelopProcurementPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
