---
name: "rar-cowork-cookbook-adaptive-card-adjust-inventory-levels"
description: "Generates a read-only Adaptive Card JSON file visualizing adjust-inventory-levels status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_adjust_inventory_levels", "rar_sha256": "10cdbd1cc1663d8a6a2c072f2e30c077b05cce173a74733684f1b4581243d6cd", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_adjust_inventory_levels`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_adjust_inventory_levels_agent.py` and in the RCI capsule.

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

Adjust inventory levels Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing adjust-inventory-levels status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-adjust-inventory-levels
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
    "as_of_date": {
      "description": "Date used for the card timestamp and file name.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
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
    "output_file_name": {
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-adjust-inventory-levels-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_adjust_inventory_levels_agent.py` and embedded as the fenced Python below (sha256 10cdbd1cc1663d8a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_adjust_inventory_levels_agent.py` first:

```bash
python3 adaptive_card_adjust_inventory_levels_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_adjust_inventory_levels_agent.py   # or on stdin
python3 adaptive_card_adjust_inventory_levels_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Adjust inventory levels Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing adjust-inventory-levels status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-adjust-inventory-levels
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_adjust_inventory_levels',
    "version": '3.0.2',
    "display_name": 'Adjust inventory levels Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing adjust-inventory-levels status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.',
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
        "upstream_slug": 'adaptive-card-adjust-inventory-levels',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-adjust-inventory-levels',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd5d0af4d77ea7274',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/maintain-inventory-levels/adjust-inventory-levels'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/adaptive-card-adjust-inventory-levels', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date used for the card timestamp and file name.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_file_name': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-adjust-inventory-levels-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical adjust inventory levels status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-adjust-inventory-levels-2026-05-24-card.json' that visualizes the current state of adjust inventory levels. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current adjust inventory levels KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing adjust-inventory-levels status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card JSON for adjust inventory levels status in USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-adjust-inventory-levels-2026-05-24-card.json.', 'name': 'output_file_name'}, {'description': 'Date used for the card timestamp and file name.', 'name': 'as_of_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable Adaptive Card snapshot of adjust inventory levels status for Teams, Outlook, or a dashboard, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardAdjustInventoryLevels(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardAdjustInventoryLevels'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date used for the card timestamp and file name.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_file_name': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-adjust-inventory-levels-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardAdjustInventoryLevels().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
