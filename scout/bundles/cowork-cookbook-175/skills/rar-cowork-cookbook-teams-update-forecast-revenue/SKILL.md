---
name: "rar-cowork-cookbook-teams-update-forecast-revenue"
description: "Summarizes forecast revenue from the Dynamics 365 ERP plugin for a given legal entity and returns a draft Teams channel post (markdown) plus an Adaptive Card JSON file saved for review, never posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_forecast_revenue", "rar_sha256": "36bd5d9e5585b4b41398acb3affd47075b849b968ed739df16e9b86dd13070a0", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_forecast_revenue`. The original RAPP
agent is preserved byte-for-byte in `teams_update_forecast_revenue_agent.py` and in the RCI capsule.

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

Forecast revenue Teams Channel Update — Summarizes forecast revenue from the Dynamics 365 ERP plugin for a given legal entity and returns a draft Teams channel post (markdown) plus an Adaptive Card JSON file saved for review, never posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-forecast-revenue
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
      "description": "Filename for the Adaptive Card JSON, e.g. teams-update-forecast-revenue-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_forecast_revenue_agent.py` and embedded as the fenced Python below (sha256 36bd5d9e5585b4b4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_forecast_revenue_agent.py` first:

```bash
python3 teams_update_forecast_revenue_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_forecast_revenue_agent.py   # or on stdin
python3 teams_update_forecast_revenue_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Forecast revenue Teams Channel Update — Summarizes forecast revenue from the Dynamics 365 ERP plugin for a given legal entity and returns a draft Teams channel post (markdown) plus an Adaptive Card JSON file saved for review, never posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-forecast-revenue
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_forecast_revenue',
    "version": '3.0.3',
    "display_name": 'Forecast revenue Teams Channel Update',
    "description": 'Summarizes forecast revenue from the Dynamics 365 ERP plugin for a given legal entity and returns a draft Teams channel post (markdown) plus an Adaptive Card JSON file saved for review, never posted.',
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
        "upstream_slug": 'teams-update-forecast-revenue',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-forecast-revenue',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '21a515d6c0b032cc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-financial-planning/forecast-revenue'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/teams-update-forecast-revenue', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the Adaptive Card JSON, e.g. teams-update-forecast-revenue-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of forecast revenue. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-forecast-revenue-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads forecast revenue, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes forecast revenue from the Dynamics 365 ERP plugin for a given legal entity and returns a draft Teams channel post (markdown) plus an Adaptive Card JSON file saved for review, never posted.', 'example_request': "Draft a Teams update on forecast revenue for USMF with an Adaptive Card — save it, don't post it.", 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-forecast-revenue-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a ready-to-review Teams channel update on forecast revenue status, with KPI Adaptive Card artifacts saved rather than posted.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateForecastRevenue(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateForecastRevenue'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-forecast-revenue-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateForecastRevenue().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
