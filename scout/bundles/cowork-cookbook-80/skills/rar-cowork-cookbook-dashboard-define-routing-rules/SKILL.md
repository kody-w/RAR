---
name: "rar-cowork-cookbook-dashboard-define-routing-rules"
description: "Pulls define routing rules data from Dynamics 365 F&SCM (read-only) for the most recent fiscal period and produces a standalone interactive HTML dashboard file saved to the Cowork output folder."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_routing_rules", "rar_sha256": "57c01df2c39b6c67776a3ae625d8ce7fb8ce78279b012f6dcaec1677d633d2ed", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_define_routing_rules`. The original RAPP
agent is preserved byte-for-byte in `dashboard_define_routing_rules_agent.py` and in the RCI capsule.

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

Define routing rules Interactive HTML Dashboard — Pulls define routing rules data from Dynamics 365 F&SCM (read-only) for the most recent fiscal period and produces a standalone interactive HTML dashboard file saved to the Cowork output folder.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-routing-rules
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
      "description": "Name of the generated HTML file, e.g. dashboard-define-routing-rules-2026-05-24.html.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_define_routing_rules_agent.py` and embedded as the fenced Python below (sha256 57c01df2c39b6c67…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_define_routing_rules_agent.py` first:

```bash
python3 dashboard_define_routing_rules_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_define_routing_rules_agent.py   # or on stdin
python3 dashboard_define_routing_rules_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define routing rules Interactive HTML Dashboard — Pulls define routing rules data from Dynamics 365 F&SCM (read-only) for the most recent fiscal period and produces a standalone interactive HTML dashboard file saved to the Cowork output folder.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-routing-rules
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_define_routing_rules',
    "version": '3.0.3',
    "display_name": 'Define routing rules Interactive HTML Dashboard',
    "description": 'Pulls define routing rules data from Dynamics 365 F&SCM (read-only) for the most recent fiscal period and produces a standalone interactive HTML dashboard file saved to the Cowork output folder.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-define-routing-rules',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-define-routing-rules',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2a7b16209f5c4da1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/define-customer-and-employee-service-operations/define-routing-rules'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/dashboard-define-routing-rules', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the generated HTML file, e.g. dashboard-define-routing-rules-2026-05-24.html.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of define routing rules with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull define routing rules data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-define-routing-rules-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing define routing rules.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls define routing rules data from Dynamics 365 F&SCM (read-only) for the most recent fiscal period and produces a standalone interactive HTML dashboard file saved to the Cowork output folder.', 'example_request': 'Build me an interactive HTML dashboard of define routing rules from D365 USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the generated HTML file, e.g. dashboard-define-routing-rules-2026-05-24.html.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of define routing rules data from D365 that viewers can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardDefineRoutingRules(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDefineRoutingRules'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the generated HTML file, e.g. dashboard-define-routing-rules-2026-05-24.html.', 'type': 'string'}},
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
    print(DashboardDefineRoutingRules().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
