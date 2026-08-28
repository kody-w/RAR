---
name: "rar-cowork-cookbook-bulk-update-maintain-project-contracts"
description: "Applies a bulk field update across maintain project contracts records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_maintain_project_contracts", "rar_sha256": "4cac072de579fb40584b567ac8059089442f92cdf11de91f4e14a0693c4a24df", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
