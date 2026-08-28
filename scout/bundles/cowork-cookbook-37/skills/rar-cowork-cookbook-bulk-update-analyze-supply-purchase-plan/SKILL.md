---
name: "rar-cowork-cookbook-bulk-update-analyze-supply-purchase-plan"
description: "Applies a bulk field update across analyze supply purchase plan records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_analyze_supply_purchase_plan", "rar_sha256": "f3e50a43e6a11ad3c93ec5f3b70c7d400b84f1f539b6515ca431f71d4a556dde", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_analyze_supply_purchase_plan_agent.py` and embedded as the fenced Python below (sha256 f3e50a43e6a11ad3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_analyze_supply_purchase_plan_agent.py` first:

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
    "version": '2.0.0',
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
