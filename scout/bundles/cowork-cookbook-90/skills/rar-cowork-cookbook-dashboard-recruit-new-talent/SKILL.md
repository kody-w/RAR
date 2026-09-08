---
name: "rar-cowork-cookbook-dashboard-recruit-new-talent"
description: "Pulls recruit-new-talent data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and returns a standalone interactive HTML dashboard file with totals, inline SVG charts, sortable table, and RAG"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_recruit_new_talent", "rar_sha256": "afb66105e3053bf0f4280e03e0056ca83d82d09cf1e2c75ca6b530d0fb66bad6", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_recruit_new_talent`. The original RAPP
agent is preserved byte-for-byte in `dashboard_recruit_new_talent_agent.py` and in the RCI capsule.

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

Recruit new talent Interactive HTML Dashboard — Pulls recruit-new-talent data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and returns a standalone interactive HTML dashboard file with totals, inline SVG charts, sortable table, and RAG

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-recruit-new-talent
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
      "description": "D365 legal entity to query; the recipe uses USMF.",
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
      "description": "Name of the HTML file to produce, e.g. dashboard-recruit-new-talent-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the saved HTML, typically Documents/Cowork/output/ in OneDrive.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_recruit_new_talent_agent.py` and embedded as the fenced Python below (sha256 afb66105e3053bf0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_recruit_new_talent_agent.py` first:

```bash
python3 dashboard_recruit_new_talent_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_recruit_new_talent_agent.py   # or on stdin
python3 dashboard_recruit_new_talent_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Recruit new talent Interactive HTML Dashboard — Pulls recruit-new-talent data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and returns a standalone interactive HTML dashboard file with totals, inline SVG charts, sortable table, and RAG

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-recruit-new-talent
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_recruit_new_talent',
    "version": '3.0.3',
    "display_name": 'Recruit new talent Interactive HTML Dashboard',
    "description": 'Pulls recruit-new-talent data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and returns a standalone interactive HTML dashboard file with totals, inline SVG charts, sortable table, and RAG',
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
        "upstream_slug": 'dashboard-recruit-new-talent',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-recruit-new-talent',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '202b00ad76ff463c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/recruit-and-onboard-talent/recruit-new-talent'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/dashboard-recruit-new-talent', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Reporting period; defaults to the most recent fiscal period available.', 'legal_entity': 'D365 legal entity to query; the recipe uses USMF.', 'output_filename': 'Name of the HTML file to produce, e.g. dashboard-recruit-new-talent-2026-05-24.html.', 'output_folder': 'Destination folder for the saved HTML, typically Documents/Cowork/output/ in OneDrive.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of recruit new talent with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull recruit new talent data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-recruit-new-talent-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing recruit new talent.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls recruit-new-talent data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and returns a standalone interactive HTML dashboard file with totals, inline SVG charts, sortable table, and RAG', 'example_request': 'Build me an interactive HTML dashboard of recruit new talent data from USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query; the recipe uses USMF.', 'name': 'legal_entity'}, {'description': 'Reporting period; defaults to the most recent fiscal period available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to produce, e.g. dashboard-recruit-new-talent-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the saved HTML, typically Documents/Cowork/output/ in OneDrive.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable, browser-viewable recruiting dashboard from D365 ERP data without giving the viewer D365 access. Read-only; no data is modified.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardRecruitNewTalent(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardRecruitNewTalent'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Reporting period; defaults to the most recent fiscal period available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query; the recipe uses USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to produce, e.g. dashboard-recruit-new-talent-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the saved HTML, typically Documents/Cowork/output/ in OneDrive.', 'type': 'string'}},
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
    print(DashboardRecruitNewTalent().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
