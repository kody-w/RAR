---
name: "rar-cowork-cookbook-configure-track-fronline-worker-location"
description: "Applies a bulk configuration change to track fronline worker location from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_track_fronline_worker_location", "rar_sha256": "d5829d8ae47c1dffcd389d8165735abb7c482f9a6fe8597790f900e21d7b7466", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_track_fronline_worker_location_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-track-fronline-worker-location:d4810d4238c8792b8c9b60c501737f9fe43bb924aa315d2a1e4a9a3a01db3e76", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_track_fronline_worker_location`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_track_fronline_worker_location_agent.py` is
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
