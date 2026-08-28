---
name: "rar-cowork-cookbook-bulk-update-develop-training-materials"
description: "Applies a bulk field update across develop training materials records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_develop_training_materials", "rar_sha256": "f85c23ed7e971224cf30f094b2e6f9f7f316144c164a2dcbcf4e76b9d0ed8acf", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_develop_training_materials_agent.py` and embedded as the fenced Python below (sha256 f85c23ed7e971224…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_develop_training_materials_agent.py` first:

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
    "version": '2.0.1',
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
