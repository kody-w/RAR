---
name: "rar-cowork-cookbook-adaptive-card-design-bills-of-materials"
description: "Generates a read-only Adaptive Card JSON file summarizing design bills of materials status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_design_bills_of_materials", "rar_sha256": "014c494f55a6703cb83a6573367f1a89415708026da1b7fbfc420906cb0987f1", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
