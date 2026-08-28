---
name: "rar-cowork-cookbook-adaptive-card-schedule-dock-appointments"
description: "Produces a reusable Adaptive Card JSON snapshot of schedule dock appointments status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_schedule_dock_appointments", "rar_sha256": "2dc20e5f33744c26d1bb951eaa6d19148a2567939cf531b96a4ec5d3f095ecf2", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_schedule_dock_appointments_agent.py` and embedded as the fenced Python below (sha256 2dc20e5f33744c26…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_schedule_dock_appointments_agent.py` first:

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
    "version": '2.0.1',
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
