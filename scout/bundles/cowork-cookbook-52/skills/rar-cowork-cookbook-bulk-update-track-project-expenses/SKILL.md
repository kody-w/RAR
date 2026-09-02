---
name: "rar-cowork-cookbook-bulk-update-track-project-expenses"
description: "Applies a bulk field update across track project expenses records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_track_project_expenses", "rar_sha256": "597f82bf681579cea6412b34267b33c998d52b17582f17c91322c3b2ffa3d6bf", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_track_project_expenses_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-track-project-expenses:11faa32551a96b1d77b376a48320a5b29b4111b62d421f307b4dd843cf3385a1", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_track_project_expenses`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_track_project_expenses_agent.py` is
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

Track project expenses Bulk Field Update — Applies a bulk field update across track project expenses records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-track-project-expenses
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_track_project_expenses_agent.py` and embedded as the fenced Python below (sha256 597f82bf681579ce…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_track_project_expenses_agent.py` first:

```bash
python3 bulk_update_track_project_expenses_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_track_project_expenses_agent.py   # or on stdin
python3 bulk_update_track_project_expenses_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track project expenses Bulk Field Update — Applies a bulk field update across track project expenses records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-track-project-expenses
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_track_project_expenses',
    "version": '2.0.0',
    "display_name": 'Track project expenses Bulk Field Update',
    "description": 'Applies a bulk field update across track project expenses records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-track-project-expenses',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-track-project-expenses',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a96d4babece87398',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/track-project-expenses'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/bulk-update-track-project-expenses', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateTrackProjectExpenses(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateTrackProjectExpenses'
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
    print(BulkUpdateTrackProjectExpenses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
