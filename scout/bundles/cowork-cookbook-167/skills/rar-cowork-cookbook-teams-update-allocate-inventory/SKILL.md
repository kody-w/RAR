---
name: "rar-cowork-cookbook-teams-update-allocate-inventory"
description: "Summarizes allocate inventory status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON; it does not post anything."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_allocate_inventory", "rar_sha256": "1bcd9efadff73a3843441a775279f3d36ade74bf94a5e0a4468726decc1f6749", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
