---
name: "rar-cowork-cookbook-bulk-update-clean-up-and-archive-background-jobs"
description: "Applies a bulk field update across clean up and archive background jobs records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_clean_up_and_archive_background_jobs", "rar_sha256": "4135f5b9d37ce291f71e0c99015cf937c17b1f795b4058ae47d8723851feeb72", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
