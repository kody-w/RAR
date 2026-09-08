---
name: "rar-cowork-cookbook-adaptive-card-adjust-inventory-levels"
description: "Generates a read-only Adaptive Card JSON file visualizing adjust-inventory-levels status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_adjust_inventory_levels", "rar_sha256": "10cdbd1cc1663d8a6a2c072f2e30c077b05cce173a74733684f1b4581243d6cd", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
