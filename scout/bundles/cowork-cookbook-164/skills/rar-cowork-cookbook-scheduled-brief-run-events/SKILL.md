---
name: "rar-cowork-cookbook-scheduled-brief-run-events"
description: "Schedulable morning-brief email summarizing run events for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_run_events", "rar_sha256": "dee2ae556dc43deb42cd39935ef39f60de4f4b84d56d172d4aed426b1988da3b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_run_events_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-run-events:37c02f21fbcd98c22ecbaaec64628c1049ff504e1086723e4ecd74470873ea8d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_run_events`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_run_events_agent.py` is
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
