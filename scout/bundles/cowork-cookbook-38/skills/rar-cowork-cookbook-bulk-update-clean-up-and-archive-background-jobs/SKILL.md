---
name: "rar-cowork-cookbook-bulk-update-clean-up-and-archive-background-jobs"
description: "Applies a bulk field update across clean up and archive background jobs records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_clean_up_and_archive_background_jobs", "rar_sha256": "c097f4f69171ccf3eece15fe3b6da5681df1ea0bf5caa2180bd3052d20a51037", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_clean_up_and_archive_background_jobs`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_clean_up_and_archive_background_jobs_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_clean_up_and_archive_background_jobs_agent.py` and embedded as the fenced Python below (sha256 c097f4f69171ccf3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_clean_up_and_archive_background_jobs_agent.py` first:

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
    "version": '2.0.1',
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
