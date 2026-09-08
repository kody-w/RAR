---
name: "rar-cowork-cookbook-scheduled-brief-forecast-marketing-campaign-targets"
description: "Builds a morning brief on forecast marketing campaign targets from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an unsent draft email t"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_forecast_marketing_campaign_targets", "rar_sha256": "fb88873f759f8f55bcb9046836cefb095b7307b1239cda3c4ba204622ef9edb3", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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
