---
name: "rar-cowork-cookbook-scheduled-brief-follow-up-on-a-case"
description: "Schedulable morning-brief email summarizing follow up on a case for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_follow_up_on_a_case", "rar_sha256": "d8271c5caea61dc394b3674f17c564565767b94949e5a619938193ffc89945f3", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_follow_up_on_a_case_agent.py` and embedded as the fenced Python below (sha256 d8271c5caea61dc3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_follow_up_on_a_case_agent.py` first:

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
    "version": '2.0.1',
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
