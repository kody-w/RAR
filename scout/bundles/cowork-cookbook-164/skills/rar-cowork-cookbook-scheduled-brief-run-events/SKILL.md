---
name: "rar-cowork-cookbook-scheduled-brief-run-events"
description: "Schedulable morning-brief email summarizing run events for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_run_events", "rar_sha256": "dee2ae556dc43deb42cd39935ef39f60de4f4b84d56d172d4aed426b1988da3b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_run_events_agent.py` and embedded as the fenced Python below (sha256 dee2ae556dc43deb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_run_events_agent.py` first:

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
    "version": '2.0.0',
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
