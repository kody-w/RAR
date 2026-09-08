---
name: "rar-cowork-cookbook-scheduled-brief-plan-demand-consensus"
description: "Builds a morning brief on plan demand consensus from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_plan_demand_consensus", "rar_sha256": "38ce53bbea9eab3eb93d531351bef4ba981654dc0baebb57fc1a5d724674ff71", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_plan_demand_consensus`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_plan_demand_consensus_agent.py` and in the RCI capsule.

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

Plan demand consensus Scheduled Email Brief — Builds a morning brief on plan demand consensus from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-plan-demand-consensus
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
      "description": "D365 F&SCM legal entity to query; defaults to USMF.",
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
      "description": "Responsible owner who receives the drafted email.",
      "type": "string"
    },
    "schedule": {
      "description": "When to run, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_plan_demand_consensus_agent.py` and embedded as the fenced Python below (sha256 38ce53bbea9eab3e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_plan_demand_consensus_agent.py` first:

```bash
python3 scheduled_brief_plan_demand_consensus_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_plan_demand_consensus_agent.py   # or on stdin
python3 scheduled_brief_plan_demand_consensus_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan demand consensus Scheduled Email Brief — Builds a morning brief on plan demand consensus from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-plan-demand-consensus
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_plan_demand_consensus',
    "version": '3.0.3',
    "display_name": 'Plan demand consensus Scheduled Email Brief',
    "description": 'Builds a morning brief on plan demand consensus from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-plan-demand-consensus',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-plan-demand-consensus',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2faecc9af57499b8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-sales-and-operations-planning/plan-demand-consensus'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/scheduled-brief-plan-demand-consensus', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 F&SCM legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email.', 'schedule': 'When to run, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where plan demand consensus stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on plan demand consensus for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads plan demand consensus, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on plan demand consensus from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus', 'example_request': 'Draft my plan demand consensus morning brief for USMF and email it to the owner as a draft.', 'inputs': [{'description': 'D365 F&SCM legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email.', 'name': 'owner'}, {'description': 'When to run, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a demand planning owner wants a daily or weekly plan demand consensus brief drafted as an unsent email and a Teams channel summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefPlanDemandConsensus(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefPlanDemandConsensus'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email.', 'type': 'string'}, 'schedule': {'description': 'When to run, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefPlanDemandConsensus().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
