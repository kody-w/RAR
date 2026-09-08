---
name: "rar-cowork-cookbook-adaptive-card-create-marketing-material"
description: "Generates a read-only Adaptive Card JSON file summarizing create marketing material status from Dynamics 365 F&SCM, with header, KPI tiles, RAG row, and action buttons for Teams, Outlook, or dashboards."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_create_marketing_material", "rar_sha256": "95de52f078614526647c10d77c51ab02369389168cfe9ee081caef4d9e1fa6e3", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_create_marketing_material`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_create_marketing_material_agent.py` and in the RCI capsule.

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

Create marketing material Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing create marketing material status from Dynamics 365 F&SCM, with header, KPI tiles, RAG row, and action buttons for Teams, Outlook, or dashboards.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-create-marketing-material
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
      "description": "Date the status snapshot and timestamp should reflect.",
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
    "output_file_name": {
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-create-marketing-material-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_create_marketing_material_agent.py` and embedded as the fenced Python below (sha256 95de52f078614526…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_create_marketing_material_agent.py` first:

```bash
python3 adaptive_card_create_marketing_material_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_create_marketing_material_agent.py   # or on stdin
python3 adaptive_card_create_marketing_material_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create marketing material Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing create marketing material status from Dynamics 365 F&SCM, with header, KPI tiles, RAG row, and action buttons for Teams, Outlook, or dashboards.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-create-marketing-material
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_create_marketing_material',
    "version": '3.0.2',
    "display_name": 'Create marketing material Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing create marketing material status from Dynamics 365 F&SCM, with header, KPI tiles, RAG row, and action buttons for Teams, Outlook, or dashboards.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-create-marketing-material',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-create-marketing-material',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '44f60f4409c4382f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/create-marketing-material'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/adaptive-card-create-marketing-material', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_buttons': 'The 2-3 action buttons to place on the card.', 'as_of_date': 'Date the status snapshot and timestamp should reflect.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5).', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_file_name': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-create-marketing-material-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical create marketing material status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-create-marketing-material-2026-05-24-card.json' that visualizes the current state of create marketing material. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current create marketing material KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing create marketing material status from Dynamics 365 F&SCM, with header, KPI tiles, RAG row, and action buttons for Teams, Outlook, or dashboards.', 'example_request': 'Make me an Adaptive Card showing create marketing material status in USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-create-marketing-material-2026-05-24-card.json.', 'name': 'output_file_name'}, {'description': 'Date the status snapshot and timestamp should reflect.', 'name': 'as_of_date'}, {'description': 'How many KPI tiles to include (3-5).', 'name': 'kpi_count'}, {'description': 'The 2-3 action buttons to place on the card.', 'name': 'action_buttons'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable Adaptive Card snapshot of create marketing material status from D365 ERP data, without modifying any records.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardCreateMarketingMaterial(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardCreateMarketingMaterial'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_buttons': {'description': 'The 2-3 action buttons to place on the card.', 'type': 'string'}, 'as_of_date': {'description': 'Date the status snapshot and timestamp should reflect.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5).', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_file_name': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-create-marketing-material-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardCreateMarketingMaterial().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
