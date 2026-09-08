---
name: "rar-cowork-cookbook-scheduled-brief-track-supplier-managed-and-consignment-inventory"
description: "Builds a morning brief on supplier-managed and consignment inventory from Dynamics 365 ERP for a legal entity, drafts an email to the owner (saved, not sent), and a Teams-ready summary."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_track_supplier_managed_and_consignment_inventory", "rar_sha256": "ed23249b79e9e1b7acb69f5d432ce3e2c90cbc44732f6b9c7054f22df5faf5c8", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_track_supplier_managed_and_consignment_inventory`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_track_supplier_managed_and_consignment_inventory_agent.py` and in the RCI capsule.

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

Track supplier managed and consignment inventory Scheduled Email Brief — Builds a morning brief on supplier-managed and consignment inventory from Dynamics 365 ERP for a legal entity, drafts an email to the owner (saved, not sent), and a Teams-ready summary.

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-track-supplier-managed-and-consignment-inventory
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
    "owner": {
      "description": "Responsible owner who receives the drafted email brief.",
      "type": "string"
    },
    "schedule": {
      "description": "When the brief should run, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_track_supplier_managed_and_consignment_inventory_agent.py` and embedded as the fenced Python below (sha256 ed23249b79e9e1b7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_track_supplier_managed_and_consignment_inventory_agent.py` first:

```bash
python3 scheduled_brief_track_supplier_managed_and_consignment_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_track_supplier_managed_and_consignment_inventory_agent.py   # or on stdin
python3 scheduled_brief_track_supplier_managed_and_consignment_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track supplier managed and consignment inventory Scheduled Email Brief — Builds a morning brief on supplier-managed and consignment inventory from Dynamics 365 ERP for a legal entity, drafts an email to the owner (saved, not sent), and a Teams-ready summary.

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-track-supplier-managed-and-consignment-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_track_supplier_managed_and_consignment_inventory',
    "version": '3.0.3',
    "display_name": 'Track supplier managed and consignment inventory Scheduled Email Brief',
    "description": 'Builds a morning brief on supplier-managed and consignment inventory from Dynamics 365 ERP for a legal entity, drafts an email to the owner (saved, not sent), and a Teams-ready summary.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-track-supplier-managed-and-consignment-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-track-supplier-managed-and-consignment-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '769656044989bb2d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/maintain-inventory-levels/track-supplier-managed-and-consignment-inventory'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/scheduled-brief-track-supplier-managed-and-consignment-inventory', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When the brief should run, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where track supplier managed and consignment inventory stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on track supplier managed and consignment inventory for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads track supplier managed and consignment inventory, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on supplier-managed and consignment inventory from Dynamics 365 ERP for a legal entity, drafts an email to the owner (saved, not sent), and a Teams-ready summary.', 'example_request': 'Give me the 7am supplier-managed and consignment inventory brief for USMF and draft it to the owner.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a daily or weekly supplier-managed/consignment inventory brief with top items, anomalies vs 7-day average, and next actions.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefTrackSupplierManagedAndConsignmentInventory(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefTrackSupplierManagedAndConsignmentInventory'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefTrackSupplierManagedAndConsignmentInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
