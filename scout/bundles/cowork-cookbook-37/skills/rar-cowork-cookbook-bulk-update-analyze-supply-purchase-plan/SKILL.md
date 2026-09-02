---
name: "rar-cowork-cookbook-bulk-update-analyze-supply-purchase-plan"
description: "Applies a bulk field update across analyze supply purchase plan records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_analyze_supply_purchase_plan", "rar_sha256": "f3e50a43e6a11ad3c93ec5f3b70c7d400b84f1f539b6515ca431f71d4a556dde", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_analyze_supply_purchase_plan_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-analyze-supply-purchase-plan:3e1fe8631410248d77bc574f92d61ba93dd600d22d1a44efc8872b7ead6e65e4", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_analyze_supply_purchase_plan`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_analyze_supply_purchase_plan_agent.py` is
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
