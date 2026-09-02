---
name: "rar-cowork-cookbook-bulk-update-track-fronline-worker-location"
description: "Applies a bulk field update across track fronline worker location records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_track_fronline_worker_location", "rar_sha256": "9580d0c895a1373184d2b1e9fe765783b5669a32d73f0566ba346f76b5407ece", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_track_fronline_worker_location_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-track-fronline-worker-location:f46d5d80ee020351ba649c9d4627bb70473f94f1ab4f6653b8ee38f87f5c9576", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_track_fronline_worker_location`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_track_fronline_worker_location_agent.py` is
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
