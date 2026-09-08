---
name: "rar-cowork-cookbook-teams-update-allocate-inventory"
description: "Summarizes allocate inventory status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON; it does not post anything."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_allocate_inventory", "rar_sha256": "1bcd9efadff73a3843441a775279f3d36ade74bf94a5e0a4468726decc1f6749", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_allocate_inventory`. The original RAPP
agent is preserved byte-for-byte in `teams_update_allocate_inventory_agent.py` and in the RCI capsule.

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

Allocate inventory Teams Channel Update — Summarizes allocate inventory status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON; it does not post anything.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-allocate-inventory
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
      "description": "Filename for the Adaptive Card JSON, e.g. teams-update-allocate-inventory-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_allocate_inventory_agent.py` and embedded as the fenced Python below (sha256 1bcd9efadff73a38…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_allocate_inventory_agent.py` first:

```bash
python3 teams_update_allocate_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_allocate_inventory_agent.py   # or on stdin
python3 teams_update_allocate_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Allocate inventory Teams Channel Update — Summarizes allocate inventory status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON; it does not post anything.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-allocate-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_allocate_inventory',
    "version": '3.0.3',
    "display_name": 'Allocate inventory Teams Channel Update',
    "description": 'Summarizes allocate inventory status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON; it does not post anything.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-allocate-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-allocate-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '526a84f61f8fa0ff',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/execute-sales-and-operations/allocate-inventory'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/teams-update-allocate-inventory', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the Adaptive Card JSON, e.g. teams-update-allocate-inventory-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of allocate inventory. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-allocate-inventory-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads allocate inventory, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes allocate inventory status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON; it does not post anything.', 'example_request': "Draft a Teams post and Adaptive Card on allocate inventory status in USMF — save them, don't post.", 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-allocate-inventory-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update and Adaptive Card on allocate inventory status from Dynamics 365 F&SCM.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateAllocateInventory(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateAllocateInventory'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-allocate-inventory-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateAllocateInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
