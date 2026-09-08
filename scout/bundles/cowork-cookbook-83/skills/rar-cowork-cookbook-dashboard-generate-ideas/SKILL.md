---
name: "rar-cowork-cookbook-dashboard-generate-ideas"
description: "Pulls generate-ideas data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the Cowork D365 ERP plugin and saves a standalone interactive HTML dashboard file to the output folder, read-onl"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_generate_ideas", "rar_sha256": "c4c532e845e7eff4309a03ad3328f4921f4ff983aa1601aecbb7ccb98ee8962d", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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
