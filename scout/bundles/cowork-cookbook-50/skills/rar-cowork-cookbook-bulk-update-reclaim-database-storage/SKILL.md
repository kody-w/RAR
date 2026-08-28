---
name: "rar-cowork-cookbook-bulk-update-reclaim-database-storage"
description: "Applies a bulk field update across reclaim database storage records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_reclaim_database_storage", "rar_sha256": "6911e7fa66385d52f158067d7f94433ee19bf0ed1ecfaa4f7a3ba3f449ad4299", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_reclaim_database_storage_agent.py` and embedded as the fenced Python below (sha256 6911e7fa66385d52…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_reclaim_database_storage_agent.py` first:

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
    "version": '2.0.1',
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
