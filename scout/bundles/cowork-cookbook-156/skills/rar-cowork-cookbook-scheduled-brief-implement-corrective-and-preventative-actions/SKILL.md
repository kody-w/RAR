---
name: "rar-cowork-cookbook-scheduled-brief-implement-corrective-and-preventative-actions"
description: "Schedulable morning-brief email summarizing implement corrective and preventative actions for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_implement_corrective_and_preventative_actions", "rar_sha256": "7e0c08b57fef58ca76c3c8f75bf706ab9bab67835dfe5abd48dcc00900d1f7e1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_implement_corrective_and_preventative_actions_agent.py` and embedded as the fenced Python below (sha256 7e0c08b57fef58ca…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_implement_corrective_and_preventative_actions_agent.py` first:

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
    "version": '2.0.0',
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
