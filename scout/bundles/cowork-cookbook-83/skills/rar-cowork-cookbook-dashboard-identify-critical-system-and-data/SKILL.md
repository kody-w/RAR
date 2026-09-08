---
name: "rar-cowork-cookbook-dashboard-identify-critical-system-and-data"
description: "Pulls identify-critical-system-and-data records from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the out"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_identify_critical_system_and_data", "rar_sha256": "08839bf211f4f3289aece269507a24bae534d77fabea4f4559594499fc70bf27", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_identify_critical_system_and_data`. The original RAPP
agent is preserved byte-for-byte in `dashboard_identify_critical_system_and_data_agent.py` and in the RCI capsule.

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

Identify critical system and data Interactive HTML Dashboard — Pulls identify-critical-system-and-data records from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the out

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-identify-critical-system-and-data
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
      "description": "Name of the HTML file to write, e.g. dashboard-identify-critical-system-and-data-2026-05-24.html.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_identify_critical_system_and_data_agent.py` and embedded as the fenced Python below (sha256 08839bf211f4f328…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_identify_critical_system_and_data_agent.py` first:

```bash
python3 dashboard_identify_critical_system_and_data_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_identify_critical_system_and_data_agent.py   # or on stdin
python3 dashboard_identify_critical_system_and_data_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify critical system and data Interactive HTML Dashboard — Pulls identify-critical-system-and-data records from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the out

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-identify-critical-system-and-data
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_identify_critical_system_and_data',
    "version": '3.0.3',
    "display_name": 'Identify critical system and data Interactive HTML Dashboard',
    "description": 'Pulls identify-critical-system-and-data records from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the out',
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
        "upstream_slug": 'dashboard-identify-critical-system-and-data',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-identify-critical-system-and-data',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8d8037f26c03961f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/identify-critical-system-and-data'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-identify-critical-system-and-data', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-identify-critical-system-and-data-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of identify critical system and data with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull identify critical system and data data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-identify-critical-system-and-data-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing identify critical system and data.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls identify-critical-system-and-data records from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the out', 'example_request': 'Build an interactive HTML dashboard of critical system and data from D365 USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-identify-critical-system-and-data-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a browser-viewable D365 dashboard for critical system and data that someone without D365 access can open.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardIdentifyCriticalSystemAndData(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardIdentifyCriticalSystemAndData'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-identify-critical-system-and-data-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardIdentifyCriticalSystemAndData().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
