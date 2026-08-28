---
name: "rar-cowork-cookbook-adaptive-card-schedule-dock-appointments"
description: "Produces a reusable Adaptive Card JSON snapshot of schedule dock appointments status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_schedule_dock_appointments", "rar_sha256": "feb48a9df779b1fd71b814174f2164408a172eef1b9b5486f3faff3978562aca", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_schedule_dock_appointments`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_schedule_dock_appointments_agent.py` and in the RCI capsule.

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

Schedule dock appointments Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of schedule dock appointments status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-schedule-dock-appointments
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_schedule_dock_appointments_agent.py` and embedded as the fenced Python below (sha256 feb48a9df779b1fd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_schedule_dock_appointments_agent.py` first:

```bash
python3 adaptive_card_schedule_dock_appointments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_schedule_dock_appointments_agent.py   # or on stdin
python3 adaptive_card_schedule_dock_appointments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Schedule dock appointments Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of schedule dock appointments status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-schedule-dock-appointments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_schedule_dock_appointments',
    "version": '2.0.0',
    "display_name": 'Schedule dock appointments Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of schedule dock appointments status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-schedule-dock-appointments',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-schedule-dock-appointments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f163541a291d7a4a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-freight-and-transportation/schedule-dock-appointments'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/adaptive-card-schedule-dock-appointments', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'word:schedule'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardScheduleDockAppointments(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardScheduleDockAppointments'
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
    print(AdaptiveCardScheduleDockAppointments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
