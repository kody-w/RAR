---
name: "rar-cowork-cookbook-bulk-update-subcontract-project-components"
description: "Applies a bulk field update across subcontract project components records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_subcontract_project_components", "rar_sha256": "13c1088eb6426bf1825780fc83fd895f040355e9276196af94cc376bf1fa2ce4", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_subcontract_project_components_agent.py` and embedded as the fenced Python below (sha256 13c1088eb6426bf1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_subcontract_project_components_agent.py` first:

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
    "version": '2.0.0',
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
