---
name: "rar-cowork-cookbook-adaptive-card-track-customer-managed-inventory-and-consigned-inventory"
description: "Generates a read-only Adaptive Card JSON file summarizing customer-managed and consigned inventory status from Dynamics 365 F&SCM (legal entity USMF), with KPI tiles, trend arrows, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_track_customer_managed_inventory_and_consigned_inventory", "rar_sha256": "0c6d8756f3d54e62f1d013d49741f7769d196f2c38ceaf088b0a68806d54b8d9", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
