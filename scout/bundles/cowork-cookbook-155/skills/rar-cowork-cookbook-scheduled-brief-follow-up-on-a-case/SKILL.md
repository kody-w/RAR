---
name: "rar-cowork-cookbook-scheduled-brief-follow-up-on-a-case"
description: "Schedulable morning-brief email summarizing follow up on a case for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_follow_up_on_a_case", "rar_sha256": "b526fdcac20bb7dc0d8c9c9e78b90c6e12256ca85ccf1c651b731b6fa0d08b10", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_follow_up_on_a_case`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_follow_up_on_a_case_agent.py` and in the RCI capsule.

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
