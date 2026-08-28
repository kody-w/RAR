---
name: "rar-cowork-cookbook-bulk-update-track-project-expenses"
description: "Applies a bulk field update across track project expenses records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_track_project_expenses", "rar_sha256": "4132ec0f179d1ccf555cbe8cad87f94dfe4817e0bf5482b7507966209091465e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_track_project_expenses`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_track_project_expenses_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_track_project_expenses_agent.py` and embedded as the fenced Python below (sha256 4132ec0f179d1ccf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_track_project_expenses_agent.py` first:

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
    "version": '2.0.1',
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
