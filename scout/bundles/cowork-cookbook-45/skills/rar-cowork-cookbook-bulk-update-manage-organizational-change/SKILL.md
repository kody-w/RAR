---
name: "rar-cowork-cookbook-bulk-update-manage-organizational-change"
description: "Applies a bulk field update across manage organizational change records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_manage_organizational_change", "rar_sha256": "1b6167ada46eb807421bda8b0d7d434c838c1a9badc43366f98aee8bdcc4c880", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_manage_organizational_change_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-manage-organizational-change:8fb8f35c220dda96ba5229b17e17636233ecd8392605699f17c4a0f0e0db7791", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_manage_organizational_change`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_manage_organizational_change_agent.py` is
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

Manage organizational change Bulk Field Update — Applies a bulk field update across manage organizational change records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-manage-organizational-change
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_manage_organizational_change_agent.py` and embedded as the fenced Python below (sha256 1b6167ada46eb807…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_manage_organizational_change_agent.py` first:

```bash
python3 bulk_update_manage_organizational_change_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_manage_organizational_change_agent.py   # or on stdin
python3 bulk_update_manage_organizational_change_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage organizational change Bulk Field Update — Applies a bulk field update across manage organizational change records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-manage-organizational-change
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_manage_organizational_change',
    "version": '2.0.0',
    "display_name": 'Manage organizational change Bulk Field Update',
    "description": 'Applies a bulk field update across manage organizational change records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-manage-organizational-change',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-manage-organizational-change',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4b72ff409516ba61',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/manage-organizational-change'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-manage-organizational-change', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateManageOrganizationalChange(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateManageOrganizationalChange'
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
    print(BulkUpdateManageOrganizationalChange().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
