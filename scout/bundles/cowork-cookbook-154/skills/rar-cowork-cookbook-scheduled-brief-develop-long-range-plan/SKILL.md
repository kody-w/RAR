---
name: "rar-cowork-cookbook-scheduled-brief-develop-long-range-plan"
description: "Builds a long-range-plan morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, saved as an email draft plus a Teams-ready summary."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_develop_long_range_plan", "rar_sha256": "e1310ce3ef4f1b5bf4dacd26853b0b615f00c1e8422ce8113c77d5d34b1e395c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_develop_long_range_plan`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_develop_long_range_plan_agent.py` and in the RCI capsule.

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

Develop long-range plan Scheduled Email Brief — Builds a long-range-plan morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, saved as an email draft plus a Teams-ready summary.

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-develop-long-range-plan
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
      "description": "Dynamics 365 F&SCM legal entity to query, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_develop_long_range_plan_agent.py` and embedded as the fenced Python below (sha256 e1310ce3ef4f1b5b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_develop_long_range_plan_agent.py` first:

```bash
python3 scheduled_brief_develop_long_range_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_develop_long_range_plan_agent.py   # or on stdin
python3 scheduled_brief_develop_long_range_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop long-range plan Scheduled Email Brief — Builds a long-range-plan morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, saved as an email draft plus a Teams-ready summary.

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-develop-long-range-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_develop_long_range_plan',
    "version": '3.0.3',
    "display_name": 'Develop long-range plan Scheduled Email Brief',
    "description": 'Builds a long-range-plan morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, saved as an email draft plus a Teams-ready summary.',
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
        "upstream_slug": 'scheduled-brief-develop-long-range-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-develop-long-range-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '63b839fbb3d92ef5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/develop-long-range-plan'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/scheduled-brief-develop-long-range-plan', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 F&SCM legal entity to query, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where develop long-range plan stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on develop long-range plan for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads develop long-range plan, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a long-range-plan morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, saved as an email draft plus a Teams-ready summary.', 'example_request': 'Give me the long-range plan morning brief for USMF and draft it to the owner.', 'inputs': [{'description': 'Dynamics 365 F&SCM legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a daily or weekly long-range planning brief for the responsible owner, drafted as an email and a Teams channel post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefDevelopLongRangePlan(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDevelopLongRangePlan'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 F&SCM legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefDevelopLongRangePlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
