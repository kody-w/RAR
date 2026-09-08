---
name: "rar-cowork-cookbook-dashboard-purge-and-archive-business-data"
description: "Pulls purge-and-archive business data from Dynamics 365 F&SCM for a legal entity's most recent fiscal period and saves a standalone interactive HTML dashboard (charts, sortable table, RAG indicator) to the output folder;"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_purge_and_archive_business_data", "rar_sha256": "0bc7310fee65d1dd50932655312ef9582b61f034ef77a8c570cf925f4e1fb772", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
