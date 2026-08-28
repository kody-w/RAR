---
name: "rar-cowork-cookbook-bulk-update-modify-production-plan"
description: "Applies a bulk field update across modify production plan records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_modify_production_plan", "rar_sha256": "03edfa94ed654ec6253359d593b4612dfe51ab88d9083caaa800f20e8e4304f6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_modify_production_plan`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_modify_production_plan_agent.py` and in the RCI capsule.

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

Modify production plan Bulk Field Update — Applies a bulk field update across modify production plan records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-modify-production-plan
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_modify_production_plan_agent.py` and embedded as the fenced Python below (sha256 03edfa94ed654ec6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_modify_production_plan_agent.py` first:

```bash
python3 bulk_update_modify_production_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_modify_production_plan_agent.py   # or on stdin
python3 bulk_update_modify_production_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Modify production plan Bulk Field Update — Applies a bulk field update across modify production plan records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-modify-production-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_modify_production_plan',
    "version": '2.0.0',
    "display_name": 'Modify production plan Bulk Field Update',
    "description": 'Applies a bulk field update across modify production plan records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-modify-production-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-modify-production-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '943e16fabaa17b82',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/plan-production-operations/modify-production-plan'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/bulk-update-modify-production-plan', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateModifyProductionPlan(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateModifyProductionPlan'
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
    print(BulkUpdateModifyProductionPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
