---
name: "rar-cowork-cookbook-bulk-update-plan-physical-capacity"
description: "Applies a bulk field update across plan physical capacity records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_plan_physical_capacity", "rar_sha256": "d1f65904af71cfa6c7f4dffe31788f463cd2405ae13f3e8aa7309d35d5edb567", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_plan_physical_capacity_agent.py` and embedded as the fenced Python below (sha256 d1f65904af71cfa6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_plan_physical_capacity_agent.py` first:

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
    "version": '2.0.0',
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
