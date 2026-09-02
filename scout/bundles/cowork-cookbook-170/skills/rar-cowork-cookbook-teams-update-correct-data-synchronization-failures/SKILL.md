---
name: "rar-cowork-cookbook-teams-update-correct-data-synchronization-failures"
description: "Drafts a Teams channel post on correct data synchronization failures status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_correct_data_synchronization_failures", "rar_sha256": "59578c4e397988f81e3b60acc95b2d9d9efc0516ca6df03df8b5323decb95e35", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_correct_data_synchronization_failures_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-correct-data-synchronization-failures:d3a64ab05838e5a3544999c4d4fb71f203b7a3a980339178506a0b9230b75f1a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_correct_data_synchronization_failures`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_correct_data_synchronization_failures_agent.py` is
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

Correct data synchronization failures Teams Channel Update — Drafts a Teams channel post on correct data synchronization failures status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-correct-data-synchronization-failures
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_correct_data_synchronization_failures_agent.py` and embedded as the fenced Python below (sha256 59578c4e397988f8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_correct_data_synchronization_failures_agent.py` first:

```bash
python3 teams_update_correct_data_synchronization_failures_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_correct_data_synchronization_failures_agent.py   # or on stdin
python3 teams_update_correct_data_synchronization_failures_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Correct data synchronization failures Teams Channel Update — Drafts a Teams channel post on correct data synchronization failures status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-correct-data-synchronization-failures
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_correct_data_synchronization_failures',
    "version": '2.0.0',
    "display_name": 'Correct data synchronization failures Teams Channel Update',
    "description": 'Drafts a Teams channel post on correct data synchronization failures status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-correct-data-synchronization-failures',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-correct-data-synchronization-failures',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '36a44957bc2a06e4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-data/correct-data-synchronization-failures'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-correct-data-synchronization-failures', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateCorrectDataSynchronizationFailures(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateCorrectDataSynchronizationFailures'
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
    print(TeamsUpdateCorrectDataSynchronizationFailures().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
