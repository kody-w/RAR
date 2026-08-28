---
name: "rar-cowork-cookbook-scheduled-brief-modify-production-plan"
description: "Schedulable morning-brief email summarizing modify production plan for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_modify_production_plan", "rar_sha256": "ef4cb23df7bd09d79143a281f22e7060731ccb7f0f4254688e89eb6a928ed686", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_modify_production_plan`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_modify_production_plan_agent.py` and in the RCI capsule.

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

Modify production plan Scheduled Email Brief — Schedulable morning-brief email summarizing modify production plan for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-modify-production-plan
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
    "operation": {
      "description": "What to do: run, plan, checklist, describe.",
      "enum": [
        "run",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "subject": {
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_modify_production_plan_agent.py` and embedded as the fenced Python below (sha256 ef4cb23df7bd09d7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_modify_production_plan_agent.py` first:

```bash
python3 scheduled_brief_modify_production_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_modify_production_plan_agent.py   # or on stdin
python3 scheduled_brief_modify_production_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Modify production plan Scheduled Email Brief — Schedulable morning-brief email summarizing modify production plan for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-modify-production-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_modify_production_plan',
    "version": '2.0.0',
    "display_name": 'Modify production plan Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing modify production plan for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-modify-production-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-modify-production-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '760bfa7f3960a4bc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/plan-production-operations/modify-production-plan'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/scheduled-brief-modify-production-plan', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefModifyProductionPlan(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefModifyProductionPlan'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
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

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

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
    print(ScheduledBriefModifyProductionPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
