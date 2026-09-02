---
name: "rar-cowork-cookbook-scheduled-brief-correct-data-synchronization-failures"
description: "Schedulable morning-brief email summarizing correct data synchronization failures for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_correct_data_synchronization_failures", "rar_sha256": "99ec13f23c908259facd6ce594c2165ebf113b77bcde52257fe529061b34ba32", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_correct_data_synchronization_failures_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-correct-data-synchronization-failures:d6b1bf5de52de57001e7979e449ceccf609e2b6efc535f92aa7873999de20b88", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_correct_data_synchronization_failures`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_correct_data_synchronization_failures_agent.py` is
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

Correct data synchronization failures Scheduled Email Brief — Schedulable morning-brief email summarizing correct data synchronization failures for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-correct-data-synchronization-failures
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_correct_data_synchronization_failures_agent.py` and embedded as the fenced Python below (sha256 99ec13f23c908259…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_correct_data_synchronization_failures_agent.py` first:

```bash
python3 scheduled_brief_correct_data_synchronization_failures_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_correct_data_synchronization_failures_agent.py   # or on stdin
python3 scheduled_brief_correct_data_synchronization_failures_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Correct data synchronization failures Scheduled Email Brief — Schedulable morning-brief email summarizing correct data synchronization failures for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-correct-data-synchronization-failures
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_correct_data_synchronization_failures',
    "version": '2.0.0',
    "display_name": 'Correct data synchronization failures Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing correct data synchronization failures for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-correct-data-synchronization-failures',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-correct-data-synchronization-failures',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '32a0e2b823e02a50',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-data/correct-data-synchronization-failures'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-correct-data-synchronization-failures', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefCorrectDataSynchronizationFailures(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefCorrectDataSynchronizationFailures'
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
    print(ScheduledBriefCorrectDataSynchronizationFailures().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
