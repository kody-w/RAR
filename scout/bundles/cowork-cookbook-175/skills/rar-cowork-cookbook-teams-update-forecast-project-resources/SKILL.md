---
name: "rar-cowork-cookbook-teams-update-forecast-project-resources"
description: "Summarizes forecast project resources from the Dynamics 365 ERP plugin for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs, status indicators, and quick-action but"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_forecast_project_resources", "rar_sha256": "3f17caa0b29de14afeb9e89604c47aecf5d771d1ff5e3c180ac0f950a33266af", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
