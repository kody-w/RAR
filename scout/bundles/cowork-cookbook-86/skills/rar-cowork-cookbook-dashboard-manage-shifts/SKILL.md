---
name: "rar-cowork-cookbook-dashboard-manage-shifts"
description: "Pulls read-only manage shifts data for the most recent fiscal period from Dynamics 365 F&SCM via the Cowork ERP plugin and saves a standalone interactive HTML dashboard to the Cowork output folder."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_shifts", "rar_sha256": "3ed19fdd00fe96c77423eeaa7a39db00714b7ae364e7b084d724b396881497a7", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
