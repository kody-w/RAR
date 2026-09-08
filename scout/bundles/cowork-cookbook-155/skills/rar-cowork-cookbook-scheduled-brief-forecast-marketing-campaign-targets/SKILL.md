---
name: "rar-cowork-cookbook-scheduled-brief-forecast-marketing-campaign-targets"
description: "Builds a morning brief on forecast marketing campaign targets from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an unsent draft email t"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_forecast_marketing_campaign_targets", "rar_sha256": "fb88873f759f8f55bcb9046836cefb095b7307b1239cda3c4ba204622ef9edb3", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_forecast_marketing_campaign_targets`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_forecast_marketing_campaign_targets_agent.py` and in the RCI capsule.

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

Forecast marketing campaign targets Scheduled Email Brief — Builds a morning brief on forecast marketing campaign targets from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an unsent draft email t

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-forecast-marketing-campaign-targets
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
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to query; the recipe uses USMF.",
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
    },
    "owner": {
      "description": "Responsible owner who receives the drafted email brief.",
      "type": "string"
    },
    "schedule": {
      "description": "When to run the brief, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_forecast_marketing_campaign_targets_agent.py` and embedded as the fenced Python below (sha256 fb88873f759f8f55…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_forecast_marketing_campaign_targets_agent.py` first:

```bash
python3 scheduled_brief_forecast_marketing_campaign_targets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_forecast_marketing_campaign_targets_agent.py   # or on stdin
python3 scheduled_brief_forecast_marketing_campaign_targets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Forecast marketing campaign targets Scheduled Email Brief — Builds a morning brief on forecast marketing campaign targets from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an unsent draft email t

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-forecast-marketing-campaign-targets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_forecast_marketing_campaign_targets',
    "version": '3.0.3',
    "display_name": 'Forecast marketing campaign targets Scheduled Email Brief',
    "description": 'Builds a morning brief on forecast marketing campaign targets from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an unsent draft email t',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-forecast-marketing-campaign-targets',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-forecast-marketing-campaign-targets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '67f4927528c784da',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/develop-marketing-strategy/forecast-marketing-campaign-targets'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/scheduled-brief-forecast-marketing-campaign-targets', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query; the recipe uses USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When to run the brief, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where forecast marketing campaign targets stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on forecast marketing campaign targets for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads forecast marketing campaign targets, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on forecast marketing campaign targets from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an unsent draft email t', 'example_request': 'Give me the 7am weekday brief on forecast marketing campaign targets in USMF and draft the email to the owner.', 'inputs': [{'description': 'D365 legal entity to query; the recipe uses USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When to run the brief, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a responsible owner wants a daily or weekly (weekday 7am) brief on forecast marketing campaign targets from D365 F&SCM, as a draft email and Teams post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefForecastMarketingCampaignTargets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefForecastMarketingCampaignTargets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query; the recipe uses USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When to run the brief, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefForecastMarketingCampaignTargets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
