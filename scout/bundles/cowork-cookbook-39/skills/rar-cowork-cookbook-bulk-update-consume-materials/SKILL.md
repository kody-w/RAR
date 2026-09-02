---
name: "rar-cowork-cookbook-bulk-update-consume-materials"
description: "Applies a bulk field update across consume materials records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_consume_materials", "rar_sha256": "bccd3a4230eb9d7662e3d36a6f2105f029a3b178e397306818ea1af9bff92b48", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_consume_materials_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-consume-materials:2babf9be7382624bb85f0840b1b00985b2ad9180c889bac9b7b3a55c12dee585", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_consume_materials`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_consume_materials_agent.py` is
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
