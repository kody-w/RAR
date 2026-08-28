---
name: "rar-cowork-cookbook-bulk-update-develop-long-range-plan"
description: "Applies a bulk field update across develop long-range plan records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_develop_long_range_plan", "rar_sha256": "00a74311d0e9b5a56359e0dead4d861896a864e9c00691dafc10e910b63fcb32", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_develop_long_range_plan_agent.py` and embedded as the fenced Python below (sha256 00a74311d0e9b5a5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_develop_long_range_plan_agent.py` first:

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
    "version": '2.0.0',
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
