---
name: "rar-cowork-cookbook-bulk-update-plan-operational-allocation-and-investments"
description: "Applies a bulk field update across plan operational allocation and investments records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_plan_operational_allocation_and_investments", "rar_sha256": "a7448c6633221c29d9f30084036dc6deeb5add40490ba311c094fb285c6949a1", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_plan_operational_allocation_and_investments`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_plan_operational_allocation_and_investments_agent.py` and in the RCI capsule.

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

Plan operational allocation and investments Bulk Field Update — Applies a bulk field update across plan operational allocation and investments records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-plan-operational-allocation-and-investments
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_plan_operational_allocation_and_investments_agent.py` and embedded as the fenced Python below (sha256 a7448c6633221c29…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_plan_operational_allocation_and_investments_agent.py` first:

```bash
python3 bulk_update_plan_operational_allocation_and_investments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_plan_operational_allocation_and_investments_agent.py   # or on stdin
python3 bulk_update_plan_operational_allocation_and_investments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan operational allocation and investments Bulk Field Update — Applies a bulk field update across plan operational allocation and investments records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-plan-operational-allocation-and-investments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_plan_operational_allocation_and_investments',
    "version": '2.0.1',
    "display_name": 'Plan operational allocation and investments Bulk Field Update',
    "description": 'Applies a bulk field update across plan operational allocation and investments records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-plan-operational-allocation-and-investments',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-plan-operational-allocation-and-investments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '73afc7572a9c9736',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-financial-planning/plan-operational-allocation-and-investments'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/bulk-update-plan-operational-allocation-and-investments', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.857, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdatePlanOperationalAllocationAndInvestments(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdatePlanOperationalAllocationAndInvestments'
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
    print(BulkUpdatePlanOperationalAllocationAndInvestments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
