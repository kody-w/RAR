---
name: "rar-cowork-cookbook-bulk-update-develop-long-range-plan"
description: "Applies a bulk field update across develop long-range plan records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_develop_long_range_plan", "rar_sha256": "319a57c32d0fe174b4c98c3b8d9af95314c59419617613bf17ec8670e5efc1f2", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_develop_long_range_plan`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_develop_long_range_plan_agent.py` and in the RCI capsule.

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

Develop long-range plan Bulk Field Update — Applies a bulk field update across develop long-range plan records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-develop-long-range-plan
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_develop_long_range_plan_agent.py` and embedded as the fenced Python below (sha256 319a57c32d0fe174…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_develop_long_range_plan_agent.py` first:

```bash
python3 bulk_update_develop_long_range_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_develop_long_range_plan_agent.py   # or on stdin
python3 bulk_update_develop_long_range_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop long-range plan Bulk Field Update — Applies a bulk field update across develop long-range plan records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-develop-long-range-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_develop_long_range_plan',
    "version": '2.0.1',
    "display_name": 'Develop long-range plan Bulk Field Update',
    "description": 'Applies a bulk field update across develop long-range plan records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-develop-long-range-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-develop-long-range-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b7c50ab2520c2510',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/develop-long-range-plan'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/bulk-update-develop-long-range-plan', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateDevelopLongRangePlan(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDevelopLongRangePlan'
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
    print(BulkUpdateDevelopLongRangePlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
