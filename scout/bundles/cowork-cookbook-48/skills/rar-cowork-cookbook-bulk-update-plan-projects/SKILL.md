---
name: "rar-cowork-cookbook-bulk-update-plan-projects"
description: "Applies a bulk field update across plan projects records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_plan_projects", "rar_sha256": "579f25df6bd32c6d33cf30114403f630a24f4210bee9dd9a6f10cce57c0907dc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_plan_projects_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-plan-projects:abaef33b1d856f1c31545dfb940b84a6f3c23243b771db24d34823c372976ffa", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_plan_projects`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_plan_projects_agent.py` is
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

Plan projects Bulk Field Update — Applies a bulk field update across plan projects records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-plan-projects
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_plan_projects_agent.py` and embedded as the fenced Python below (sha256 579f25df6bd32c6d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_plan_projects_agent.py` first:

```bash
python3 bulk_update_plan_projects_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_plan_projects_agent.py   # or on stdin
python3 bulk_update_plan_projects_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan projects Bulk Field Update — Applies a bulk field update across plan projects records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-plan-projects
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_plan_projects',
    "version": '2.0.0',
    "display_name": 'Plan projects Bulk Field Update',
    "description": 'Applies a bulk field update across plan projects records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-plan-projects',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-plan-projects',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '59e62c28bcacd571',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/execute-sales-and-operations/plan-projects'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/bulk-update-plan-projects', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdatePlanProjects(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdatePlanProjects'
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
    print(BulkUpdatePlanProjects().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
