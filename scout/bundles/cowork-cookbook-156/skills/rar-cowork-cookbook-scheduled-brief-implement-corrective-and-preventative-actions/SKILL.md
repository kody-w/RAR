---
name: "rar-cowork-cookbook-scheduled-brief-implement-corrective-and-preventative-actions"
description: "Schedulable morning-brief email summarizing implement corrective and preventative actions for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_implement_corrective_and_preventative_actions", "rar_sha256": "7e0c08b57fef58ca76c3c8f75bf706ab9bab67835dfe5abd48dcc00900d1f7e1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_implement_corrective_and_preventative_actions_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-implement-corrective-and-preventative-actions:55f2b6c8fc54dde5c10942bf37e2da6b3b67851a4cc0e1bfcae493f158ac4cdc", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_implement_corrective_and_preventative_actions`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_implement_corrective_and_preventative_actions_agent.py` is
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
