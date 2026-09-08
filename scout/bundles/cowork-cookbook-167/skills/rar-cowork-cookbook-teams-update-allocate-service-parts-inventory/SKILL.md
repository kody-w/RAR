---
name: "rar-cowork-cookbook-teams-update-allocate-service-parts-inventory"
description: "Summarizes service parts inventory allocation for a Dynamics 365 legal entity and returns a draft Teams channel post plus an Adaptive Card JSON file with KPIs and quick actions; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_allocate_service_parts_inventory", "rar_sha256": "5a2a0bad45982d66a3d3e08e6add26836c5a1fa03b8a12ff7e2eface7c9fbb55", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_allocate_service_parts_inventory`. The original RAPP
agent is preserved byte-for-byte in `teams_update_allocate_service_parts_inventory_agent.py` and in the RCI capsule.

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

Allocate service parts inventory Teams Channel Update — Summarizes service parts inventory allocation for a Dynamics 365 legal entity and returns a draft Teams channel post plus an Adaptive Card JSON file with KPIs and quick actions; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-allocate-service-parts-inventory
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
    "card_filename": {
      "description": "Output filename for the Adaptive Card JSON, e.g. teams-update-allocate-service-parts-inventory-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to summarize, e.g. USMF.",
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
    "scope": {
      "description": "Optional scope adjustments for the inventory allocation summary.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_allocate_service_parts_inventory_agent.py` and embedded as the fenced Python below (sha256 5a2a0bad45982d66…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_allocate_service_parts_inventory_agent.py` first:

```bash
python3 teams_update_allocate_service_parts_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_allocate_service_parts_inventory_agent.py   # or on stdin
python3 teams_update_allocate_service_parts_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Allocate service parts inventory Teams Channel Update — Summarizes service parts inventory allocation for a Dynamics 365 legal entity and returns a draft Teams channel post plus an Adaptive Card JSON file with KPIs and quick actions; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-allocate-service-parts-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_allocate_service_parts_inventory',
    "version": '3.0.3',
    "display_name": 'Allocate service parts inventory Teams Channel Update',
    "description": 'Summarizes service parts inventory allocation for a Dynamics 365 legal entity and returns a draft Teams channel post plus an Adaptive Card JSON file with KPIs and quick actions; nothing is posted.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-allocate-service-parts-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-allocate-service-parts-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '92db232663cbe95a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/manage-service-work/allocate-service-parts-inventory'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/teams-update-allocate-service-parts-inventory', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output filename for the Adaptive Card JSON, e.g. teams-update-allocate-service-parts-inventory-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.', 'scope': 'Optional scope adjustments for the inventory allocation summary.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of allocate service parts inventory. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-allocate-service-parts-inventory-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads allocate service parts inventory, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes service parts inventory allocation for a Dynamics 365 legal entity and returns a draft Teams channel post plus an Adaptive Card JSON file with KPIs and quick actions; nothing is posted.', 'example_request': "Draft a Teams post and Adaptive Card on allocate service parts inventory in USMF — don't post it, just save it.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-allocate-service-parts-inventory-2026-05-24-card.json.', 'name': 'card_filename'}, {'description': 'Optional scope adjustments for the inventory allocation summary.', 'name': 'scope'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams update and Adaptive Card on allocate service parts inventory status from Dynamics 365 F&SCM.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateAllocateServicePartsInventory(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateAllocateServicePartsInventory'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-allocate-service-parts-inventory-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'scope': {'description': 'Optional scope adjustments for the inventory allocation summary.', 'type': 'string'}},
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
    print(TeamsUpdateAllocateServicePartsInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
