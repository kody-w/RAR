---
name: "rar-cowork-cookbook-bulk-update-plan-loads"
description: "Applies a bulk field update across plan loads records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_plan_loads", "rar_sha256": "61435400b8c31cafe7b2c724742e32e3c3bad13d0fc57ccc2675ec1379c46a0c", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_plan_loads`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_plan_loads_agent.py` and in the RCI capsule.

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

Plan loads Bulk Field Update — Applies a bulk field update across plan loads records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-plan-loads
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_plan_loads_agent.py` and embedded as the fenced Python below (sha256 61435400b8c31caf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_plan_loads_agent.py` first:

```bash
python3 bulk_update_plan_loads_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_plan_loads_agent.py   # or on stdin
python3 bulk_update_plan_loads_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan loads Bulk Field Update — Applies a bulk field update across plan loads records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-plan-loads
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_plan_loads',
    "version": '2.0.1',
    "display_name": 'Plan loads Bulk Field Update',
    "description": 'Applies a bulk field update across plan loads records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-plan-loads',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-plan-loads',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c52fc0dfeaab27da',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-freight-and-transportation/plan-loads'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/bulk-update-plan-loads', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdatePlanLoads(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdatePlanLoads'
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
    print(BulkUpdatePlanLoads().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
