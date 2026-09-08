---
name: "rar-cowork-cookbook-adaptive-card-manage-service-truck-inventory"
description: "Generates a read-only Adaptive Card JSON file summarizing service truck inventory status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons. Call when you need an embeddable"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_service_truck_inventory", "rar_sha256": "471a33b59b31fc0f632b63965f3069633fc3e7a29a9f5395d63498961a7b6291", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_manage_service_truck_inventory`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_manage_service_truck_inventory_agent.py` and in the RCI capsule.

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

Manage service truck inventory Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing service truck inventory status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons. Call when you need an embeddable

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-service-truck-inventory
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
    "as_of_timestamp": {
      "description": "Timestamp shown in the card header.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "kpi_count": {
      "description": "How many KPI tiles to include (3-5), each with current value and trend arrow.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-manage-service-truck-inventory-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_manage_service_truck_inventory_agent.py` and embedded as the fenced Python below (sha256 471a33b59b31fc0f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_manage_service_truck_inventory_agent.py` first:

```bash
python3 adaptive_card_manage_service_truck_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_manage_service_truck_inventory_agent.py   # or on stdin
python3 adaptive_card_manage_service_truck_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage service truck inventory Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing service truck inventory status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons. Call when you need an embeddable

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-service-truck-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_manage_service_truck_inventory',
    "version": '3.0.2',
    "display_name": 'Manage service truck inventory Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing service truck inventory status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons. Call when you need an embeddable',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-manage-service-truck-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-manage-service-truck-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '51fc379efbca01de',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/manage-service-truck-inventory'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/adaptive-card-manage-service-truck-inventory', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_button_count': 'How many action buttons to include (2-3).', 'as_of_timestamp': 'Timestamp shown in the card header.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5), each with current value and trend arrow.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-manage-service-truck-inventory-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical manage service truck inventory status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-manage-service-truck-inventory-2026-05-24-card.json' that visualizes the current state of manage service truck inventory. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current manage service truck inventory KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing service truck inventory status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons. Call when you need an embeddable', 'example_request': 'Make an Adaptive Card JSON showing service truck inventory status from D365 USMF, with 4 KPI tiles and a RAG row.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-manage-service-truck-inventory-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'How many KPI tiles to include (3-5), each with current value and trend arrow.', 'name': 'kpi_count'}, {'description': 'How many action buttons to include (2-3).', 'name': 'action_button_count'}, {'description': 'Timestamp shown in the card header.', 'name': 'as_of_timestamp'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you want a Teams/Outlook-renderable Adaptive Card snapshot of service truck inventory status from D365 ERP, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardManageServiceTruckInventory(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardManageServiceTruckInventory'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_button_count': {'description': 'How many action buttons to include (2-3).', 'type': 'string'}, 'as_of_timestamp': {'description': 'Timestamp shown in the card header.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5), each with current value and trend arrow.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-manage-service-truck-inventory-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardManageServiceTruckInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
