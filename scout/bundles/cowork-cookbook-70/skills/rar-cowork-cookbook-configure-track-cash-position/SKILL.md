---
name: "rar-cowork-cookbook-configure-track-cash-position"
description: "Applies a bulk configuration change to track cash position from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_track_cash_position", "rar_sha256": "eea54c5bdd4b2521ed722b7dbce69a40eea8b2bd0b8bfda2e3148bc67e8bd883", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_track_cash_position_agent.py` and embedded as the fenced Python below (sha256 eea54c5bdd4b2521…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_track_cash_position_agent.py` first:

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
    "version": '2.0.1',
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
