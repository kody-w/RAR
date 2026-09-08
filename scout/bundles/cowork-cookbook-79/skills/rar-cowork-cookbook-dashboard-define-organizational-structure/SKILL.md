---
name: "rar-cowork-cookbook-dashboard-define-organizational-structure"
description: "Pulls organizational structure data from Dynamics 365 F&SCM for a given legal entity and fiscal period (read-only) and saves a standalone interactive HTML dashboard with totals, inline SVG charts, a sortable detail table"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_organizational_structure", "rar_sha256": "a5a04270fe04cf8c595ed761137bbc26e2ce3d8ec70464ef57fab831ff929f2b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_define_organizational_structure`. The original RAPP
agent is preserved byte-for-byte in `dashboard_define_organizational_structure_agent.py` and in the RCI capsule.

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

Define organizational structure Interactive HTML Dashboard — Pulls organizational structure data from Dynamics 365 F&SCM for a given legal entity and fiscal period (read-only) and saves a standalone interactive HTML dashboard with totals, inline SVG charts, a sortable detail table

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-organizational-structure
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
      "description": "Name of the HTML file to write, e.g. dashboard-define-organizational-structure-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Folder where the HTML file is saved, e.g. Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_define_organizational_structure_agent.py` and embedded as the fenced Python below (sha256 a5a04270fe04cf8c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_define_organizational_structure_agent.py` first:

```bash
python3 dashboard_define_organizational_structure_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_define_organizational_structure_agent.py   # or on stdin
python3 dashboard_define_organizational_structure_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define organizational structure Interactive HTML Dashboard — Pulls organizational structure data from Dynamics 365 F&SCM for a given legal entity and fiscal period (read-only) and saves a standalone interactive HTML dashboard with totals, inline SVG charts, a sortable detail table

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-organizational-structure
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_define_organizational_structure',
    "version": '3.0.3',
    "display_name": 'Define organizational structure Interactive HTML Dashboard',
    "description": 'Pulls organizational structure data from Dynamics 365 F&SCM for a given legal entity and fiscal period (read-only) and saves a standalone interactive HTML dashboard with totals, inline SVG charts, a sortable detail table',
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
        "upstream_slug": 'dashboard-define-organizational-structure',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-define-organizational-structure',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6c418468dcf1159c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/develop-people-strategy/define-organizational-structure'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/dashboard-define-organizational-structure', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to pull from, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-define-organizational-structure-2026-05-24.html.', 'output_folder': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of define organizational structure with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull define organizational structure data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-define-organizational-structure-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing define organizational structure.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls organizational structure data from Dynamics 365 F&SCM for a given legal entity and fiscal period (read-only) and saves a standalone interactive HTML dashboard with totals, inline SVG charts, a sortable detail table', 'example_request': 'Build an org structure dashboard from D365 for USMF for the latest fiscal period as a standalone HTML file.', 'inputs': [{'description': 'D365 legal entity to pull from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-define-organizational-structure-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a shareable browser-viewable dashboard of D365 organizational structure data for viewers who have no D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardDefineOrganizationalStructure(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDefineOrganizationalStructure'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-define-organizational-structure-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardDefineOrganizationalStructure().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
