---
name: "rar-cowork-cookbook-dashboard-define-value-proposition"
description: "Pulls define value proposition data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the output folder, read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_value_proposition", "rar_sha256": "ce2da2f42e43ce83dbca09af8b5afd90efb6782ece6579f24e38f573683bcb42", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_define_value_proposition`. The original RAPP
agent is preserved byte-for-byte in `dashboard_define_value_proposition_agent.py` and in the RCI capsule.

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

Define value proposition Interactive HTML Dashboard — Pulls define value proposition data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the output folder, read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-value-proposition
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
      "description": "Name of the HTML file to produce, e.g. dashboard-define-value-proposition-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Folder where the HTML file is saved, e.g. Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_define_value_proposition_agent.py` and embedded as the fenced Python below (sha256 ce2da2f42e43ce83…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_define_value_proposition_agent.py` first:

```bash
python3 dashboard_define_value_proposition_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_define_value_proposition_agent.py   # or on stdin
python3 dashboard_define_value_proposition_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define value proposition Interactive HTML Dashboard — Pulls define value proposition data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the output folder, read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-value-proposition
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_define_value_proposition',
    "version": '3.0.3',
    "display_name": 'Define value proposition Interactive HTML Dashboard',
    "description": 'Pulls define value proposition data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the output folder, read-only.',
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
        "upstream_slug": 'dashboard-define-value-proposition',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-define-value-proposition',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '27d47e548ec3e710',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/develop-marketing-strategy/define-value-proposition'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/dashboard-define-value-proposition', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to produce, e.g. dashboard-define-value-proposition-2026-05-24.html.', 'output_folder': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of define value proposition with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull define value proposition data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-define-value-proposition-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing define value proposition.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls define value proposition data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the output folder, read-only.', 'example_request': 'Build me an interactive HTML dashboard for define value proposition from USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to produce, e.g. dashboard-define-value-proposition-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a shareable browser-viewable dashboard of define value proposition data from D365 that viewers can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardDefineValueProposition(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDefineValueProposition'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to produce, e.g. dashboard-define-value-proposition-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardDefineValueProposition().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
