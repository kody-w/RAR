---
name: "rar-cowork-cookbook-dashboard-establish-support-procedures-and-policies"
description: "Pulls support procedures and policies data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the output folder; read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_establish_support_procedures_and_policies", "rar_sha256": "39d788c7d723c4cd54e0f2a83caf369605e985f350a541295f059e7fff1ad5cf", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
