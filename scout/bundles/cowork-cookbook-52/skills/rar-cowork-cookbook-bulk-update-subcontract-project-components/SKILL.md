---
name: "rar-cowork-cookbook-bulk-update-subcontract-project-components"
description: "Applies a bulk field update across subcontract project components records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_subcontract_project_components", "rar_sha256": "0ad7588726377ac38745bdc6cad26f09a70ac5a09a62d637bb0b79bdcab2e0d8", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_subcontract_project_components`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_subcontract_project_components_agent.py` and in the RCI capsule.

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

Subcontract project components Bulk Field Update — Applies a bulk field update across subcontract project components records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-subcontract-project-components
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_subcontract_project_components_agent.py` and embedded as the fenced Python below (sha256 0ad7588726377ac3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_subcontract_project_components_agent.py` first:

```bash
python3 bulk_update_subcontract_project_components_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_subcontract_project_components_agent.py   # or on stdin
python3 bulk_update_subcontract_project_components_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Subcontract project components Bulk Field Update — Applies a bulk field update across subcontract project components records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-subcontract-project-components
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_subcontract_project_components',
    "version": '2.0.1',
    "display_name": 'Subcontract project components Bulk Field Update',
    "description": 'Applies a bulk field update across subcontract project components records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-subcontract-project-components',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-subcontract-project-components',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '81f03c673e512b65',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/subcontract-project-components'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/bulk-update-subcontract-project-components', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateSubcontractProjectComponents(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateSubcontractProjectComponents'
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
    print(BulkUpdateSubcontractProjectComponents().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
