---
name: "rar-cowork-cookbook-bulk-update-clean-up-and-archive-background-jobs"
description: "Applies a bulk field update across clean up and archive background jobs records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_clean_up_and_archive_background_jobs", "rar_sha256": "4135f5b9d37ce291f71e0c99015cf937c17b1f795b4058ae47d8723851feeb72", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_clean_up_and_archive_background_jobs_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-clean-up-and-archive-background-jobs:09cbdee930dd815e98e981314c5e8bc533292b9e28b92449672d0a97ecd8cc0d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_clean_up_and_archive_background_jobs`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_clean_up_and_archive_background_jobs_agent.py` is
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

Clean up and archive background jobs Bulk Field Update — Applies a bulk field update across clean up and archive background jobs records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-clean-up-and-archive-background-jobs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_clean_up_and_archive_background_jobs_agent.py` and embedded as the fenced Python below (sha256 4135f5b9d37ce291…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_clean_up_and_archive_background_jobs_agent.py` first:

```bash
python3 bulk_update_clean_up_and_archive_background_jobs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_clean_up_and_archive_background_jobs_agent.py   # or on stdin
python3 bulk_update_clean_up_and_archive_background_jobs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Clean up and archive background jobs Bulk Field Update — Applies a bulk field update across clean up and archive background jobs records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-clean-up-and-archive-background-jobs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_clean_up_and_archive_background_jobs',
    "version": '2.0.0',
    "display_name": 'Clean up and archive background jobs Bulk Field Update',
    "description": 'Applies a bulk field update across clean up and archive background jobs records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-clean-up-and-archive-background-jobs',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-clean-up-and-archive-background-jobs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '97306da88422fc8e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-background-jobs/clean-up-and-archive-background-jobs'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-clean-up-and-archive-background-jobs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateCleanUpAndArchiveBackgroundJobs(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateCleanUpAndArchiveBackgroundJobs'
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
    print(BulkUpdateCleanUpAndArchiveBackgroundJobs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
