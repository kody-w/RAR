---
name: "rar-cowork-cookbook-teams-update-record-life-events"
description: "Drafts a Teams channel post on record life events status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_record_life_events", "rar_sha256": "8fef4bcc170dc924abbab059d7999ed055b56534ff2113fce81ac136ecce9117", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_record_life_events`. The original RAPP
agent is preserved byte-for-byte in `teams_update_record_life_events_agent.py` and in the RCI capsule.

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
