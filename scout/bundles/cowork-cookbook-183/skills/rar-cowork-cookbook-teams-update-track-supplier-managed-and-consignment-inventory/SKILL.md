---
name: "rar-cowork-cookbook-teams-update-track-supplier-managed-and-consignment-inventory"
description: "Summarizes supplier-managed and consignment inventory from Dynamics 365 F&SCM for a given legal entity and saves a draft Teams channel post plus an Adaptive Card JSON file; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_track_supplier_managed_and_consignment_inventory", "rar_sha256": "4907519b9e464b3480efdae400ae44b314c9cd4959bd06a27d779476a99be2ca", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_track_supplier_managed_and_consignment_inventory`. The original RAPP
agent is preserved byte-for-byte in `teams_update_track_supplier_managed_and_consignment_inventory_agent.py` and in the RCI capsule.

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

Track supplier managed and consignment inventory Teams Channel Update — Summarizes supplier-managed and consignment inventory from Dynamics 365 F&SCM for a given legal entity and saves a draft Teams channel post plus an Adaptive Card JSON file; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-track-supplier-managed-and-consignment-inventory
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
      "description": "Date used for the report scope and card filename, e.g. 2026-05-24.",
      "type": "string"
    },
    "card_filename": {
      "description": "Output name for the Adaptive Card JSON artifact.",
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
    "scope_notes": {
      "description": "Optional narrowing of scope, such as specific suppliers, sites, or items.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_track_supplier_managed_and_consignment_inventory_agent.py` and embedded as the fenced Python below (sha256 4907519b9e464b34…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_track_supplier_managed_and_consignment_inventory_agent.py` first:

```bash
python3 teams_update_track_supplier_managed_and_consignment_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_track_supplier_managed_and_consignment_inventory_agent.py   # or on stdin
python3 teams_update_track_supplier_managed_and_consignment_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track supplier managed and consignment inventory Teams Channel Update — Summarizes supplier-managed and consignment inventory from Dynamics 365 F&SCM for a given legal entity and saves a draft Teams channel post plus an Adaptive Card JSON file; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-track-supplier-managed-and-consignment-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_track_supplier_managed_and_consignment_inventory',
    "version": '3.0.3',
    "display_name": 'Track supplier managed and consignment inventory Teams Channel Update',
    "description": 'Summarizes supplier-managed and consignment inventory from Dynamics 365 F&SCM for a given legal entity and saves a draft Teams channel post plus an Adaptive Card JSON file; nothing is posted.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-track-supplier-managed-and-consignment-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-track-supplier-managed-and-consignment-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '088dd86390585645',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/maintain-inventory-levels/track-supplier-managed-and-consignment-inventory'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/teams-update-track-supplier-managed-and-consignment-inventory', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date used for the report scope and card filename, e.g. 2026-05-24.', 'card_filename': 'Output name for the Adaptive Card JSON artifact.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'scope_notes': 'Optional narrowing of scope, such as specific suppliers, sites, or items.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of track supplier managed and consignment inventory. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-track-supplier-managed-and-consignment-inventory-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads track supplier managed and consignment inventory, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes supplier-managed and consignment inventory from Dynamics 365 F&SCM for a given legal entity and saves a draft Teams channel post plus an Adaptive Card JSON file; nothing is posted.', 'example_request': 'Draft a Teams update on supplier-managed and consignment inventory for USMF as of 2026-05-24, with an Adaptive Card.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date used for the report scope and card filename, e.g. 2026-05-24.', 'name': 'as_of_date'}, {'description': 'Output name for the Adaptive Card JSON artifact.', 'name': 'card_filename'}, {'description': 'Optional narrowing of scope, such as specific suppliers, sites, or items.', 'name': 'scope_notes'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams update on supplier-managed/consignment inventory status with KPIs and quick-action buttons drafted, not posted.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateTrackSupplierManagedAndConsignmentInventory(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateTrackSupplierManagedAndConsignmentInventory'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date used for the report scope and card filename, e.g. 2026-05-24.', 'type': 'string'}, 'card_filename': {'description': 'Output name for the Adaptive Card JSON artifact.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'scope_notes': {'description': 'Optional narrowing of scope, such as specific suppliers, sites, or items.', 'type': 'string'}},
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
    print(TeamsUpdateTrackSupplierManagedAndConsignmentInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
