---
name: "rar-cowork-cookbook-bulk-update-promote-employees"
description: "Applies a bulk field update across promote employees records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_promote_employees", "rar_sha256": "32132bac31e527bd24a4491d9a2e4f7eab47666d20baf5cdfeb565f2602d8e3c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_promote_employees_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-promote-employees:17d93244f07135fa35b5e9fcdf4c0e6980cbc9c206283b38f68f6e13218b6541", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_promote_employees`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_promote_employees_agent.py` is
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

Promote employees Bulk Field Update — Applies a bulk field update across promote employees records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-promote-employees
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_promote_employees_agent.py` and embedded as the fenced Python below (sha256 32132bac31e527bd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_promote_employees_agent.py` first:

```bash
python3 bulk_update_promote_employees_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_promote_employees_agent.py   # or on stdin
python3 bulk_update_promote_employees_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Promote employees Bulk Field Update — Applies a bulk field update across promote employees records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-promote-employees
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_promote_employees',
    "version": '2.0.0',
    "display_name": 'Promote employees Bulk Field Update',
    "description": 'Applies a bulk field update across promote employees records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-promote-employees',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-promote-employees',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '328b39f8330ede27',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/promote-employees'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/bulk-update-promote-employees', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdatePromoteEmployees(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdatePromoteEmployees'
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
    print(BulkUpdatePromoteEmployees().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
