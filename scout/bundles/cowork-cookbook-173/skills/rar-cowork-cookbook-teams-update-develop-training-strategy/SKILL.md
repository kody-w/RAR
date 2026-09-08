---
name: "rar-cowork-cookbook-teams-update-develop-training-strategy"
description: "Summarizes develop training strategy status from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is p"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_develop_training_strategy", "rar_sha256": "a4eaee8e4ec28d1259617a8c0d95de415ceb683289733ea1e8ef97320d6c8d39", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_develop_training_strategy`. The original RAPP
agent is preserved byte-for-byte in `teams_update_develop_training_strategy_agent.py` and in the RCI capsule.

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

Develop training strategy Teams Channel Update — Summarizes develop training strategy status from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is p

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-develop-training-strategy
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
      "description": "Filename for the saved Adaptive Card JSON, e.g. teams-update-develop-training-strategy-2026-05-24-card.json.",
      "type": "string"
    },
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
    "quick_actions": {
      "description": "Quick-action buttons to include on the card, e.g. 'View detail', 'Open in D365'.",
      "type": "string"
    },
    "topic": {
      "description": "The initiative to summarize, e.g. develop training strategy.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_develop_training_strategy_agent.py` and embedded as the fenced Python below (sha256 a4eaee8e4ec28d12…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_develop_training_strategy_agent.py` first:

```bash
python3 teams_update_develop_training_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_develop_training_strategy_agent.py   # or on stdin
python3 teams_update_develop_training_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop training strategy Teams Channel Update — Summarizes develop training strategy status from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is p

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-develop-training-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_develop_training_strategy',
    "version": '3.0.3',
    "display_name": 'Develop training strategy Teams Channel Update',
    "description": 'Summarizes develop training strategy status from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is p',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-develop-training-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-develop-training-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '86e0958ebf663df7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/train-users-and-increase-adoption/develop-training-strategy'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-develop-training-strategy', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the saved Adaptive Card JSON, e.g. teams-update-develop-training-strategy-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'quick_actions': "Quick-action buttons to include on the card, e.g. 'View detail', 'Open in D365'.", 'topic': 'The initiative to summarize, e.g. develop training strategy.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of develop training strategy. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-develop-training-strategy-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads develop training strategy, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes develop training strategy status from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is p', 'example_request': "Draft a Teams update on develop training strategy from D365 USMF plus an Adaptive Card — save both, don't post.", 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'The initiative to summarize, e.g. develop training strategy.', 'name': 'topic'}, {'description': 'Filename for the saved Adaptive Card JSON, e.g. teams-update-develop-training-strategy-2026-05-24-card.json.', 'name': 'card_filename'}, {'description': "Quick-action buttons to include on the card, e.g. 'View detail', 'Open in D365'.", 'name': 'quick_actions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need a review-ready Teams channel update on develop training strategy status, drafted from D365 ERP data, without auto-posting.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateDevelopTrainingStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDevelopTrainingStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the saved Adaptive Card JSON, e.g. teams-update-develop-training-strategy-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'quick_actions': {'description': "Quick-action buttons to include on the card, e.g. 'View detail', 'Open in D365'.", 'type': 'string'}, 'topic': {'description': 'The initiative to summarize, e.g. develop training strategy.', 'type': 'string'}},
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
    print(TeamsUpdateDevelopTrainingStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
