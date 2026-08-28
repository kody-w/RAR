---
name: "rar-cowork-cookbook-configure-create-and-track-service-level-agreements"
description: "Applies a bulk configuration change to create and track service level agreements from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_create_and_track_service_level_agreements", "rar_sha256": "6402659726f1aea1cbb667487c5b62a60c896692d6265903d1c091ccf7dea90b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_create_and_track_service_level_agreements`. The original RAPP
agent is preserved byte-for-byte in `configure_create_and_track_service_level_agreements_agent.py` and in the RCI capsule.

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

Create and track service level agreements Configuration Bulk Setup — Applies a bulk configuration change to create and track service level agreements from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-create-and-track-service-level-agreements
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_create_and_track_service_level_agreements_agent.py` and embedded as the fenced Python below (sha256 6402659726f1aea1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_create_and_track_service_level_agreements_agent.py` first:

```bash
python3 configure_create_and_track_service_level_agreements_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_create_and_track_service_level_agreements_agent.py   # or on stdin
python3 configure_create_and_track_service_level_agreements_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create and track service level agreements Configuration Bulk Setup — Applies a bulk configuration change to create and track service level agreements from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-create-and-track-service-level-agreements
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_create_and_track_service_level_agreements',
    "version": '2.0.1',
    "display_name": 'Create and track service level agreements Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to create and track service level agreements from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-create-and-track-service-level-agreements',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-create-and-track-service-level-agreements',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'eceac0b0ead6f015',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/create-and-track-service-level-agreements'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/configure-create-and-track-service-level-agreements', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureCreateAndTrackServiceLevelAgreements(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureCreateAndTrackServiceLevelAgreements'
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
    print(ConfigureCreateAndTrackServiceLevelAgreements().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
