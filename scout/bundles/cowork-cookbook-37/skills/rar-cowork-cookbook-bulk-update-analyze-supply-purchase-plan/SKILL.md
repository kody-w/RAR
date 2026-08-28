---
name: "rar-cowork-cookbook-bulk-update-analyze-supply-purchase-plan"
description: "Applies a bulk field update across analyze supply purchase plan records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_analyze_supply_purchase_plan", "rar_sha256": "04b29453731fada24d301b9376ed3c64afe3950c47936c83af42dd78e9f124cf", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_analyze_supply_purchase_plan`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_analyze_supply_purchase_plan_agent.py` and in the RCI capsule.

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

Analyze supply purchase plan Bulk Field Update — Applies a bulk field update across analyze supply purchase plan records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-analyze-supply-purchase-plan
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_analyze_supply_purchase_plan_agent.py` and embedded as the fenced Python below (sha256 04b29453731fada2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_analyze_supply_purchase_plan_agent.py` first:

```bash
python3 bulk_update_analyze_supply_purchase_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_analyze_supply_purchase_plan_agent.py   # or on stdin
python3 bulk_update_analyze_supply_purchase_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze supply purchase plan Bulk Field Update — Applies a bulk field update across analyze supply purchase plan records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-analyze-supply-purchase-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_analyze_supply_purchase_plan',
    "version": '2.0.1',
    "display_name": 'Analyze supply purchase plan Bulk Field Update',
    "description": 'Applies a bulk field update across analyze supply purchase plan records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-analyze-supply-purchase-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-analyze-supply-purchase-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0a028720deb0dec4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/procure-goods-and-services/analyze-supply-purchase-plan'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/bulk-update-analyze-supply-purchase-plan', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.75, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateAnalyzeSupplyPurchasePlan(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateAnalyzeSupplyPurchasePlan'
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
    print(BulkUpdateAnalyzeSupplyPurchasePlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
