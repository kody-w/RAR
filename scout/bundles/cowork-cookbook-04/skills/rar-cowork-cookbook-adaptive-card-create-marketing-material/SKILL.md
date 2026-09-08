---
name: "rar-cowork-cookbook-adaptive-card-create-marketing-material"
description: "Generates a read-only Adaptive Card JSON file summarizing create marketing material status from Dynamics 365 F&SCM, with header, KPI tiles, RAG row, and action buttons for Teams, Outlook, or dashboards."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_create_marketing_material", "rar_sha256": "95de52f078614526647c10d77c51ab02369389168cfe9ee081caef4d9e1fa6e3", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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
