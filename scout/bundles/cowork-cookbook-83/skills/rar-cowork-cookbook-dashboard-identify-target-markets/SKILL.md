---
name: "rar-cowork-cookbook-dashboard-identify-target-markets"
description: "Pulls target-market data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder, read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_identify_target_markets", "rar_sha256": "7f0de19faaa0f79666774772a872e99e85396433165ed73a7b7ddecbc48365ed", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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
