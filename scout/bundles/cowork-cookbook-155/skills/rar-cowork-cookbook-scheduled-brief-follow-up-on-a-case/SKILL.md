---
name: "rar-cowork-cookbook-scheduled-brief-follow-up-on-a-case"
description: "Schedulable morning-brief email summarizing follow up on a case for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_follow_up_on_a_case", "rar_sha256": "b526fdcac20bb7dc0d8c9c9e78b90c6e12256ca85ccf1c651b731b6fa0d08b10", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_follow_up_on_a_case_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-follow-up-on-a-case:3881b24d9b105a263c7e08adb72fbe2ae844efde4d3bf268cad9b9ecd8b4b12f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_follow_up_on_a_case`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_follow_up_on_a_case_agent.py` is
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

Follow up on a case Scheduled Email Brief — Schedulable morning-brief email summarizing follow up on a case for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-follow-up-on-a-case
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_follow_up_on_a_case_agent.py` and embedded as the fenced Python below (sha256 b526fdcac20bb7dc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_follow_up_on_a_case_agent.py` first:

```bash
python3 scheduled_brief_follow_up_on_a_case_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_follow_up_on_a_case_agent.py   # or on stdin
python3 scheduled_brief_follow_up_on_a_case_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Follow up on a case Scheduled Email Brief — Schedulable morning-brief email summarizing follow up on a case for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-follow-up-on-a-case
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_follow_up_on_a_case',
    "version": '2.0.0',
    "display_name": 'Follow up on a case Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing follow up on a case for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-follow-up-on-a-case',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-follow-up-on-a-case',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '385a17859f3dde56',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/follow-up-on-a-case'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/scheduled-brief-follow-up-on-a-case', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefFollowUpOnACase(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefFollowUpOnACase'
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
    print(ScheduledBriefFollowUpOnACase().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
