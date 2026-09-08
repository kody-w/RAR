---
name: "rar-cowork-cookbook-scheduled-brief-track-supplier-managed-and-consignment-inventory"
description: "Builds a morning brief on supplier-managed and consignment inventory from Dynamics 365 ERP for a legal entity, drafts an email to the owner (saved, not sent), and a Teams-ready summary."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_track_supplier_managed_and_consignment_inventory", "rar_sha256": "ed23249b79e9e1b7acb69f5d432ce3e2c90cbc44732f6b9c7054f22df5faf5c8", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
