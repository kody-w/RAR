---
name: "rar-cowork-cookbook-bulk-update-purchase-assets"
description: "Applies a bulk field update across purchase assets records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_purchase_assets", "rar_sha256": "720eb2d79767e39bb9af823a5e1793b20ae7250a167feaf6215fe8efc03f5423", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_purchase_assets`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_purchase_assets_agent.py` and in the RCI capsule.

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

Purchase assets Bulk Field Update — Applies a bulk field update across purchase assets records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-purchase-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_purchase_assets_agent.py` and embedded as the fenced Python below (sha256 720eb2d79767e39b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_purchase_assets_agent.py` first:

```bash
python3 bulk_update_purchase_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_purchase_assets_agent.py   # or on stdin
python3 bulk_update_purchase_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Purchase assets Bulk Field Update — Applies a bulk field update across purchase assets records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-purchase-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_purchase_assets',
    "version": '2.0.1',
    "display_name": 'Purchase assets Bulk Field Update',
    "description": 'Applies a bulk field update across purchase assets records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-purchase-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-purchase-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'dc6286a232c60202',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/purchase-assets'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/bulk-update-purchase-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdatePurchaseAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdatePurchaseAssets'
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
    print(BulkUpdatePurchaseAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
