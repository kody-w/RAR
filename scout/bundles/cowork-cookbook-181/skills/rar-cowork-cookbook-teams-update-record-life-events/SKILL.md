---
name: "rar-cowork-cookbook-teams-update-record-life-events"
description: "Drafts a Teams channel post on record life events status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_record_life_events", "rar_sha256": "13c1874bc38e04e92678f997efb83e8b4bfc0b9a2d2143fbb124d778c3c1520d", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_record_life_events_agent.py` and embedded as the fenced Python below (sha256 13c1874bc38e04e9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_record_life_events_agent.py` first:

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
    "version": '2.0.1',
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
