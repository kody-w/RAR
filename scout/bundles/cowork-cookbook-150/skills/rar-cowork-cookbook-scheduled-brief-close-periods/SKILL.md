---
name: "rar-cowork-cookbook-scheduled-brief-close-periods"
description: "Schedulable morning-brief email summarizing close periods for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_close_periods", "rar_sha256": "0f47571211505e7435e9deb08032e481ec16ada774ad2730011c1de92d332e99", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_close_periods_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-close-periods:343841474e08f26eb29ce22220964ccddf89322876a8e29d9d1ca0262855c19f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_close_periods`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_close_periods_agent.py` is
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

Close periods Scheduled Email Brief — Schedulable morning-brief email summarizing close periods for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-close-periods
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_close_periods_agent.py` and embedded as the fenced Python below (sha256 0f47571211505e74…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_close_periods_agent.py` first:

```bash
python3 scheduled_brief_close_periods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_close_periods_agent.py   # or on stdin
python3 scheduled_brief_close_periods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Close periods Scheduled Email Brief — Schedulable morning-brief email summarizing close periods for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-close-periods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_close_periods',
    "version": '2.0.0',
    "display_name": 'Close periods Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing close periods for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'scheduled-brief-close-periods',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-close-periods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '22b7e87e25f2aab8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/close-financial-periods/close-periods'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/scheduled-brief-close-periods', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class ScheduledBriefClosePeriods(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefClosePeriods'
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
    print(ScheduledBriefClosePeriods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
