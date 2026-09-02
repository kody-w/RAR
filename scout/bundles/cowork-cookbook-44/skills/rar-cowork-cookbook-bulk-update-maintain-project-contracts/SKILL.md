---
name: "rar-cowork-cookbook-bulk-update-maintain-project-contracts"
description: "Applies a bulk field update across maintain project contracts records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_maintain_project_contracts", "rar_sha256": "4cac072de579fb40584b567ac8059089442f92cdf11de91f4e14a0693c4a24df", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_maintain_project_contracts_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-maintain-project-contracts:acb91b932a1c645b232c15fbf6dc57965055faefceb4df8dcb6a4e9ffa07ac2b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_maintain_project_contracts`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_maintain_project_contracts_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_maintain_project_contracts_agent.py` and embedded as the fenced Python below (sha256 4cac072de579fb40…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_maintain_project_contracts_agent.py` first:

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
    "version": '2.0.0',
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
