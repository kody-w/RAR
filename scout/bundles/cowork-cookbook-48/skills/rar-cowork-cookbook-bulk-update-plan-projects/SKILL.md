---
name: "rar-cowork-cookbook-bulk-update-plan-projects"
description: "Applies a bulk field update across plan projects records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_plan_projects", "rar_sha256": "04c2a218379a66a1f811bdafa15d9044e722d70870206679ec35d1dacd6990f5", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_plan_projects_agent.py` and embedded as the fenced Python below (sha256 04c2a218379a66a1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_plan_projects_agent.py` first:

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
    "version": '2.0.1',
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
