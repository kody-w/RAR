---
name: "rar-cowork-cookbook-configure-track-cash-position"
description: "Applies a bulk configuration change to track cash position from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_track_cash_position", "rar_sha256": "ac00b968d6019016070d8e7c175cac94f7227916c2ae6d96338bd858eb88dea8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_track_cash_position_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-track-cash-position:3865150c542c9f28015c7cd3dc4262e1fe6bc50f535e4f71e886b8c76ae148da", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_track_cash_position`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_track_cash_position_agent.py` is
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

Track cash position Configuration Bulk Setup — Applies a bulk configuration change to track cash position from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-track-cash-position
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_track_cash_position_agent.py` and embedded as the fenced Python below (sha256 ac00b968d6019016…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_track_cash_position_agent.py` first:

```bash
python3 configure_track_cash_position_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_track_cash_position_agent.py   # or on stdin
python3 configure_track_cash_position_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track cash position Configuration Bulk Setup — Applies a bulk configuration change to track cash position from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-track-cash-position
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_track_cash_position',
    "version": '2.0.0',
    "display_name": 'Track cash position Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to track cash position from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-track-cash-position',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-track-cash-position',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f84be924d065a5fa',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-cash/track-cash-position'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/configure-track-cash-position', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureTrackCashPosition(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureTrackCashPosition'
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
    print(ConfigureTrackCashPosition().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
