---
name: "rar-cowork-cookbook-scheduled-brief-develop-maintenance-strategy"
description: "Builds a morning brief on develop maintenance strategy from Dynamics 365 F&SCM data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, plus an email saved to"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_develop_maintenance_strategy", "rar_sha256": "760c751a11b3dbc78081b8abf815589e2c90ebc2375fcf9815b12d289079c51b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
