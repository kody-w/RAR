---
name: "rar-cowork-cookbook-scheduled-brief-implement-corrective-and-preventative-actions"
description: "Schedulable morning-brief email summarizing implement corrective and preventative actions for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_implement_corrective_and_preventative_actions", "rar_sha256": "9e8966e9b20c4c44bc186ff8394b1fc05f730cd425a884ef93ec08aaf4ecb43c", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_implement_corrective_and_preventative_actions`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_implement_corrective_and_preventative_actions_agent.py` and in the RCI capsule.

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

Implement corrective and preventative actions Scheduled Email Brief — Schedulable morning-brief email summarizing implement corrective and preventative actions for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-implement-corrective-and-preventative-actions
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_implement_corrective_and_preventative_actions_agent.py` and embedded as the fenced Python below (sha256 9e8966e9b20c4c44…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_implement_corrective_and_preventative_actions_agent.py` first:

```bash
python3 scheduled_brief_implement_corrective_and_preventative_actions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_implement_corrective_and_preventative_actions_agent.py   # or on stdin
python3 scheduled_brief_implement_corrective_and_preventative_actions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Implement corrective and preventative actions Scheduled Email Brief — Schedulable morning-brief email summarizing implement corrective and preventative actions for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-implement-corrective-and-preventative-actions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_implement_corrective_and_preventative_actions',
    "version": '2.0.1',
    "display_name": 'Implement corrective and preventative actions Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing implement corrective and preventative actions for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-implement-corrective-and-preventative-actions',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-implement-corrective-and-preventative-actions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '27407915f66210d2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/control-production-quality/implement-corrective-and-preventative-actions'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/scheduled-brief-implement-corrective-and-preventative-actions', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefImplementCorrectiveAndPreventativeActions(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefImplementCorrectiveAndPreventativeActions'
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
    print(ScheduledBriefImplementCorrectiveAndPreventativeActions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
