---
name: "rar-cowork-cookbook-bulk-update-reclaim-database-storage"
description: "Applies a bulk field update across reclaim database storage records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_reclaim_database_storage", "rar_sha256": "0e2ea83b985ba639ece899120f84858f2696267c1c49b8f6741663617a4aa3f6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_reclaim_database_storage`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_reclaim_database_storage_agent.py` and in the RCI capsule.

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
