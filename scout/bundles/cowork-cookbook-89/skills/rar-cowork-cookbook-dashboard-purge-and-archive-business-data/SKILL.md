---
name: "rar-cowork-cookbook-dashboard-purge-and-archive-business-data"
description: "Pulls purge-and-archive business data from Dynamics 365 F&SCM for a legal entity's most recent fiscal period and saves a standalone interactive HTML dashboard (charts, sortable table, RAG indicator) to the output folder;"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_purge_and_archive_business_data", "rar_sha256": "0bc7310fee65d1dd50932655312ef9582b61f034ef77a8c570cf925f4e1fb772", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_purge_and_archive_business_data`. The original RAPP
agent is preserved byte-for-byte in `dashboard_purge_and_archive_business_data_agent.py` and in the RCI capsule.

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

Purge and archive business data Interactive HTML Dashboard — Pulls purge-and-archive business data from Dynamics 365 F&SCM for a legal entity's most recent fiscal period and saves a standalone interactive HTML dashboard (charts, sortable table, RAG indicator) to the output folder;

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-purge-and-archive-business-data
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
      "description": "Period to report on; defaults to the most recent fiscal period available.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to pull data from, e.g. USMF.",
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
      "description": "Name of the HTML file to write, e.g. dashboard-purge-and-archive-business-data-2026-05-24.html.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_purge_and_archive_business_data_agent.py` and embedded as the fenced Python below (sha256 0bc7310fee65d1dd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_purge_and_archive_business_data_agent.py` first:

```bash
python3 dashboard_purge_and_archive_business_data_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_purge_and_archive_business_data_agent.py   # or on stdin
python3 dashboard_purge_and_archive_business_data_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Purge and archive business data Interactive HTML Dashboard — Pulls purge-and-archive business data from Dynamics 365 F&SCM for a legal entity's most recent fiscal period and saves a standalone interactive HTML dashboard (charts, sortable table, RAG indicator) to the output folder;

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-purge-and-archive-business-data
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_purge_and_archive_business_data',
    "version": '3.0.3',
    "display_name": 'Purge and archive business data Interactive HTML Dashboard',
    "description": "Pulls purge-and-archive business data from Dynamics 365 F&SCM for a legal entity's most recent fiscal period and saves a standalone interactive HTML dashboard (charts, sortable table, RAG indicator) to the output folder;",
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
        "upstream_slug": 'dashboard-purge-and-archive-business-data',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-purge-and-archive-business-data',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c5286ee16b63ff90',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/monitor-systems-environments-and-capacity/purge-and-archive-business-data'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-purge-and-archive-business-data', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Period to report on; defaults to the most recent fiscal period available.', 'legal_entity': 'D365 legal entity to pull data from, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-purge-and-archive-business-data-2026-05-24.html.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of purge and archive business data with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull purge and archive business data data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-purge-and-archive-business-data-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing purge and archive business data.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Pulls purge-and-archive business data from Dynamics 365 F&SCM for a legal entity's most recent fiscal period and saves a standalone interactive HTML dashboard (charts, sortable table, RAG indicator) to the output folder;", 'example_request': 'Build a purge and archive business data dashboard for USMF for the latest fiscal period as an HTML file.', 'inputs': [{'description': 'D365 legal entity to pull data from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Period to report on; defaults to the most recent fiscal period available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-purge-and-archive-business-data-2026-05-24.html.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a browser-viewable dashboard of D365 purge and archive business data that viewers can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardPurgeAndArchiveBusinessData(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardPurgeAndArchiveBusinessData'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Period to report on; defaults to the most recent fiscal period available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull data from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-purge-and-archive-business-data-2026-05-24.html.', 'type': 'string'}},
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
    print(DashboardPurgeAndArchiveBusinessData().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
