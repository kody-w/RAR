---
name: "rar-cowork-cookbook-bulk-update-retry-background-jobs"
description: "Applies a bulk field update across retry background jobs records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_retry_background_jobs", "rar_sha256": "762e5ae6f37a1c8cd16f30283f3d446d8612e55c494a46972ef4aaa56d04c297", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_retry_background_jobs_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-retry-background-jobs:6c111d6d79e36c5d4ad6e30e9bbc39e534da112395e55e7bdc2f5d294592bf9b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_retry_background_jobs`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_retry_background_jobs_agent.py` is
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

Retry background jobs Bulk Field Update — Applies a bulk field update across retry background jobs records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-retry-background-jobs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_retry_background_jobs_agent.py` and embedded as the fenced Python below (sha256 762e5ae6f37a1c8c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_retry_background_jobs_agent.py` first:

```bash
python3 bulk_update_retry_background_jobs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_retry_background_jobs_agent.py   # or on stdin
python3 bulk_update_retry_background_jobs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Retry background jobs Bulk Field Update — Applies a bulk field update across retry background jobs records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-retry-background-jobs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_retry_background_jobs',
    "version": '2.0.0',
    "display_name": 'Retry background jobs Bulk Field Update',
    "description": 'Applies a bulk field update across retry background jobs records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-retry-background-jobs',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-retry-background-jobs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '33bbf94bd257bf26',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-background-jobs/retry-background-jobs'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-retry-background-jobs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateRetryBackgroundJobs(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateRetryBackgroundJobs'
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
    print(BulkUpdateRetryBackgroundJobs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
