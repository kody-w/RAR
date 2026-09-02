---
name: "rar-cowork-cookbook-bulk-update-reclaim-database-storage"
description: "Applies a bulk field update across reclaim database storage records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_reclaim_database_storage", "rar_sha256": "0e2ea83b985ba639ece899120f84858f2696267c1c49b8f6741663617a4aa3f6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_reclaim_database_storage_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-reclaim-database-storage:051ad10503d8d2d8f360cee6cc4de9f9420493b6eb64bfe66d7bfce95e7b5ff1", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_reclaim_database_storage`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_reclaim_database_storage_agent.py` is
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

Reclaim database storage Bulk Field Update — Applies a bulk field update across reclaim database storage records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-reclaim-database-storage
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_reclaim_database_storage_agent.py` and embedded as the fenced Python below (sha256 0e2ea83b985ba639…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_reclaim_database_storage_agent.py` first:

```bash
python3 bulk_update_reclaim_database_storage_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_reclaim_database_storage_agent.py   # or on stdin
python3 bulk_update_reclaim_database_storage_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Reclaim database storage Bulk Field Update — Applies a bulk field update across reclaim database storage records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-reclaim-database-storage
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_reclaim_database_storage',
    "version": '2.0.0',
    "display_name": 'Reclaim database storage Bulk Field Update',
    "description": 'Applies a bulk field update across reclaim database storage records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-reclaim-database-storage',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-reclaim-database-storage',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bcd110ed78bbc6c9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/monitor-systems-environments-and-capacity/reclaim-database-storage'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-reclaim-database-storage', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateReclaimDatabaseStorage(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateReclaimDatabaseStorage'
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
    print(BulkUpdateReclaimDatabaseStorage().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
