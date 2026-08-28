---
name: "rar-cowork-cookbook-scheduled-brief-run-events"
description: "Schedulable morning-brief email summarizing run events for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_run_events", "rar_sha256": "274849d91796d1815295a08fc6d6f8a7dc742f87aad42ae193261d69df1db18a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_run_events`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_run_events_agent.py` and in the RCI capsule.

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

Run events Scheduled Email Brief — Schedulable morning-brief email summarizing run events for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-run-events
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_run_events_agent.py` and embedded as the fenced Python below (sha256 274849d91796d181…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_run_events_agent.py` first:

```bash
python3 scheduled_brief_run_events_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_run_events_agent.py   # or on stdin
python3 scheduled_brief_run_events_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Run events Scheduled Email Brief — Schedulable morning-brief email summarizing run events for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-run-events
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_run_events',
    "version": '2.0.1',
    "display_name": 'Run events Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing run events for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-run-events',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-run-events',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6057ae5bf1066faa',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/manage-marketing-campaigns/run-events'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/scheduled-brief-run-events', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefRunEvents(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefRunEvents'
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
    print(ScheduledBriefRunEvents().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
