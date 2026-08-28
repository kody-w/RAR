---
name: "rar-cowork-cookbook-configure-track-cash-position"
description: "Applies a bulk configuration change to track cash position from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_track_cash_position", "rar_sha256": "ac00b968d6019016070d8e7c175cac94f7227916c2ae6d96338bd858eb88dea8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_track_cash_position`. The original RAPP
agent is preserved byte-for-byte in `configure_track_cash_position_agent.py` and in the RCI capsule.

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
