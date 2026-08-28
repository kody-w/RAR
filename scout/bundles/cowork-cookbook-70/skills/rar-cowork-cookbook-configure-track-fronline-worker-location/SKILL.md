---
name: "rar-cowork-cookbook-configure-track-fronline-worker-location"
description: "Applies a bulk configuration change to track fronline worker location from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_track_fronline_worker_location", "rar_sha256": "45019dd80e39b19325e31339fa1f97f63ba341d1c76264a1b7ce8859269931db", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_track_fronline_worker_location`. The original RAPP
agent is preserved byte-for-byte in `configure_track_fronline_worker_location_agent.py` and in the RCI capsule.

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

Track fronline worker location Configuration Bulk Setup — Applies a bulk configuration change to track fronline worker location from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-track-fronline-worker-location
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_track_fronline_worker_location_agent.py` and embedded as the fenced Python below (sha256 45019dd80e39b193…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_track_fronline_worker_location_agent.py` first:

```bash
python3 configure_track_fronline_worker_location_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_track_fronline_worker_location_agent.py   # or on stdin
python3 configure_track_fronline_worker_location_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track fronline worker location Configuration Bulk Setup — Applies a bulk configuration change to track fronline worker location from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-track-fronline-worker-location
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_track_fronline_worker_location',
    "version": '2.0.1',
    "display_name": 'Track fronline worker location Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to track fronline worker location from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-track-fronline-worker-location',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-track-fronline-worker-location',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '898a8b80b30c6f10',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/track-fronline-worker-location'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/configure-track-fronline-worker-location', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureTrackFronlineWorkerLocation(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureTrackFronlineWorkerLocation'
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
    print(ConfigureTrackFronlineWorkerLocation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
