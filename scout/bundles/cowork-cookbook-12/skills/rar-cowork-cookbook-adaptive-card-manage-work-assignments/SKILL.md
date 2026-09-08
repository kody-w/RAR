---
name: "rar-cowork-cookbook-adaptive-card-manage-work-assignments"
description: "Generates a read-only Adaptive Card JSON file summarizing work assignment status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_work_assignments", "rar_sha256": "71034042d3fd39d28eafdc3d815a4a5b2beacda19c9d5793ea0bb3a5bd36ff05", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_manage_work_assignments`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_manage_work_assignments_agent.py` and in the RCI capsule.

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

Manage work assignments Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing work assignment status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-work-assignments
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
    "action_button_count": {
      "description": "How many action buttons to include (2-3).",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "kpi_count": {
      "description": "How many KPI tiles to include (3-5).",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to query, e.g. USMF.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-manage-work-assignments-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_manage_work_assignments_agent.py` and embedded as the fenced Python below (sha256 71034042d3fd39d2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_manage_work_assignments_agent.py` first:

```bash
python3 adaptive_card_manage_work_assignments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_manage_work_assignments_agent.py   # or on stdin
python3 adaptive_card_manage_work_assignments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage work assignments Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing work assignment status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-work-assignments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_manage_work_assignments',
    "version": '3.0.2',
    "display_name": 'Manage work assignments Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing work assignment status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-manage-work-assignments',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-manage-work-assignments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '22c3f6312d6d94fd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-warehouse-operations/manage-work-assignments'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/adaptive-card-manage-work-assignments', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_button_count': 'How many action buttons to include (2-3).', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5).', 'legal_entity': 'Dynamics 365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-manage-work-assignments-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical manage work assignments status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-manage-work-assignments-2026-05-24-card.json' that visualizes the current state of manage work assignments. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current manage work assignments KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing work assignment status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card JSON of work assignment status in USMF with 4 KPI tiles and 2 buttons.', 'inputs': [{'description': 'Dynamics 365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-manage-work-assignments-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'How many KPI tiles to include (3-5).', 'name': 'kpi_count'}, {'description': 'How many action buttons to include (2-3).', 'name': 'action_button_count'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable Adaptive Card snapshot of manage work assignments status for Teams, Outlook, or a dashboard, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardManageWorkAssignments(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardManageWorkAssignments'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_button_count': {'description': 'How many action buttons to include (2-3).', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5).', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-manage-work-assignments-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardManageWorkAssignments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
