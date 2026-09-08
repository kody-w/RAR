---
name: "rar-cowork-cookbook-dashboard-retire-software-licenses"
description: "Pulls retire software licenses data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the output folder, read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_retire_software_licenses", "rar_sha256": "8d727e6087233d799a0d1161b3f0f0b8ebe78d7b5c339370090abcca91beabc0", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_retire_software_licenses`. The original RAPP
agent is preserved byte-for-byte in `dashboard_retire_software_licenses_agent.py` and in the RCI capsule.

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

Retire software licenses Interactive HTML Dashboard — Pulls retire software licenses data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the output folder, read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-retire-software-licenses
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
      "description": "Fiscal period to pull; defaults to the most recent available.",
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
      "description": "Name of the HTML file to write, e.g. dashboard-retire-software-licenses-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the generated HTML, e.g. Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_retire_software_licenses_agent.py` and embedded as the fenced Python below (sha256 8d727e6087233d79…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_retire_software_licenses_agent.py` first:

```bash
python3 dashboard_retire_software_licenses_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_retire_software_licenses_agent.py   # or on stdin
python3 dashboard_retire_software_licenses_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Retire software licenses Interactive HTML Dashboard — Pulls retire software licenses data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the output folder, read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-retire-software-licenses
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_retire_software_licenses',
    "version": '3.0.3',
    "display_name": 'Retire software licenses Interactive HTML Dashboard',
    "description": 'Pulls retire software licenses data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the output folder, read-only.',
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
        "upstream_slug": 'dashboard-retire-software-licenses',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-retire-software-licenses',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4aad2a1630e10e7d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-licensing-and-entitlements/retire-software-licenses'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-retire-software-licenses', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to pull; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query; defaults to USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-retire-software-licenses-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of retire software licenses with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull retire software licenses data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-retire-software-licenses-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing retire software licenses.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls retire software licenses data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the output folder, read-only.', 'example_request': 'Build me an interactive HTML dashboard of retire software licenses from D365 USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to pull; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-retire-software-licenses-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of retire software licenses D365 data for viewers without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardRetireSoftwareLicenses(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardRetireSoftwareLicenses'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to pull; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-retire-software-licenses-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardRetireSoftwareLicenses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
