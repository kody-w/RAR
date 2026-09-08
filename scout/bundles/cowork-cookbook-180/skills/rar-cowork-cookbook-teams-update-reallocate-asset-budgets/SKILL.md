---
name: "rar-cowork-cookbook-teams-update-reallocate-asset-budgets"
description: "Summarizes the current state of reallocate asset budgets from the Dynamics 365 ERP plugin for a legal entity, returning a markdown Teams channel post plus a saved Adaptive Card JSON file; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_reallocate_asset_budgets", "rar_sha256": "0e8524b84a82aa6f49cb25ad1428708611610b851d62792fc7a393d6fbeedacb", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_reallocate_asset_budgets`. The original RAPP
agent is preserved byte-for-byte in `teams_update_reallocate_asset_budgets_agent.py` and in the RCI capsule.

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

Reallocate asset budgets Teams Channel Update — Summarizes the current state of reallocate asset budgets from the Dynamics 365 ERP plugin for a legal entity, returning a markdown Teams channel post plus a saved Adaptive Card JSON file; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-reallocate-asset-budgets
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
      "description": "Filename for the generated Adaptive Card JSON, e.g. teams-update-reallocate-asset-budgets-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_reallocate_asset_budgets_agent.py` and embedded as the fenced Python below (sha256 0e8524b84a82aa6f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_reallocate_asset_budgets_agent.py` first:

```bash
python3 teams_update_reallocate_asset_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_reallocate_asset_budgets_agent.py   # or on stdin
python3 teams_update_reallocate_asset_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Reallocate asset budgets Teams Channel Update — Summarizes the current state of reallocate asset budgets from the Dynamics 365 ERP plugin for a legal entity, returning a markdown Teams channel post plus a saved Adaptive Card JSON file; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-reallocate-asset-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_reallocate_asset_budgets',
    "version": '3.0.3',
    "display_name": 'Reallocate asset budgets Teams Channel Update',
    "description": 'Summarizes the current state of reallocate asset budgets from the Dynamics 365 ERP plugin for a legal entity, returning a markdown Teams channel post plus a saved Adaptive Card JSON file; nothing is posted.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'teams-update-reallocate-asset-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-reallocate-asset-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b8ef9897f0033232',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/reallocate-asset-budgets'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/teams-update-reallocate-asset-budgets', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-reallocate-asset-budgets-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of reallocate asset budgets. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-reallocate-asset-budgets-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Reads reallocate asset budgets, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes the current state of reallocate asset budgets from the Dynamics 365 ERP plugin for a legal entity, returning a markdown Teams channel post plus a saved Adaptive Card JSON file; nothing is posted.', 'example_request': "Draft a Teams channel update on reallocate asset budgets for USMF with an Adaptive Card, but don't post it.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-reallocate-asset-budgets-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update on reallocate asset budgets status, with an Adaptive Card of KPIs and quick actions saved for manual posting.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateReallocateAssetBudgets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateReallocateAssetBudgets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-reallocate-asset-budgets-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateReallocateAssetBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
