---
name: "rar-cowork-cookbook-scheduled-brief-develop-long-range-plan"
description: "Builds a long-range-plan morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, saved as an email draft plus a Teams-ready summary."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_develop_long_range_plan", "rar_sha256": "e1310ce3ef4f1b5bf4dacd26853b0b615f00c1e8422ce8113c77d5d34b1e395c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
