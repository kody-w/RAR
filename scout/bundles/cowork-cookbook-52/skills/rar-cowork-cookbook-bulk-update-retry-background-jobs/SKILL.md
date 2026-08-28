---
name: "rar-cowork-cookbook-bulk-update-retry-background-jobs"
description: "Applies a bulk field update across retry background jobs records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_retry_background_jobs", "rar_sha256": "762e5ae6f37a1c8cd16f30283f3d446d8612e55c494a46972ef4aaa56d04c297", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_retry_background_jobs`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_retry_background_jobs_agent.py` and in the RCI capsule.

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
