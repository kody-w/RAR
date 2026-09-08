---
name: "rar-cowork-cookbook-dashboard-generate-ideas"
description: "Pulls generate-ideas data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the Cowork D365 ERP plugin and saves a standalone interactive HTML dashboard file to the output folder, read-onl"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_generate_ideas", "rar_sha256": "c4c532e845e7eff4309a03ad3328f4921f4ff983aa1601aecbb7ccb98ee8962d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_generate_ideas`. The original RAPP
agent is preserved byte-for-byte in `dashboard_generate_ideas_agent.py` and in the RCI capsule.

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

Generate ideas Interactive HTML Dashboard — Pulls generate-ideas data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the Cowork D365 ERP plugin and saves a standalone interactive HTML dashboard file to the output folder, read-onl

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-generate-ideas
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
      "description": "Name of the HTML file to write, e.g. dashboard-generate-ideas-2026-05-24.html.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_generate_ideas_agent.py` and embedded as the fenced Python below (sha256 c4c532e845e7eff4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_generate_ideas_agent.py` first:

```bash
python3 dashboard_generate_ideas_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_generate_ideas_agent.py   # or on stdin
python3 dashboard_generate_ideas_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Generate ideas Interactive HTML Dashboard — Pulls generate-ideas data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the Cowork D365 ERP plugin and saves a standalone interactive HTML dashboard file to the output folder, read-onl

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-generate-ideas
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_generate_ideas',
    "version": '3.0.3',
    "display_name": 'Generate ideas Interactive HTML Dashboard',
    "description": 'Pulls generate-ideas data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the Cowork D365 ERP plugin and saves a standalone interactive HTML dashboard file to the output folder, read-onl',
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
        "upstream_slug": 'dashboard-generate-ideas',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-generate-ideas',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '590a55f701c7de0e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/research-and-develop-offerings/generate-ideas'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/dashboard-generate-ideas', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-generate-ideas-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of generate ideas with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull generate ideas data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-generate-ideas-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing generate ideas.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls generate-ideas data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the Cowork D365 ERP plugin and saves a standalone interactive HTML dashboard file to the output folder, read-onl', 'example_request': 'Build me an interactive HTML dashboard of generate ideas data from D365 USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-generate-ideas-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of D365 generate-ideas data for the latest fiscal period, without giving the viewer D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardGenerateIdeas(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardGenerateIdeas'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-generate-ideas-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardGenerateIdeas().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
