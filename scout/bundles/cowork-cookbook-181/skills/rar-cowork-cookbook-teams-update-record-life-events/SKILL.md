---
name: "rar-cowork-cookbook-teams-update-record-life-events"
description: "Drafts a Teams channel post on record life events status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_record_life_events", "rar_sha256": "8fef4bcc170dc924abbab059d7999ed055b56534ff2113fce81ac136ecce9117", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_record_life_events_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-record-life-events:aedcf03a1af6d42d3b3e7ee005dae78e822cb39112ea24a1e317beabeaec98d5", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_record_life_events`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_record_life_events_agent.py` is
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

Record life events Teams Channel Update — Drafts a Teams channel post on record life events status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-record-life-events
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_record_life_events_agent.py` and embedded as the fenced Python below (sha256 8fef4bcc170dc924…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_record_life_events_agent.py` first:

```bash
python3 teams_update_record_life_events_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_record_life_events_agent.py   # or on stdin
python3 teams_update_record_life_events_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record life events Teams Channel Update — Drafts a Teams channel post on record life events status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-record-life-events
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_record_life_events',
    "version": '2.0.0',
    "display_name": 'Record life events Teams Channel Update',
    "description": 'Drafts a Teams channel post on record life events status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-record-life-events',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-record-life-events',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7e548e8ca788da89',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-compensation-and-benefits/record-life-events'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/teams-update-record-life-events', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateRecordLifeEvents(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateRecordLifeEvents'
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
    print(TeamsUpdateRecordLifeEvents().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
