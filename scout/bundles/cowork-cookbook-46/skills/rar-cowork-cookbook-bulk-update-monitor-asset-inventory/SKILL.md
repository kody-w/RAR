---
name: "rar-cowork-cookbook-bulk-update-monitor-asset-inventory"
description: "Applies a bulk field update across monitor asset inventory records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_monitor_asset_inventory", "rar_sha256": "b58f342c8332bbf45a0697856366c51aefff1356f008925e28efdcebae91cf0f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_monitor_asset_inventory`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_monitor_asset_inventory_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_monitor_asset_inventory_agent.py` and embedded as the fenced Python below (sha256 b58f342c8332bbf4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_monitor_asset_inventory_agent.py` first:

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
    "version": '2.0.1',
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
