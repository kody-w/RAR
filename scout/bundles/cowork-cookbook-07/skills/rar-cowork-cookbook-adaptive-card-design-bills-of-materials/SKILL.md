---
name: "rar-cowork-cookbook-adaptive-card-design-bills-of-materials"
description: "Generates a read-only Adaptive Card JSON file summarizing design bills of materials status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_design_bills_of_materials", "rar_sha256": "014c494f55a6703cb83a6573367f1a89415708026da1b7fbfc420906cb0987f1", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_design_bills_of_materials`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_design_bills_of_materials_agent.py` and in the RCI capsule.

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

Design bills of materials Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing design bills of materials status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-design-bills-of-materials
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
      "description": "The 2-3 action buttons to place on the card.",
      "type": "string"
    },
    "as_of_date": {
      "description": "Snapshot date used in the card timestamp and output filename.",
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
      "description": "D365 F&SCM legal entity to query, e.g. USMF.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-design-bills-of-materials-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_design_bills_of_materials_agent.py` and embedded as the fenced Python below (sha256 014c494f55a6703c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_design_bills_of_materials_agent.py` first:

```bash
python3 adaptive_card_design_bills_of_materials_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_design_bills_of_materials_agent.py   # or on stdin
python3 adaptive_card_design_bills_of_materials_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Design bills of materials Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing design bills of materials status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-design-bills-of-materials
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_design_bills_of_materials',
    "version": '3.0.2',
    "display_name": 'Design bills of materials Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing design bills of materials status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons.',
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
        "upstream_slug": 'adaptive-card-design-bills-of-materials',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-design-bills-of-materials',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bf518f71038f6bc0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/introduce-products/design-bills-of-materials'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/adaptive-card-design-bills-of-materials', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_buttons': 'The 2-3 action buttons to place on the card.', 'as_of_date': 'Snapshot date used in the card timestamp and output filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5).', 'legal_entity': 'D365 F&SCM legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-design-bills-of-materials-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical design bills of materials status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-design-bills-of-materials-2026-05-24-card.json' that visualizes the current state of design bills of materials. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current design bills of materials KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing design bills of materials status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card showing design BOM status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 F&SCM legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Snapshot date used in the card timestamp and output filename.', 'name': 'as_of_date'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-design-bills-of-materials-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'How many KPI tiles to include (3-5).', 'name': 'kpi_count'}, {'description': 'The 2-3 action buttons to place on the card.', 'name': 'action_buttons'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable Adaptive Card snapshot of design BOM status for Teams, Outlook, or a dashboard, without changing any ERP data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardDesignBillsOfMaterials(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDesignBillsOfMaterials'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_buttons': {'description': 'The 2-3 action buttons to place on the card.', 'type': 'string'}, 'as_of_date': {'description': 'Snapshot date used in the card timestamp and output filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5).', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-design-bills-of-materials-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardDesignBillsOfMaterials().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
