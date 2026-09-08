---
name: "rar-cowork-cookbook-dashboard-develop-procurement-policies"
description: "Pulls procurement policy data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and produces a standalone interactive HTML dashboard file, read-only, saved to the output folder."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_develop_procurement_policies", "rar_sha256": "84e1427066ad7f581781b6b65ff3b4b398047dda7c37a3bd8f81b13f0a1b8e1e", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
