---
name: "rar-cowork-cookbook-dashboard-identify-critical-system-and-data"
description: "Pulls identify-critical-system-and-data records from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the out"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_identify_critical_system_and_data", "rar_sha256": "08839bf211f4f3289aece269507a24bae534d77fabea4f4559594499fc70bf27", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
