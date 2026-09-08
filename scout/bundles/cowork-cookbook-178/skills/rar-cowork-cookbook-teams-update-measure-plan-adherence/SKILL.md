---
name: "rar-cowork-cookbook-teams-update-measure-plan-adherence"
description: "Summarizes measure plan adherence from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_measure_plan_adherence", "rar_sha256": "e58251d7ef86b01d389d752e1c025e09dbde51434448b10c7e9395a0e57268d9", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_measure_plan_adherence`. The original RAPP
agent is preserved byte-for-byte in `teams_update_measure_plan_adherence_agent.py` and in the RCI capsule.

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

Measure plan adherence Teams Channel Update — Summarizes measure plan adherence from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-measure-plan-adherence
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
      "description": "Output filename for the Adaptive Card JSON, e.g. teams-update-measure-plan-adherence-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_measure_plan_adherence_agent.py` and embedded as the fenced Python below (sha256 e58251d7ef86b01d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_measure_plan_adherence_agent.py` first:

```bash
python3 teams_update_measure_plan_adherence_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_measure_plan_adherence_agent.py   # or on stdin
python3 teams_update_measure_plan_adherence_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Measure plan adherence Teams Channel Update — Summarizes measure plan adherence from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-measure-plan-adherence
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_measure_plan_adherence',
    "version": '3.0.3',
    "display_name": 'Measure plan adherence Teams Channel Update',
    "description": 'Summarizes measure plan adherence from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.',
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
        "upstream_slug": 'teams-update-measure-plan-adherence',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-measure-plan-adherence',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '653b1282dba9d307',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/analyze-business-performance/measure-plan-adherence'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/teams-update-measure-plan-adherence', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output filename for the Adaptive Card JSON, e.g. teams-update-measure-plan-adherence-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of measure plan adherence. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-measure-plan-adherence-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads measure plan adherence, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes measure plan adherence from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.', 'example_request': "Draft a Teams update on measure plan adherence for USMF with an Adaptive Card, but don't post it.", 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-measure-plan-adherence-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update plus Adaptive Card on measure plan adherence from D365 F&SCM data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateMeasurePlanAdherence(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateMeasurePlanAdherence'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-measure-plan-adherence-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateMeasurePlanAdherence().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
