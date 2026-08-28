---
name: "rar-cowork-cookbook-bulk-update-consume-materials"
description: "Applies a bulk field update across consume materials records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_consume_materials", "rar_sha256": "ffb9d66bdd12a287f9600a5279bfe4645843a20649e11192a0a3e3d67387e551", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_consume_materials_agent.py` and embedded as the fenced Python below (sha256 ffb9d66bdd12a287…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_consume_materials_agent.py` first:

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
    "version": '2.0.1',
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
