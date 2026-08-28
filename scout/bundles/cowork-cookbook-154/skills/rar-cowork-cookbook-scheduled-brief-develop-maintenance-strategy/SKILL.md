---
name: "rar-cowork-cookbook-scheduled-brief-develop-maintenance-strategy"
description: "Schedulable morning-brief email summarizing develop maintenance strategy for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_develop_maintenance_strategy", "rar_sha256": "2f2bb488f7d1eb39c7a4c2b2ff2d0f91b6f3476513a11c719a6fbf9f924e9612", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_develop_maintenance_strategy_agent.py` and embedded as the fenced Python below (sha256 2f2bb488f7d1eb39…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_develop_maintenance_strategy_agent.py` first:

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
    "version": '2.0.1',
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
