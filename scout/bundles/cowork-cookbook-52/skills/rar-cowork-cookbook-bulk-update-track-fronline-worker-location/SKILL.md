---
name: "rar-cowork-cookbook-bulk-update-track-fronline-worker-location"
description: "Applies a bulk field update across track fronline worker location records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_track_fronline_worker_location", "rar_sha256": "7aed0a947362f83c8c876959fa5e04bba8f363ad513585ab9982fae23b1db7e9", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_track_fronline_worker_location`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_track_fronline_worker_location_agent.py` and in the RCI capsule.

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

Track fronline worker location Bulk Field Update — Applies a bulk field update across track fronline worker location records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-track-fronline-worker-location
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_track_fronline_worker_location_agent.py` and embedded as the fenced Python below (sha256 7aed0a947362f83c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_track_fronline_worker_location_agent.py` first:

```bash
python3 bulk_update_track_fronline_worker_location_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_track_fronline_worker_location_agent.py   # or on stdin
python3 bulk_update_track_fronline_worker_location_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track fronline worker location Bulk Field Update — Applies a bulk field update across track fronline worker location records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-track-fronline-worker-location
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_track_fronline_worker_location',
    "version": '2.0.1',
    "display_name": 'Track fronline worker location Bulk Field Update',
    "description": 'Applies a bulk field update across track fronline worker location records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-track-fronline-worker-location',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-track-fronline-worker-location',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '29813f9ef3a26b81',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/track-fronline-worker-location'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/bulk-update-track-fronline-worker-location', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateTrackFronlineWorkerLocation(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateTrackFronlineWorkerLocation'
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
    print(BulkUpdateTrackFronlineWorkerLocation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
