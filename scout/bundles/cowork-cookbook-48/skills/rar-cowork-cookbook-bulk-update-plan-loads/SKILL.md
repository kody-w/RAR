---
name: "rar-cowork-cookbook-bulk-update-plan-loads"
description: "Applies a bulk field update across plan loads records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_plan_loads", "rar_sha256": "cab322941a7308494e94717f00f6c55a0f65f79c877c5734152b49aeff2bd0d9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_plan_loads_agent.py` and embedded as the fenced Python below (sha256 cab322941a730849…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_plan_loads_agent.py` first:

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
    "version": '2.0.0',
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
