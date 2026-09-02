---
name: "rar-cowork-cookbook-bulk-update-manage-loyalty-programs"
description: "Applies a bulk field update across manage loyalty programs records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_manage_loyalty_programs", "rar_sha256": "a26d10f0895633c69c1b34e46bdf637b89ed42537411529b5534efa7d3e7a079", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_manage_loyalty_programs_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-manage-loyalty-programs:5984b89d0f9417967cd01f164f7158171ced4c0237441c482e700d46c9bcdf27", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_manage_loyalty_programs`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_manage_loyalty_programs_agent.py` is
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

Manage loyalty programs Bulk Field Update — Applies a bulk field update across manage loyalty programs records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-manage-loyalty-programs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_manage_loyalty_programs_agent.py` and embedded as the fenced Python below (sha256 a26d10f0895633c6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_manage_loyalty_programs_agent.py` first:

```bash
python3 bulk_update_manage_loyalty_programs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_manage_loyalty_programs_agent.py   # or on stdin
python3 bulk_update_manage_loyalty_programs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage loyalty programs Bulk Field Update — Applies a bulk field update across manage loyalty programs records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-manage-loyalty-programs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_manage_loyalty_programs',
    "version": '2.0.0',
    "display_name": 'Manage loyalty programs Bulk Field Update',
    "description": 'Applies a bulk field update across manage loyalty programs records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-manage-loyalty-programs',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-manage-loyalty-programs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd89a9d0f3e987374',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/manage-customer-relationships/manage-loyalty-programs'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/bulk-update-manage-loyalty-programs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateManageLoyaltyPrograms(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateManageLoyaltyPrograms'
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
    print(BulkUpdateManageLoyaltyPrograms().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
