---
name: "rar-cowork-cookbook-teams-update-reallocate-asset-budgets"
description: "Summarizes the current state of reallocate asset budgets from the Dynamics 365 ERP plugin for a legal entity, returning a markdown Teams channel post plus a saved Adaptive Card JSON file; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_reallocate_asset_budgets", "rar_sha256": "0e8524b84a82aa6f49cb25ad1428708611610b851d62792fc7a393d6fbeedacb", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
