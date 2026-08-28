---
name: "rar-cowork-cookbook-bulk-update-modify-production-plan"
description: "Applies a bulk field update across modify production plan records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_modify_production_plan", "rar_sha256": "f87d89a348fac6b415014798ce1302173d9ff067d8b581a00af2df0fe1fac34d", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_modify_production_plan_agent.py` and embedded as the fenced Python below (sha256 f87d89a348fac6b4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_modify_production_plan_agent.py` first:

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
    "version": '2.0.1',
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
