---
name: "rar-cowork-cookbook-scheduled-brief-develop-maintenance-strategy"
description: "Builds a morning brief on develop maintenance strategy from Dynamics 365 F&SCM data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, plus an email saved to"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_develop_maintenance_strategy", "rar_sha256": "760c751a11b3dbc78081b8abf815589e2c90ebc2375fcf9815b12d289079c51b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_develop_maintenance_strategy`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_develop_maintenance_strategy_agent.py` and in the RCI capsule.

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

Develop maintenance strategy Scheduled Email Brief — Builds a morning brief on develop maintenance strategy from Dynamics 365 F&SCM data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, plus an email saved to

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-develop-maintenance-strategy
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
      "description": "D365 legal entity to query, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_develop_maintenance_strategy_agent.py` and embedded as the fenced Python below (sha256 760c751a11b3dbc7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_develop_maintenance_strategy_agent.py` first:

```bash
python3 scheduled_brief_develop_maintenance_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_develop_maintenance_strategy_agent.py   # or on stdin
python3 scheduled_brief_develop_maintenance_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop maintenance strategy Scheduled Email Brief — Builds a morning brief on develop maintenance strategy from Dynamics 365 F&SCM data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, plus an email saved to

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-develop-maintenance-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_develop_maintenance_strategy',
    "version": '3.0.3',
    "display_name": 'Develop maintenance strategy Scheduled Email Brief',
    "description": 'Builds a morning brief on develop maintenance strategy from Dynamics 365 F&SCM data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, plus an email saved to',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'scheduled-brief-develop-maintenance-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-develop-maintenance-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'dcafc2f39bf499cb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/define-asset-strategy/develop-maintenance-strategy'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/scheduled-brief-develop-maintenance-strategy', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where develop maintenance strategy stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on develop maintenance strategy for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Reads develop maintenance strategy, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on develop maintenance strategy from Dynamics 365 F&SCM data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, plus an email saved to', 'example_request': 'Give me the maintenance strategy morning brief for USMF and draft it to the owner.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Use for a daily or weekly (weekday 7am) maintenance-strategy brief for the responsible owner, drafted as an unsent email and a Teams channel post summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefDevelopMaintenanceStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDevelopMaintenanceStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefDevelopMaintenanceStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
