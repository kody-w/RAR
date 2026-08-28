---
name: "rar-cowork-cookbook-bulk-update-develop-training-materials"
description: "Applies a bulk field update across develop training materials records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_develop_training_materials", "rar_sha256": "5968bd7ab264a4fd77d42f10491540a59ece956471970e03a8a4b1dd9e74f3c9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_develop_training_materials`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_develop_training_materials_agent.py` and in the RCI capsule.

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
