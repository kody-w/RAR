---
name: "rar-cowork-cookbook-bulk-update-plan-events"
description: "Applies a bulk field update across plan events records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_plan_events", "rar_sha256": "a6b5be6fed856c1f8da50bbbdbdd7d409fa1e0a82fa79d3ab9336fa38d1f4ccf", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_plan_events_agent.py` and embedded as the fenced Python below (sha256 a6b5be6fed856c1f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_plan_events_agent.py` first:

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
    "version": '2.0.0',
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
