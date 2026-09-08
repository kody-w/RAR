---
name: "rar-cowork-cookbook-dashboard-manage-shifts"
description: "Pulls read-only manage shifts data for the most recent fiscal period from Dynamics 365 F&SCM via the Cowork ERP plugin and saves a standalone interactive HTML dashboard to the Cowork output folder."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_shifts", "rar_sha256": "3ed19fdd00fe96c77423eeaa7a39db00714b7ae364e7b084d724b396881497a7", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_manage_shifts`. The original RAPP
agent is preserved byte-for-byte in `dashboard_manage_shifts_agent.py` and in the RCI capsule.

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

Manage shifts Interactive HTML Dashboard — Pulls read-only manage shifts data for the most recent fiscal period from Dynamics 365 F&SCM via the Cowork ERP plugin and saves a standalone interactive HTML dashboard to the Cowork output folder.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-shifts
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
      "description": "Reporting period; defaults to the most recent fiscal period available.",
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
      "description": "Name of the generated HTML file, e.g. dashboard-manage-shifts-2026-05-24.html.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_shifts_agent.py` and embedded as the fenced Python below (sha256 3ed19fdd00fe96c7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_shifts_agent.py` first:

```bash
python3 dashboard_manage_shifts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_manage_shifts_agent.py   # or on stdin
python3 dashboard_manage_shifts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage shifts Interactive HTML Dashboard — Pulls read-only manage shifts data for the most recent fiscal period from Dynamics 365 F&SCM via the Cowork ERP plugin and saves a standalone interactive HTML dashboard to the Cowork output folder.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-shifts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_manage_shifts',
    "version": '3.0.3',
    "display_name": 'Manage shifts Interactive HTML Dashboard',
    "description": 'Pulls read-only manage shifts data for the most recent fiscal period from Dynamics 365 F&SCM via the Cowork ERP plugin and saves a standalone interactive HTML dashboard to the Cowork output folder.',
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
        "upstream_slug": 'dashboard-manage-shifts',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-manage-shifts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '970ef2a9523bc4e7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-time-and-attendance/manage-shifts'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/dashboard-manage-shifts', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Reporting period; defaults to the most recent fiscal period available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the generated HTML file, e.g. dashboard-manage-shifts-2026-05-24.html.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of manage shifts with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull manage shifts data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-manage-shifts-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing manage shifts.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls read-only manage shifts data for the most recent fiscal period from Dynamics 365 F&SCM via the Cowork ERP plugin and saves a standalone interactive HTML dashboard to the Cowork output folder.', 'example_request': 'Build me an interactive manage shifts dashboard from D365 USMF for the latest fiscal period as a standalone HTML file.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Reporting period; defaults to the most recent fiscal period available.', 'name': 'fiscal_period'}, {'description': 'Name of the generated HTML file, e.g. dashboard-manage-shifts-2026-05-24.html.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable manage shifts dashboard with charts, totals, sortable table and RAG status, without giving the viewer D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardManageShifts(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardManageShifts'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Reporting period; defaults to the most recent fiscal period available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the generated HTML file, e.g. dashboard-manage-shifts-2026-05-24.html.', 'type': 'string'}},
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
    print(DashboardManageShifts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
