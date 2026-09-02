---
name: "rar-cowork-cookbook-bulk-update-develop-training-materials"
description: "Applies a bulk field update across develop training materials records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_develop_training_materials", "rar_sha256": "5968bd7ab264a4fd77d42f10491540a59ece956471970e03a8a4b1dd9e74f3c9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_develop_training_materials_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-develop-training-materials:d6d21baa6d1716d89998dcad3080436e976db2d91e3cc7ea20f54a2568e28572", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_develop_training_materials`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_develop_training_materials_agent.py` is
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

Develop training materials Bulk Field Update — Applies a bulk field update across develop training materials records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-develop-training-materials
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_develop_training_materials_agent.py` and embedded as the fenced Python below (sha256 5968bd7ab264a4fd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_develop_training_materials_agent.py` first:

```bash
python3 bulk_update_develop_training_materials_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_develop_training_materials_agent.py   # or on stdin
python3 bulk_update_develop_training_materials_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop training materials Bulk Field Update — Applies a bulk field update across develop training materials records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-develop-training-materials
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_develop_training_materials',
    "version": '2.0.0',
    "display_name": 'Develop training materials Bulk Field Update',
    "description": 'Applies a bulk field update across develop training materials records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-develop-training-materials',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-develop-training-materials',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c91bc280681adef3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/train-users-and-increase-adoption/develop-training-materials'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-develop-training-materials', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateDevelopTrainingMaterials(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDevelopTrainingMaterials'
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
    print(BulkUpdateDevelopTrainingMaterials().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
