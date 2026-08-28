---
name: "rar-cowork-cookbook-bulk-update-plan-projects"
description: "Applies a bulk field update across plan projects records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_plan_projects", "rar_sha256": "579f25df6bd32c6d33cf30114403f630a24f4210bee9dd9a6f10cce57c0907dc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_plan_projects`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_plan_projects_agent.py` and in the RCI capsule.

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
