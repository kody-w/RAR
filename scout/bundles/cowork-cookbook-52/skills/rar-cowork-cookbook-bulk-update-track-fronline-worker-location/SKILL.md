---
name: "rar-cowork-cookbook-bulk-update-track-fronline-worker-location"
description: "Applies a bulk field update across track fronline worker location records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_track_fronline_worker_location", "rar_sha256": "9580d0c895a1373184d2b1e9fe765783b5669a32d73f0566ba346f76b5407ece", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_track_fronline_worker_location_agent.py` and embedded as the fenced Python below (sha256 9580d0c895a13731…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_track_fronline_worker_location_agent.py` first:

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
    "version": '2.0.0',
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
