---
name: "rar-cowork-cookbook-bulk-update-track-project-expenses"
description: "Applies a bulk field update across track project expenses records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_track_project_expenses", "rar_sha256": "597f82bf681579cea6412b34267b33c998d52b17582f17c91322c3b2ffa3d6bf", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
