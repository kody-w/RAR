---
name: "rar-cowork-cookbook-configure-track-fronline-worker-location"
description: "Applies a bulk configuration change to track fronline worker location from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_track_fronline_worker_location", "rar_sha256": "d5829d8ae47c1dffcd389d8165735abb7c482f9a6fe8597790f900e21d7b7466", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_track_fronline_worker_location_agent.py` and embedded as the fenced Python below (sha256 d5829d8ae47c1dff…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_track_fronline_worker_location_agent.py` first:

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
    "version": '2.0.0',
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
