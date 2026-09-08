---
name: "rar-cowork-cookbook-scheduled-brief-plan-demand-consensus"
description: "Builds a morning brief on plan demand consensus from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_plan_demand_consensus", "rar_sha256": "38ce53bbea9eab3eb93d531351bef4ba981654dc0baebb57fc1a5d724674ff71", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
