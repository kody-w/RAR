---
name: "rar-cowork-cookbook-bulk-update-plan-events"
description: "Applies a bulk field update across plan events records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_plan_events", "rar_sha256": "bf84b4e364a611d1ad398c787eef149df988979db5b7d8831e3a59557058479e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_plan_events`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_plan_events_agent.py` and in the RCI capsule.

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

Plan events Bulk Field Update — Applies a bulk field update across plan events records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-plan-events
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_plan_events_agent.py` and embedded as the fenced Python below (sha256 bf84b4e364a611d1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_plan_events_agent.py` first:

```bash
python3 bulk_update_plan_events_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_plan_events_agent.py   # or on stdin
python3 bulk_update_plan_events_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan events Bulk Field Update — Applies a bulk field update across plan events records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-plan-events
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_plan_events',
    "version": '2.0.1',
    "display_name": 'Plan events Bulk Field Update',
    "description": 'Applies a bulk field update across plan events records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-plan-events',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-plan-events',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '68343183a7def23e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/plan-events'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/bulk-update-plan-events', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdatePlanEvents(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdatePlanEvents'
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
    print(BulkUpdatePlanEvents().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
