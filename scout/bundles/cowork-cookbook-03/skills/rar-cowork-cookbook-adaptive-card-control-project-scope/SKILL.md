---
name: "rar-cowork-cookbook-adaptive-card-control-project-scope"
description: "Generates a read-only Adaptive Card JSON file summarizing control project scope status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_control_project_scope", "rar_sha256": "5459372e296a5fc186c0e1e72f577756d2037483cbb35ea3581b0a782b594e35", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
