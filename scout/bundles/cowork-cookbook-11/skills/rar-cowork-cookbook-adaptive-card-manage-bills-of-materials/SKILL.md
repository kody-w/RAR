---
name: "rar-cowork-cookbook-adaptive-card-manage-bills-of-materials"
description: "Generates a read-only Adaptive Card JSON file summarizing bill of materials status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, trend arrows, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_bills_of_materials", "rar_sha256": "eac19b7171c1b88512d773c8a5bc0c8e547d2b42dd8508ee5a7b490efb64d555", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
