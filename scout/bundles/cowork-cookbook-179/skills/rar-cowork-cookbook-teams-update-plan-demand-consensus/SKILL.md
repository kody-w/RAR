---
name: "rar-cowork-cookbook-teams-update-plan-demand-consensus"
description: "Summarizes plan demand consensus from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not post anythin"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_plan_demand_consensus", "rar_sha256": "9245528d37106220382337939531cdb5835c07c3dcdd61d4ccef40d2e80e3b23", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_plan_demand_consensus`. The original RAPP
agent is preserved byte-for-byte in `teams_update_plan_demand_consensus_agent.py` and in the RCI capsule.

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

Plan demand consensus Teams Channel Update — Summarizes plan demand consensus from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not post anythin

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-plan-demand-consensus
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
      "description": "Filename for the saved Adaptive Card JSON, e.g. teams-update-plan-demand-consensus-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_plan_demand_consensus_agent.py` and embedded as the fenced Python below (sha256 9245528d37106220…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_plan_demand_consensus_agent.py` first:

```bash
python3 teams_update_plan_demand_consensus_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_plan_demand_consensus_agent.py   # or on stdin
python3 teams_update_plan_demand_consensus_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan demand consensus Teams Channel Update — Summarizes plan demand consensus from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not post anythin

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-plan-demand-consensus
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_plan_demand_consensus',
    "version": '3.0.3',
    "display_name": 'Plan demand consensus Teams Channel Update',
    "description": 'Summarizes plan demand consensus from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not post anythin',
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
        "upstream_slug": 'teams-update-plan-demand-consensus',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-plan-demand-consensus',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0c2bc0a50dff2d91',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-sales-and-operations-planning/plan-demand-consensus'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/teams-update-plan-demand-consensus', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the saved Adaptive Card JSON, e.g. teams-update-plan-demand-consensus-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of plan demand consensus. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-plan-demand-consensus-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads plan demand consensus, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes plan demand consensus from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not post anythin', 'example_request': "Draft a Teams post and Adaptive Card on plan demand consensus for USMF — save them, don't post.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the saved Adaptive Card JSON, e.g. teams-update-plan-demand-consensus-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update and Adaptive Card on plan demand consensus status from D365 ERP data, without auto-posting.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdatePlanDemandConsensus(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdatePlanDemandConsensus'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the saved Adaptive Card JSON, e.g. teams-update-plan-demand-consensus-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdatePlanDemandConsensus().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
