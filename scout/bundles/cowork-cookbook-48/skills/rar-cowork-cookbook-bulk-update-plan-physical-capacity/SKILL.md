---
name: "rar-cowork-cookbook-bulk-update-plan-physical-capacity"
description: "Applies a bulk field update across plan physical capacity records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_plan_physical_capacity", "rar_sha256": "ca4580a727a7297e7de98f53fde4f701740019671fe370a94ad57492514dda33", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_plan_physical_capacity`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_plan_physical_capacity_agent.py` and in the RCI capsule.

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

Plan physical capacity Bulk Field Update — Applies a bulk field update across plan physical capacity records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-plan-physical-capacity
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_plan_physical_capacity_agent.py` and embedded as the fenced Python below (sha256 ca4580a727a7297e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_plan_physical_capacity_agent.py` first:

```bash
python3 bulk_update_plan_physical_capacity_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_plan_physical_capacity_agent.py   # or on stdin
python3 bulk_update_plan_physical_capacity_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan physical capacity Bulk Field Update — Applies a bulk field update across plan physical capacity records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-plan-physical-capacity
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_plan_physical_capacity',
    "version": '2.0.1',
    "display_name": 'Plan physical capacity Bulk Field Update',
    "description": 'Applies a bulk field update across plan physical capacity records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-plan-physical-capacity',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-plan-physical-capacity',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '97deb7c63cb33b8f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-sales-and-operations-planning/plan-physical-capacity'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/bulk-update-plan-physical-capacity', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdatePlanPhysicalCapacity(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdatePlanPhysicalCapacity'
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
    print(BulkUpdatePlanPhysicalCapacity().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
