---
name: "rar-cowork-cookbook-bulk-update-retry-background-jobs"
description: "Applies a bulk field update across retry background jobs records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_retry_background_jobs", "rar_sha256": "9334a021f5c50566cf03159dfa30db4736b2dd9978c6efa6d5986713a551e845", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_retry_background_jobs_agent.py` and embedded as the fenced Python below (sha256 9334a021f5c50566…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_retry_background_jobs_agent.py` first:

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
    "version": '2.0.1',
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
