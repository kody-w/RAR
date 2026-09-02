---
name: "rar-cowork-cookbook-adaptive-card-schedule-dock-appointments"
description: "Produces a reusable Adaptive Card JSON snapshot of schedule dock appointments status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_schedule_dock_appointments", "rar_sha256": "feb48a9df779b1fd71b814174f2164408a172eef1b9b5486f3faff3978562aca", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_schedule_dock_appointments_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-schedule-dock-appointments:35035c6daf8ff32423f02bd806d4e30e7f21144ebdb5cbe69253265305fb619c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_schedule_dock_appointments`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_schedule_dock_appointments_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
