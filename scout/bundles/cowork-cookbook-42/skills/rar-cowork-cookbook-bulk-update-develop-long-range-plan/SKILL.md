---
name: "rar-cowork-cookbook-bulk-update-develop-long-range-plan"
description: "Applies a bulk field update across develop long-range plan records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_develop_long_range_plan", "rar_sha256": "00a74311d0e9b5a56359e0dead4d861896a864e9c00691dafc10e910b63fcb32", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_develop_long_range_plan_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-develop-long-range-plan:58a560183df7318e59ed7e0bc0fdda3d9200c4986e7966252c760a13448caf94", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_develop_long_range_plan`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_develop_long_range_plan_agent.py` is
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
