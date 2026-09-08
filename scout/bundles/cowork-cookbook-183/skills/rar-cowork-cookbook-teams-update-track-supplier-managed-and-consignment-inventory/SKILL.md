---
name: "rar-cowork-cookbook-teams-update-track-supplier-managed-and-consignment-inventory"
description: "Summarizes supplier-managed and consignment inventory from Dynamics 365 F&SCM for a given legal entity and saves a draft Teams channel post plus an Adaptive Card JSON file; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_track_supplier_managed_and_consignment_inventory", "rar_sha256": "4907519b9e464b3480efdae400ae44b314c9cd4959bd06a27d779476a99be2ca", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
