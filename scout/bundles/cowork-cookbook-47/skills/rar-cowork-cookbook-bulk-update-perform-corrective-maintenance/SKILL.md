---
name: "rar-cowork-cookbook-bulk-update-perform-corrective-maintenance"
description: "Applies a bulk field update across perform corrective maintenance records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_perform_corrective_maintenance", "rar_sha256": "3390c559cead385d344fed955958b92f9bae20a4468e6a4410da747333454273", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_perform_corrective_maintenance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-perform-corrective-maintenance:b9a9e5311f16049eac03a97fb389e18d5f4194eb7a1d5d08e7e318ff987b14d6", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_perform_corrective_maintenance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_perform_corrective_maintenance_agent.py` is
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

Perform corrective maintenance Bulk Field Update — Applies a bulk field update across perform corrective maintenance records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-perform-corrective-maintenance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_perform_corrective_maintenance_agent.py` and embedded as the fenced Python below (sha256 3390c559cead385d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_perform_corrective_maintenance_agent.py` first:

```bash
python3 bulk_update_perform_corrective_maintenance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_perform_corrective_maintenance_agent.py   # or on stdin
python3 bulk_update_perform_corrective_maintenance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Perform corrective maintenance Bulk Field Update — Applies a bulk field update across perform corrective maintenance records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-perform-corrective-maintenance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_perform_corrective_maintenance',
    "version": '2.0.0',
    "display_name": 'Perform corrective maintenance Bulk Field Update',
    "description": 'Applies a bulk field update across perform corrective maintenance records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-perform-corrective-maintenance',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-perform-corrective-maintenance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7bae3d7026cc0a1c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/perform-asset-maintenance/perform-corrective-maintenance'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/bulk-update-perform-corrective-maintenance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdatePerformCorrectiveMaintenance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdatePerformCorrectiveMaintenance'
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
    print(BulkUpdatePerformCorrectiveMaintenance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
