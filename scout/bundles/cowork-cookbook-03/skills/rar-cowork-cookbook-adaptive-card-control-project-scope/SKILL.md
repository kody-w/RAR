---
name: "rar-cowork-cookbook-adaptive-card-control-project-scope"
description: "Generates a read-only Adaptive Card JSON file summarizing control project scope status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_control_project_scope", "rar_sha256": "5459372e296a5fc186c0e1e72f577756d2037483cbb35ea3581b0a782b594e35", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_control_project_scope`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_control_project_scope_agent.py` and in the RCI capsule.

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

Control project scope Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing control project scope status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-control-project-scope
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
    "action_buttons": {
      "description": "The 2-3 action buttons and their target links to include on the card.",
      "type": "string"
    },
    "as_of_date": {
      "description": "Snapshot date used in the card header and filename, e.g. 2026-05-24.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "kpi_selection": {
      "description": "Which 3-5 control project scope KPIs to show as tiles with trend arrows.",
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
      "description": "Name of the Adaptive Card JSON file to produce.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_control_project_scope_agent.py` and embedded as the fenced Python below (sha256 5459372e296a5fc1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_control_project_scope_agent.py` first:

```bash
python3 adaptive_card_control_project_scope_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_control_project_scope_agent.py   # or on stdin
python3 adaptive_card_control_project_scope_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Control project scope Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing control project scope status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-control-project-scope
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_control_project_scope',
    "version": '3.0.2',
    "display_name": 'Control project scope Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing control project scope status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-control-project-scope',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-control-project-scope',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b57391cd2d8e1961',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/control-project-scope'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/adaptive-card-control-project-scope', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_buttons': 'The 2-3 action buttons and their target links to include on the card.', 'as_of_date': 'Snapshot date used in the card header and filename, e.g. 2026-05-24.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_selection': 'Which 3-5 control project scope KPIs to show as tiles with trend arrows.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical control project scope status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-control-project-scope-2026-05-24-card.json' that visualizes the current state of control project scope. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current control project scope KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing control project scope status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card JSON of control project scope status for USMF as of 2026-05-24, read-only.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Snapshot date used in the card header and filename, e.g. 2026-05-24.', 'name': 'as_of_date'}, {'description': 'Name of the Adaptive Card JSON file to produce.', 'name': 'output_filename'}, {'description': 'Which 3-5 control project scope KPIs to show as tiles with trend arrows.', 'name': 'kpi_selection'}, {'description': 'The 2-3 action buttons and their target links to include on the card.', 'name': 'action_buttons'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a Teams/Outlook-ready Adaptive Card snapshot of control project scope status pulled from D365 ERP, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardControlProjectScope(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardControlProjectScope'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_buttons': {'description': 'The 2-3 action buttons and their target links to include on the card.', 'type': 'string'}, 'as_of_date': {'description': 'Snapshot date used in the card header and filename, e.g. 2026-05-24.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_selection': {'description': 'Which 3-5 control project scope KPIs to show as tiles with trend arrows.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce.', 'type': 'string'}},
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
    print(AdaptiveCardControlProjectScope().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
