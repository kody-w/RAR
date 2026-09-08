---
name: "rar-cowork-cookbook-teams-update-measure-plan-adherence"
description: "Summarizes measure plan adherence from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_measure_plan_adherence", "rar_sha256": "e58251d7ef86b01d389d752e1c025e09dbde51434448b10c7e9395a0e57268d9", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
