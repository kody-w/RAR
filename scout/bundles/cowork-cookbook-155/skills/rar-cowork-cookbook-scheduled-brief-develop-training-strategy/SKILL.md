---
name: "rar-cowork-cookbook-scheduled-brief-develop-training-strategy"
description: "Schedulable morning-brief email summarizing develop training strategy for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_develop_training_strategy", "rar_sha256": "7c0cbddd9e31d802783a2dc44d389158130b94d6636df12d0f5c3df955903b99", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_develop_training_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-develop-training-strategy:79c61013bf56f7db60dff04831e8fda56ea4456b9cf110761dea603f3892d072", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_develop_training_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_develop_training_strategy_agent.py` is
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

Develop training strategy Scheduled Email Brief — Schedulable morning-brief email summarizing develop training strategy for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-develop-training-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_develop_training_strategy_agent.py` and embedded as the fenced Python below (sha256 7c0cbddd9e31d802…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_develop_training_strategy_agent.py` first:

```bash
python3 scheduled_brief_develop_training_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_develop_training_strategy_agent.py   # or on stdin
python3 scheduled_brief_develop_training_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop training strategy Scheduled Email Brief — Schedulable morning-brief email summarizing develop training strategy for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-develop-training-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_develop_training_strategy',
    "version": '2.0.0',
    "display_name": 'Develop training strategy Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing develop training strategy for the responsible owner; designed to run daily or weekly.',
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
        "upstream_slug": 'scheduled-brief-develop-training-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-develop-training-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5ee90fa9b124bea0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/train-users-and-increase-adoption/develop-training-strategy'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-develop-training-strategy', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefDevelopTrainingStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDevelopTrainingStrategy'
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
    print(ScheduledBriefDevelopTrainingStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
