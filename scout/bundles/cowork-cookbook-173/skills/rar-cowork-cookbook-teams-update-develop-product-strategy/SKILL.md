---
name: "rar-cowork-cookbook-teams-update-develop-product-strategy"
description: "Summarizes develop product strategy status from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs, status indicators, and quick-action bu"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_develop_product_strategy", "rar_sha256": "957a9602549fafba2b51878de165fefbd959e73ebab0dce566ec96ed843edd1a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
