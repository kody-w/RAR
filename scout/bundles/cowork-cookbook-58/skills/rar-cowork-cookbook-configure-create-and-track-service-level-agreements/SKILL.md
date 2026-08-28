---
name: "rar-cowork-cookbook-configure-create-and-track-service-level-agreements"
description: "Applies a bulk configuration change to create and track service level agreements from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_create_and_track_service_level_agreements", "rar_sha256": "68deee7354572e81832ff42288e2d70954e23a9ea24d21b61cb13e55f96c1654", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_create_and_track_service_level_agreements_agent.py` and embedded as the fenced Python below (sha256 68deee7354572e81…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_create_and_track_service_level_agreements_agent.py` first:

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
    "version": '2.0.0',
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
