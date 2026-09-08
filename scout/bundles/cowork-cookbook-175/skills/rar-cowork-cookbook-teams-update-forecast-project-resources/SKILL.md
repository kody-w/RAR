---
name: "rar-cowork-cookbook-teams-update-forecast-project-resources"
description: "Summarizes forecast project resources from the Dynamics 365 ERP plugin for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs, status indicators, and quick-action but"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_forecast_project_resources", "rar_sha256": "3f17caa0b29de14afeb9e89604c47aecf5d771d1ff5e3c180ac0f950a33266af", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_forecast_project_resources`. The original RAPP
agent is preserved byte-for-byte in `teams_update_forecast_project_resources_agent.py` and in the RCI capsule.

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

Forecast project resources Teams Channel Update — Summarizes forecast project resources from the Dynamics 365 ERP plugin for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs, status indicators, and quick-action but

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-forecast-project-resources
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
      "description": "Filename for the generated Adaptive Card JSON, e.g. teams-update-forecast-project-resources-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_forecast_project_resources_agent.py` and embedded as the fenced Python below (sha256 3f17caa0b29de14a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_forecast_project_resources_agent.py` first:

```bash
python3 teams_update_forecast_project_resources_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_forecast_project_resources_agent.py   # or on stdin
python3 teams_update_forecast_project_resources_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Forecast project resources Teams Channel Update — Summarizes forecast project resources from the Dynamics 365 ERP plugin for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs, status indicators, and quick-action but

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-forecast-project-resources
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_forecast_project_resources',
    "version": '3.0.3',
    "display_name": 'Forecast project resources Teams Channel Update',
    "description": 'Summarizes forecast project resources from the Dynamics 365 ERP plugin for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs, status indicators, and quick-action but',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-forecast-project-resources',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-forecast-project-resources',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '93ff5a9702d4abba',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/plan-projects/forecast-project-resources'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/teams-update-forecast-project-resources', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-forecast-project-resources-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of forecast project resources. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-forecast-project-resources-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads forecast project resources, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes forecast project resources from the Dynamics 365 ERP plugin for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs, status indicators, and quick-action but', 'example_request': "Draft a Teams update on forecast project resources for USMF with an Adaptive Card — don't post it, just save it.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-forecast-project-resources-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update on forecast project resources status from D365 F&SCM, with an Adaptive Card saved for manual posting.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateForecastProjectResources(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateForecastProjectResources'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-forecast-project-resources-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateForecastProjectResources().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
