---
name: "rar-cowork-cookbook-dashboard-define-routing-rules"
description: "Pulls define routing rules data from Dynamics 365 F&SCM (read-only) for the most recent fiscal period and produces a standalone interactive HTML dashboard file saved to the Cowork output folder."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_routing_rules", "rar_sha256": "57c01df2c39b6c67776a3ae625d8ce7fb8ce78279b012f6dcaec1677d633d2ed", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
