---
name: "rar-cowork-cookbook-dashboard-define-value-proposition"
description: "Pulls define value proposition data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the output folder, read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_value_proposition", "rar_sha256": "ce2da2f42e43ce83dbca09af8b5afd90efb6782ece6579f24e38f573683bcb42", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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
