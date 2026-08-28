---
name: "rar-cowork-cookbook-scheduled-brief-develop-maintenance-strategy"
description: "Schedulable morning-brief email summarizing develop maintenance strategy for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_develop_maintenance_strategy", "rar_sha256": "510ef0e5be328de3007a30ee7381b8f47cf9b85a1883be4970e287733e6b9f58", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

Develop maintenance strategy Scheduled Email Brief — Schedulable morning-brief email summarizing develop maintenance strategy for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_develop_maintenance_strategy_agent.py` and embedded as the fenced Python below (sha256 510ef0e5be328de3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_develop_maintenance_strategy_agent.py` first:

```bash
python3 scheduled_brief_develop_maintenance_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_develop_maintenance_strategy_agent.py   # or on stdin
python3 scheduled_brief_develop_maintenance_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop maintenance strategy Scheduled Email Brief — Schedulable morning-brief email summarizing develop maintenance strategy for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

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
    "version": '2.0.0',
    "display_name": 'Develop maintenance strategy Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing develop maintenance strategy for the responsible owner; designed to run daily or weekly.',
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
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5cf0b495a18702dd',
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


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefDevelopMaintenanceStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDevelopMaintenanceStrategy'
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
    print(ScheduledBriefDevelopMaintenanceStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
