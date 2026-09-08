---
name: "rar-cowork-cookbook-teams-update-forecast-service-parts-demand"
description: "Summarizes forecast service parts demand from the Dynamics 365 ERP plugin for a legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON file; nothing is posted automatically."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_forecast_service_parts_demand", "rar_sha256": "a8778c142c53109bf4dc9b122092831e618542d78085a6427a862e905aa8613a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
