---
name: "rar-cowork-cookbook-teams-update-forecast-service-parts-demand"
description: "Summarizes forecast service parts demand from the Dynamics 365 ERP plugin for a legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON file; nothing is posted automatically."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_forecast_service_parts_demand", "rar_sha256": "a8778c142c53109bf4dc9b122092831e618542d78085a6427a862e905aa8613a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_forecast_service_parts_demand`. The original RAPP
agent is preserved byte-for-byte in `teams_update_forecast_service_parts_demand_agent.py` and in the RCI capsule.

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

Forecast service parts demand Teams Channel Update — Summarizes forecast service parts demand from the Dynamics 365 ERP plugin for a legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON file; nothing is posted automatically.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-forecast-service-parts-demand
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
      "description": "Output filename for the Adaptive Card JSON, e.g. teams-update-forecast-service-parts-demand-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_forecast_service_parts_demand_agent.py` and embedded as the fenced Python below (sha256 a8778c142c53109b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_forecast_service_parts_demand_agent.py` first:

```bash
python3 teams_update_forecast_service_parts_demand_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_forecast_service_parts_demand_agent.py   # or on stdin
python3 teams_update_forecast_service_parts_demand_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Forecast service parts demand Teams Channel Update — Summarizes forecast service parts demand from the Dynamics 365 ERP plugin for a legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON file; nothing is posted automatically.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-forecast-service-parts-demand
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_forecast_service_parts_demand',
    "version": '3.0.3',
    "display_name": 'Forecast service parts demand Teams Channel Update',
    "description": 'Summarizes forecast service parts demand from the Dynamics 365 ERP plugin for a legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON file; nothing is posted automatically.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-forecast-service-parts-demand',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-forecast-service-parts-demand',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c49948b86199d4b4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/plan-service-work/forecast-service-parts-demand'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/teams-update-forecast-service-parts-demand', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output filename for the Adaptive Card JSON, e.g. teams-update-forecast-service-parts-demand-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of forecast service parts demand. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-forecast-service-parts-demand-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads forecast service parts demand, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes forecast service parts demand from the Dynamics 365 ERP plugin for a legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON file; nothing is posted automatically.', 'example_request': "Draft a Teams update on forecast service parts demand for USMF with an Adaptive Card, but don't post it.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-forecast-service-parts-demand-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update and Adaptive Card on forecast service parts demand status from D365 F&SCM data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateForecastServicePartsDemand(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateForecastServicePartsDemand'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-forecast-service-parts-demand-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateForecastServicePartsDemand().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
