---
name: "rar-cowork-cookbook-teams-update-allocate-service-parts-inventory"
description: "Summarizes service parts inventory allocation for a Dynamics 365 legal entity and returns a draft Teams channel post plus an Adaptive Card JSON file with KPIs and quick actions; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_allocate_service_parts_inventory", "rar_sha256": "5a2a0bad45982d66a3d3e08e6add26836c5a1fa03b8a12ff7e2eface7c9fbb55", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
