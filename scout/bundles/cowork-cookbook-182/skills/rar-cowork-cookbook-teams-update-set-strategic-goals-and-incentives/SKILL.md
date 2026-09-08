---
name: "rar-cowork-cookbook-teams-update-set-strategic-goals-and-incentives"
description: "Summarizes the current state of strategic goals and incentives from Dynamics 365 ERP for a legal entity, returning a markdown Teams channel post plus a saved Adaptive Card JSON; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_set_strategic_goals_and_incentives", "rar_sha256": "c72764bc6445b57eb9bbcf4f279eed42f245d3d51e6b3df0256f3da03b48aa01", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_set_strategic_goals_and_incentives`. The original RAPP
agent is preserved byte-for-byte in `teams_update_set_strategic_goals_and_incentives_agent.py` and in the RCI capsule.

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

Set strategic goals and incentives Teams Channel Update — Summarizes the current state of strategic goals and incentives from Dynamics 365 ERP for a legal entity, returning a markdown Teams channel post plus a saved Adaptive Card JSON; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-set-strategic-goals-and-incentives
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
      "description": "Filename for the generated Adaptive Card JSON artifact.",
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
    "scope": {
      "description": "Optional adjustment to the scope of the goals/incentives summary.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_set_strategic_goals_and_incentives_agent.py` and embedded as the fenced Python below (sha256 c72764bc6445b57e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_set_strategic_goals_and_incentives_agent.py` first:

```bash
python3 teams_update_set_strategic_goals_and_incentives_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_set_strategic_goals_and_incentives_agent.py   # or on stdin
python3 teams_update_set_strategic_goals_and_incentives_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Set strategic goals and incentives Teams Channel Update — Summarizes the current state of strategic goals and incentives from Dynamics 365 ERP for a legal entity, returning a markdown Teams channel post plus a saved Adaptive Card JSON; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-set-strategic-goals-and-incentives
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_set_strategic_goals_and_incentives',
    "version": '3.0.3',
    "display_name": 'Set strategic goals and incentives Teams Channel Update',
    "description": 'Summarizes the current state of strategic goals and incentives from Dynamics 365 ERP for a legal entity, returning a markdown Teams channel post plus a saved Adaptive Card JSON; nothing is posted.',
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
        "upstream_slug": 'teams-update-set-strategic-goals-and-incentives',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-set-strategic-goals-and-incentives',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '82beea4c94701f2c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/set-strategic-goals-and-incentives'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/teams-update-set-strategic-goals-and-incentives', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the generated Adaptive Card JSON artifact.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'scope': 'Optional adjustment to the scope of the goals/incentives summary.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of set strategic goals and incentives. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-set-strategic-goals-and-incentives-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads set strategic goals and incentives, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes the current state of strategic goals and incentives from Dynamics 365 ERP for a legal entity, returning a markdown Teams channel post plus a saved Adaptive Card JSON; nothing is posted.', 'example_request': "Draft a Teams update on strategic goals and incentives for USMF with an Adaptive Card — don't post it, just save it.", 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the generated Adaptive Card JSON artifact.', 'name': 'card_filename'}, {'description': 'Optional adjustment to the scope of the goals/incentives summary.', 'name': 'scope'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams update on strategic goals and incentives status from D365 F&SCM, with KPIs and quick-action buttons in an Adaptive Card.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateSetStrategicGoalsAndIncentives(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateSetStrategicGoalsAndIncentives'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the generated Adaptive Card JSON artifact.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'scope': {'description': 'Optional adjustment to the scope of the goals/incentives summary.', 'type': 'string'}},
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
    print(TeamsUpdateSetStrategicGoalsAndIncentives().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
