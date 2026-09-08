---
name: "rar-cowork-cookbook-adaptive-card-track-customer-managed-inventory-and-consigned-inventory"
description: "Generates a read-only Adaptive Card JSON file summarizing customer-managed and consigned inventory status from Dynamics 365 F&SCM (legal entity USMF), with KPI tiles, trend arrows, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_track_customer_managed_inventory_and_consigned_inventory", "rar_sha256": "0c6d8756f3d54e62f1d013d49741f7769d196f2c38ceaf088b0a68806d54b8d9", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_track_customer_managed_inventory_and_consigned_inventory`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_track_customer_managed_inventory_and_consigned_inventory_agent.py` and in the RCI capsule.

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

Track customer managed inventory and consigned inventory Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing customer-managed and consigned inventory status from Dynamics 365 F&SCM (legal entity USMF), with KPI tiles, trend arrows, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-track-customer-managed-inventory-and-consigned-inventory
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
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-track-customer-managed-inventory-and-consigned-inventory-2026-05-24-card.json.",
      "type": "string"
    },
    "snapshot_date": {
      "description": "Date the status snapshot represents, used in the card header timestamp and filename.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_track_customer_managed_inventory_and_consigned_inventory_agent.py` and embedded as the fenced Python below (sha256 0c6d8756f3d54e62…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_track_customer_managed_inventory_and_consigned_inventory_agent.py` first:

```bash
python3 adaptive_card_track_customer_managed_inventory_and_consigned_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_track_customer_managed_inventory_and_consigned_inventory_agent.py   # or on stdin
python3 adaptive_card_track_customer_managed_inventory_and_consigned_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track customer managed inventory and consigned inventory Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing customer-managed and consigned inventory status from Dynamics 365 F&SCM (legal entity USMF), with KPI tiles, trend arrows, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-track-customer-managed-inventory-and-consigned-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_track_customer_managed_inventory_and_consigned_inventory',
    "version": '3.0.2',
    "display_name": 'Track customer managed inventory and consigned inventory Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing customer-managed and consigned inventory status from Dynamics 365 F&SCM (legal entity USMF), with KPI tiles, trend arrows, a RAG row, and action buttons.',
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
        "upstream_slug": 'adaptive-card-track-customer-managed-inventory-and-consigned-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-track-customer-managed-inventory-and-consigned-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '088ba4abbd6d8a36',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/maintain-inventory-levels/track-customer-managed-inventory-and-consigned-inventory'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/adaptive-card-track-customer-managed-inventory-and-consigned-inventory', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-track-customer-managed-inventory-and-consigned-inventory-2026-05-24-card.json.', 'snapshot_date': 'Date the status snapshot represents, used in the card header timestamp and filename.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical track customer managed inventory and consigned inventory status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-track-customer-managed-inventory-and-consigned-inventory-2026-05-24-card.json' that visualizes the current state of track customer managed inventory and consigned inventory. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current track customer managed inventory and consigned inventory KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing customer-managed and consigned inventory status from Dynamics 365 F&SCM (legal entity USMF), with KPI tiles, trend arrows, a RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card showing customer-managed and consigned inventory status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-track-customer-managed-inventory-and-consigned-inventory-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date the status snapshot represents, used in the card header timestamp and filename.', 'name': 'snapshot_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a Teams/Outlook-ready Adaptive Card snapshot of customer-managed and consigned inventory status from D365 F&SCM, without changing data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardTrackCustomerManagedInventoryAndConsignedInventory(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardTrackCustomerManagedInventoryAndConsignedInventory'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-track-customer-managed-inventory-and-consigned-inventory-2026-05-24-card.json.', 'type': 'string'}, 'snapshot_date': {'description': 'Date the status snapshot represents, used in the card header timestamp and filename.', 'type': 'string'}},
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
    print(AdaptiveCardTrackCustomerManagedInventoryAndConsignedInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
