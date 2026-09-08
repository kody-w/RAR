---
name: "rar-cowork-cookbook-teams-update-develop-product-strategy"
description: "Summarizes develop product strategy status from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs, status indicators, and quick-action bu"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_develop_product_strategy", "rar_sha256": "957a9602549fafba2b51878de165fefbd959e73ebab0dce566ec96ed843edd1a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_develop_product_strategy`. The original RAPP
agent is preserved byte-for-byte in `teams_update_develop_product_strategy_agent.py` and in the RCI capsule.

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

Develop product strategy Teams Channel Update — Summarizes develop product strategy status from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs, status indicators, and quick-action bu

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-develop-product-strategy
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
      "description": "Filename for the saved Adaptive Card JSON, e.g. teams-update-develop-product-strategy-2026-05-24-card.json.",
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
    "topic": {
      "description": "The initiative or area to report on, e.g. develop product strategy.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_develop_product_strategy_agent.py` and embedded as the fenced Python below (sha256 957a9602549fafba…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_develop_product_strategy_agent.py` first:

```bash
python3 teams_update_develop_product_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_develop_product_strategy_agent.py   # or on stdin
python3 teams_update_develop_product_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop product strategy Teams Channel Update — Summarizes develop product strategy status from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs, status indicators, and quick-action bu

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-develop-product-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_develop_product_strategy',
    "version": '3.0.3',
    "display_name": 'Develop product strategy Teams Channel Update',
    "description": 'Summarizes develop product strategy status from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs, status indicators, and quick-action bu',
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
        "upstream_slug": 'teams-update-develop-product-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-develop-product-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '021b3a9c86c6d1c5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/develop-product-strategy'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/teams-update-develop-product-strategy', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the saved Adaptive Card JSON, e.g. teams-update-develop-product-strategy-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.', 'topic': 'The initiative or area to report on, e.g. develop product strategy.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of develop product strategy. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-develop-product-strategy-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads develop product strategy, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes develop product strategy status from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs, status indicators, and quick-action bu', 'example_request': "Draft a Teams update on develop product strategy for USMF with an Adaptive Card — save it, don't post.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'The initiative or area to report on, e.g. develop product strategy.', 'name': 'topic'}, {'description': 'Filename for the saved Adaptive Card JSON, e.g. teams-update-develop-product-strategy-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update plus Adaptive Card on develop product strategy status pulled from D365 F&SCM, saved not posted.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateDevelopProductStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDevelopProductStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the saved Adaptive Card JSON, e.g. teams-update-develop-product-strategy-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'topic': {'description': 'The initiative or area to report on, e.g. develop product strategy.', 'type': 'string'}},
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
    print(TeamsUpdateDevelopProductStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
