---
name: "rar-cowork-cookbook-teams-update-plan-demand-consensus"
description: "Summarizes plan demand consensus from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not post anythin"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_plan_demand_consensus", "rar_sha256": "9245528d37106220382337939531cdb5835c07c3dcdd61d4ccef40d2e80e3b23", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
