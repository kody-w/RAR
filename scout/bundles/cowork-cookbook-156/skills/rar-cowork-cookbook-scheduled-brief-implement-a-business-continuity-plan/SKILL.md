---
name: "rar-cowork-cookbook-scheduled-brief-implement-a-business-continuity-plan"
description: "Builds a business continuity morning brief from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; drafts an owner email and a Teams-ready summary"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_implement_a_business_continuity_plan", "rar_sha256": "629bd98ac7b0058dc91f6d45b4ef8cde8370097d83d3f3dacb3f77dc4546617e", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_implement_a_business_continuity_plan`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_implement_a_business_continuity_plan_agent.py` and in the RCI capsule.

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

Implement a business continuity plan Scheduled Email Brief — Builds a business continuity morning brief from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; drafts an owner email and a Teams-ready summary

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-implement-a-business-continuity-plan
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
      "description": "Dynamics 365 F&SCM legal entity to query; defaults to USMF.",
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
      "description": "Optional cadence for the scheduled task, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_implement_a_business_continuity_plan_agent.py` and embedded as the fenced Python below (sha256 629bd98ac7b0058d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_implement_a_business_continuity_plan_agent.py` first:

```bash
python3 scheduled_brief_implement_a_business_continuity_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_implement_a_business_continuity_plan_agent.py   # or on stdin
python3 scheduled_brief_implement_a_business_continuity_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Implement a business continuity plan Scheduled Email Brief — Builds a business continuity morning brief from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; drafts an owner email and a Teams-ready summary

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-implement-a-business-continuity-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_implement_a_business_continuity_plan',
    "version": '3.0.3',
    "display_name": 'Implement a business continuity plan Scheduled Email Brief',
    "description": 'Builds a business continuity morning brief from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; drafts an owner email and a Teams-ready summary',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-implement-a-business-continuity-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-implement-a-business-continuity-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4aa35eddb56778bd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/implement-a-business-continuity-plan'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-implement-a-business-continuity-plan', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 F&SCM legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where implement a business continuity plan stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on implement a business continuity plan for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads implement a business continuity plan, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a business continuity morning brief from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; drafts an owner email and a Teams-ready summary', 'example_request': 'Give me the business continuity morning brief for USMF and draft it to the owner.', 'inputs': [{'description': 'Dynamics 365 F&SCM legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a daily or weekly business continuity brief for the responsible owner, saved as an email draft plus a Teams channel summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefImplementABusinessContinuityPlan(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefImplementABusinessContinuityPlan'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 F&SCM legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefImplementABusinessContinuityPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
