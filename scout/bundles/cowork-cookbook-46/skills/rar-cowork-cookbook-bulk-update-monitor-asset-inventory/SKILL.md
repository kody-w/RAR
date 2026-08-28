---
name: "rar-cowork-cookbook-bulk-update-monitor-asset-inventory"
description: "Applies a bulk field update across monitor asset inventory records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_monitor_asset_inventory", "rar_sha256": "9589892e86148575ae33a71eac7a3aadafdf04e9972052f55a028393560684f8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
