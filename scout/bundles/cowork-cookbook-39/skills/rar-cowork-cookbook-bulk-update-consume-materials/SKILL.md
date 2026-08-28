---
name: "rar-cowork-cookbook-bulk-update-consume-materials"
description: "Applies a bulk field update across consume materials records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_consume_materials", "rar_sha256": "bccd3a4230eb9d7662e3d36a6f2105f029a3b178e397306818ea1af9bff92b48", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_consume_materials`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_consume_materials_agent.py` and in the RCI capsule.

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

Consume materials Bulk Field Update — Applies a bulk field update across consume materials records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-consume-materials
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_consume_materials_agent.py` and embedded as the fenced Python below (sha256 bccd3a4230eb9d76…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_consume_materials_agent.py` first:

```bash
python3 bulk_update_consume_materials_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_consume_materials_agent.py   # or on stdin
python3 bulk_update_consume_materials_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Consume materials Bulk Field Update — Applies a bulk field update across consume materials records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-consume-materials
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_consume_materials',
    "version": '2.0.0',
    "display_name": 'Consume materials Bulk Field Update',
    "description": 'Applies a bulk field update across consume materials records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-consume-materials',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-consume-materials',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'dea1c9ce6d473274',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/run-production-operations/consume-materials'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/bulk-update-consume-materials', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateConsumeMaterials(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateConsumeMaterials'
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
    print(BulkUpdateConsumeMaterials().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
