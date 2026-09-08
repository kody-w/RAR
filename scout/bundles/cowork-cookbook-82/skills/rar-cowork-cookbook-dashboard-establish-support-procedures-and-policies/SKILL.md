---
name: "rar-cowork-cookbook-dashboard-establish-support-procedures-and-policies"
description: "Pulls support procedures and policies data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the output folder; read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_establish_support_procedures_and_policies", "rar_sha256": "39d788c7d723c4cd54e0f2a83caf369605e985f350a541295f059e7fff1ad5cf", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_establish_support_procedures_and_policies`. The original RAPP
agent is preserved byte-for-byte in `dashboard_establish_support_procedures_and_policies_agent.py` and in the RCI capsule.

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

Establish support procedures and policies Interactive HTML Dashboard — Pulls support procedures and policies data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the output folder; read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-establish-support-procedures-and-policies
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
      "description": "Name of the generated HTML file, e.g. dashboard-establish-support-procedures-and-policies-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the HTML file; defaults to Documents/Cowork/output/ in OneDrive.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_establish_support_procedures_and_policies_agent.py` and embedded as the fenced Python below (sha256 39d788c7d723c4cd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_establish_support_procedures_and_policies_agent.py` first:

```bash
python3 dashboard_establish_support_procedures_and_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_establish_support_procedures_and_policies_agent.py   # or on stdin
python3 dashboard_establish_support_procedures_and_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Establish support procedures and policies Interactive HTML Dashboard — Pulls support procedures and policies data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the output folder; read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-establish-support-procedures-and-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_establish_support_procedures_and_policies',
    "version": '3.0.3',
    "display_name": 'Establish support procedures and policies Interactive HTML Dashboard',
    "description": 'Pulls support procedures and policies data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the output folder; read-only.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-establish-support-procedures-and-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-establish-support-procedures-and-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2c118a5edabde44e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/support-systems/establish-support-procedures-and-policies'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-establish-support-procedures-and-policies', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query; defaults to USMF.', 'output_filename': 'Name of the generated HTML file, e.g. dashboard-establish-support-procedures-and-policies-2026-05-24.html.', 'output_folder': 'Destination folder for the HTML file; defaults to Documents/Cowork/output/ in OneDrive.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of establish support procedures and policies with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull establish support procedures and policies data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-establish-support-procedures-and-policies-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing establish support procedures and policies.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls support procedures and policies data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the output folder; read-only.', 'example_request': 'Build an interactive HTML dashboard of support procedures and policies from D365 USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the generated HTML file, e.g. dashboard-establish-support-procedures-and-policies-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the HTML file; defaults to Documents/Cowork/output/ in OneDrive.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of support procedures and policies data from D365 without giving the viewer D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardEstablishSupportProceduresAndPolicies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardEstablishSupportProceduresAndPolicies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the generated HTML file, e.g. dashboard-establish-support-procedures-and-policies-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the HTML file; defaults to Documents/Cowork/output/ in OneDrive.', 'type': 'string'}},
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
    print(DashboardEstablishSupportProceduresAndPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
