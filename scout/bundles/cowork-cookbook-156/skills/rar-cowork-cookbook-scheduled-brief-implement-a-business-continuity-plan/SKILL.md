---
name: "rar-cowork-cookbook-scheduled-brief-implement-a-business-continuity-plan"
description: "Builds a business continuity morning brief from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; drafts an owner email and a Teams-ready summary"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_implement_a_business_continuity_plan", "rar_sha256": "629bd98ac7b0058dc91f6d45b4ef8cde8370097d83d3f3dacb3f77dc4546617e", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
