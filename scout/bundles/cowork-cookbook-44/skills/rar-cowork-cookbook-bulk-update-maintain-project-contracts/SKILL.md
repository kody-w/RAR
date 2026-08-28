---
name: "rar-cowork-cookbook-bulk-update-maintain-project-contracts"
description: "Applies a bulk field update across maintain project contracts records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_maintain_project_contracts", "rar_sha256": "17c9f66abef2b41d8d5c2dde6877cefbc892893ca87410e0d4811a29c4ba7c48", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_maintain_project_contracts`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_maintain_project_contracts_agent.py` and in the RCI capsule.

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

Maintain project contracts Bulk Field Update — Applies a bulk field update across maintain project contracts records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-maintain-project-contracts
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_maintain_project_contracts_agent.py` and embedded as the fenced Python below (sha256 17c9f66abef2b41d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_maintain_project_contracts_agent.py` first:

```bash
python3 bulk_update_maintain_project_contracts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_maintain_project_contracts_agent.py   # or on stdin
python3 bulk_update_maintain_project_contracts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain project contracts Bulk Field Update — Applies a bulk field update across maintain project contracts records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-maintain-project-contracts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_maintain_project_contracts',
    "version": '2.0.1',
    "display_name": 'Maintain project contracts Bulk Field Update',
    "description": 'Applies a bulk field update across maintain project contracts records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-maintain-project-contracts',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-maintain-project-contracts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4cc915a7f6014a08',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-contracts/maintain-project-contracts'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/bulk-update-maintain-project-contracts', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateMaintainProjectContracts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateMaintainProjectContracts'
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
    print(BulkUpdateMaintainProjectContracts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
