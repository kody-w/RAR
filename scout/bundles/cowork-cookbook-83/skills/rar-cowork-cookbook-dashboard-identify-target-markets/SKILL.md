---
name: "rar-cowork-cookbook-dashboard-identify-target-markets"
description: "Pulls target-market data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder, read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_identify_target_markets", "rar_sha256": "7f0de19faaa0f79666774772a872e99e85396433165ed73a7b7ddecbc48365ed", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_identify_target_markets`. The original RAPP
agent is preserved byte-for-byte in `dashboard_identify_target_markets_agent.py` and in the RCI capsule.

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

Identify target markets Interactive HTML Dashboard — Pulls target-market data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder, read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-identify-target-markets
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
      "description": "Name of the HTML file to write, e.g. dashboard-identify-target-markets-2026-05-24.html.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_identify_target_markets_agent.py` and embedded as the fenced Python below (sha256 7f0de19faaa0f796…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_identify_target_markets_agent.py` first:

```bash
python3 dashboard_identify_target_markets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_identify_target_markets_agent.py   # or on stdin
python3 dashboard_identify_target_markets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify target markets Interactive HTML Dashboard — Pulls target-market data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder, read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-identify-target-markets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_identify_target_markets',
    "version": '3.0.3',
    "display_name": 'Identify target markets Interactive HTML Dashboard',
    "description": 'Pulls target-market data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder, read-only.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-identify-target-markets',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-identify-target-markets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c1fb48c54ef954f0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/research-and-develop-offerings/identify-target-markets'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/dashboard-identify-target-markets', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-identify-target-markets-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of identify target markets with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull identify target markets data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-identify-target-markets-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing identify target markets.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls target-market data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder, read-only.', 'example_request': 'Build a target markets dashboard from D365 USMF for the latest fiscal period as a standalone HTML file.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-identify-target-markets-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a browser-viewable target-market dashboard from D365 ERP data that someone without D365 access can open.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardIdentifyTargetMarkets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardIdentifyTargetMarkets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-identify-target-markets-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardIdentifyTargetMarkets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
