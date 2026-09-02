---
name: "rar-cowork-cookbook-bulk-update-subcontract-project-components"
description: "Applies a bulk field update across subcontract project components records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_subcontract_project_components", "rar_sha256": "13c1088eb6426bf1825780fc83fd895f040355e9276196af94cc376bf1fa2ce4", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_subcontract_project_components_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-subcontract-project-components:f3002f5e93acd0b222423a1b2b5d18b73d30d995323f3975630a2df51482d7d7", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_subcontract_project_components`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_subcontract_project_components_agent.py` is
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
