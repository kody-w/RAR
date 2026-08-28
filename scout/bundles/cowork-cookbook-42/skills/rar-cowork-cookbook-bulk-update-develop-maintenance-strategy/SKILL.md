---
name: "rar-cowork-cookbook-bulk-update-develop-maintenance-strategy"
description: "Applies a bulk field update across develop maintenance strategy records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_develop_maintenance_strategy", "rar_sha256": "58b04c28b6d359f4bbe4bf4bfe977086e6878d376ec6261f6e31e08a35653eb2", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_develop_maintenance_strategy_agent.py` and embedded as the fenced Python below (sha256 58b04c28b6d359f4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_develop_maintenance_strategy_agent.py` first:

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
    "version": '2.0.0',
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
