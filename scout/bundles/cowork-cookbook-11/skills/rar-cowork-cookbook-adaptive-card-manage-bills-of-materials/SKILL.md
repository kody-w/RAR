---
name: "rar-cowork-cookbook-adaptive-card-manage-bills-of-materials"
description: "Generates a read-only Adaptive Card JSON file summarizing bill of materials status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, trend arrows, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_bills_of_materials", "rar_sha256": "eac19b7171c1b88512d773c8a5bc0c8e547d2b42dd8508ee5a7b490efb64d555", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_manage_bills_of_materials`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_manage_bills_of_materials_agent.py` and in the RCI capsule.

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

Manage bills of materials Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing bill of materials status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, trend arrows, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-bills-of-materials
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
    "as_of_date": {
      "description": "Date/timestamp shown in the card header.",
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
      "description": "D365 legal entity to report on, e.g. USMF.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-manage-bills-of-materials-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_manage_bills_of_materials_agent.py` and embedded as the fenced Python below (sha256 eac19b7171c1b885…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_manage_bills_of_materials_agent.py` first:

```bash
python3 adaptive_card_manage_bills_of_materials_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_manage_bills_of_materials_agent.py   # or on stdin
python3 adaptive_card_manage_bills_of_materials_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage bills of materials Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing bill of materials status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, trend arrows, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-bills-of-materials
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_manage_bills_of_materials',
    "version": '3.0.2',
    "display_name": 'Manage bills of materials Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing bill of materials status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, trend arrows, a RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-manage-bills-of-materials',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-manage-bills-of-materials',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b4616af15ae037f3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/manage-active-products/manage-bills-of-materials'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/adaptive-card-manage-bills-of-materials', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_button_count': 'How many action buttons to include (2-3).', 'as_of_date': 'Date/timestamp shown in the card header.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5).', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-manage-bills-of-materials-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical manage bills of materials status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-manage-bills-of-materials-2026-05-24-card.json' that visualizes the current state of manage bills of materials. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current manage bills of materials KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing bill of materials status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, trend arrows, a RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card showing BOM status for USMF with 4 KPI tiles and a RAG row.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-manage-bills-of-materials-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'How many KPI tiles to include (3-5).', 'name': 'kpi_count'}, {'description': 'How many action buttons to include (2-3).', 'name': 'action_button_count'}, {'description': 'Date/timestamp shown in the card header.', 'name': 'as_of_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable Adaptive Card snapshot of BOM status for Teams, Outlook, or a dashboard, without changing any ERP data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardManageBillsOfMaterials(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardManageBillsOfMaterials'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_button_count': {'description': 'How many action buttons to include (2-3).', 'type': 'string'}, 'as_of_date': {'description': 'Date/timestamp shown in the card header.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5).', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-manage-bills-of-materials-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardManageBillsOfMaterials().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
