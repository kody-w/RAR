---
name: "rar-cowork-cookbook-bulk-update-monitor-asset-inventory"
description: "Applies a bulk field update across monitor asset inventory records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_monitor_asset_inventory", "rar_sha256": "9589892e86148575ae33a71eac7a3aadafdf04e9972052f55a028393560684f8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_monitor_asset_inventory_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-monitor-asset-inventory:a1364fdc2924f8ea168cdbc9a0e0db0697d5814db0129f1a97dd25756214b156", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_monitor_asset_inventory`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_monitor_asset_inventory_agent.py` is
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

Monitor asset inventory Bulk Field Update — Applies a bulk field update across monitor asset inventory records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-monitor-asset-inventory
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_monitor_asset_inventory_agent.py` and embedded as the fenced Python below (sha256 9589892e86148575…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_monitor_asset_inventory_agent.py` first:

```bash
python3 bulk_update_monitor_asset_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_monitor_asset_inventory_agent.py   # or on stdin
python3 bulk_update_monitor_asset_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor asset inventory Bulk Field Update — Applies a bulk field update across monitor asset inventory records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-monitor-asset-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_monitor_asset_inventory',
    "version": '2.0.0',
    "display_name": 'Monitor asset inventory Bulk Field Update',
    "description": 'Applies a bulk field update across monitor asset inventory records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-monitor-asset-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-monitor-asset-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cb5af628ae9f347e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/analyze-assets/monitor-asset-inventory'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/bulk-update-monitor-asset-inventory', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateMonitorAssetInventory(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateMonitorAssetInventory'
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
    print(BulkUpdateMonitorAssetInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
