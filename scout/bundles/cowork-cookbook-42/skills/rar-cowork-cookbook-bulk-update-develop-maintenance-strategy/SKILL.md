---
name: "rar-cowork-cookbook-bulk-update-develop-maintenance-strategy"
description: "Applies a bulk field update across develop maintenance strategy records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_develop_maintenance_strategy", "rar_sha256": "27f0b63815b1d5a07ce7112ee6777fd7a88c2156af2f4f2036a586ebb626f419", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_develop_maintenance_strategy`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_develop_maintenance_strategy_agent.py` and in the RCI capsule.

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

Develop maintenance strategy Bulk Field Update — Applies a bulk field update across develop maintenance strategy records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-develop-maintenance-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_develop_maintenance_strategy_agent.py` and embedded as the fenced Python below (sha256 27f0b63815b1d5a0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_develop_maintenance_strategy_agent.py` first:

```bash
python3 bulk_update_develop_maintenance_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_develop_maintenance_strategy_agent.py   # or on stdin
python3 bulk_update_develop_maintenance_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop maintenance strategy Bulk Field Update — Applies a bulk field update across develop maintenance strategy records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-develop-maintenance-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_develop_maintenance_strategy',
    "version": '2.0.1',
    "display_name": 'Develop maintenance strategy Bulk Field Update',
    "description": 'Applies a bulk field update across develop maintenance strategy records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-develop-maintenance-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-develop-maintenance-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1e5d2193b8210d84',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/define-asset-strategy/develop-maintenance-strategy'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/bulk-update-develop-maintenance-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateDevelopMaintenanceStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDevelopMaintenanceStrategy'
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
    print(BulkUpdateDevelopMaintenanceStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
