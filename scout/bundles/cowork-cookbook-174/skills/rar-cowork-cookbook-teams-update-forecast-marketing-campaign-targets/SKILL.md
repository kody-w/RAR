---
name: "rar-cowork-cookbook-teams-update-forecast-marketing-campaign-targets"
description: "Summarizes forecast marketing campaign targets from Dynamics 365 ERP for a given legal entity and saves two artifacts for review: a markdown Teams channel post and an Adaptive Card JSON; it does not post anything."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_forecast_marketing_campaign_targets", "rar_sha256": "867f2a8e2d8ce15e77cac3e65aeda1122d53aa228b68dee6b8a223d09ccf8aaf", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_forecast_marketing_campaign_targets`. The original RAPP
agent is preserved byte-for-byte in `teams_update_forecast_marketing_campaign_targets_agent.py` and in the RCI capsule.

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

Forecast marketing campaign targets Teams Channel Update — Summarizes forecast marketing campaign targets from Dynamics 365 ERP for a given legal entity and saves two artifacts for review: a markdown Teams channel post and an Adaptive Card JSON; it does not post anything.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-forecast-marketing-campaign-targets
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
      "description": "Output Adaptive Card JSON filename, e.g. teams-update-forecast-marketing-campaign-targets-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_forecast_marketing_campaign_targets_agent.py` and embedded as the fenced Python below (sha256 867f2a8e2d8ce15e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_forecast_marketing_campaign_targets_agent.py` first:

```bash
python3 teams_update_forecast_marketing_campaign_targets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_forecast_marketing_campaign_targets_agent.py   # or on stdin
python3 teams_update_forecast_marketing_campaign_targets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Forecast marketing campaign targets Teams Channel Update — Summarizes forecast marketing campaign targets from Dynamics 365 ERP for a given legal entity and saves two artifacts for review: a markdown Teams channel post and an Adaptive Card JSON; it does not post anything.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-forecast-marketing-campaign-targets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_forecast_marketing_campaign_targets',
    "version": '3.0.3',
    "display_name": 'Forecast marketing campaign targets Teams Channel Update',
    "description": 'Summarizes forecast marketing campaign targets from Dynamics 365 ERP for a given legal entity and saves two artifacts for review: a markdown Teams channel post and an Adaptive Card JSON; it does not post anything.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-forecast-marketing-campaign-targets',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-forecast-marketing-campaign-targets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '89bac41943a7da32',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/develop-marketing-strategy/forecast-marketing-campaign-targets'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/teams-update-forecast-marketing-campaign-targets', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output Adaptive Card JSON filename, e.g. teams-update-forecast-marketing-campaign-targets-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of forecast marketing campaign targets. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-forecast-marketing-campaign-targets-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads forecast marketing campaign targets, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes forecast marketing campaign targets from Dynamics 365 ERP for a given legal entity and saves two artifacts for review: a markdown Teams channel post and an Adaptive Card JSON; it does not post anything.', 'example_request': "Draft a Teams update on forecast marketing campaign targets for USMF with an Adaptive Card — don't post it.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Output Adaptive Card JSON filename, e.g. teams-update-forecast-marketing-campaign-targets-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a ready-to-review Teams channel update plus Adaptive Card on forecast marketing campaign targets status from D365 F&SCM.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateForecastMarketingCampaignTargets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateForecastMarketingCampaignTargets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output Adaptive Card JSON filename, e.g. teams-update-forecast-marketing-campaign-targets-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateForecastMarketingCampaignTargets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
