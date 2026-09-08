---
name: "rar-cowork-cookbook-dashboard-recruit-new-talent"
description: "Pulls recruit-new-talent data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and returns a standalone interactive HTML dashboard file with totals, inline SVG charts, sortable table, and RAG"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_recruit_new_talent", "rar_sha256": "afb66105e3053bf0f4280e03e0056ca83d82d09cf1e2c75ca6b530d0fb66bad6", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
