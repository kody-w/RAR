---
name: "rar-cowork-cookbook-teams-update-develop-training-strategy"
description: "Summarizes develop training strategy status from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is p"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_develop_training_strategy", "rar_sha256": "a4eaee8e4ec28d1259617a8c0d95de415ceb683289733ea1e8ef97320d6c8d39", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
