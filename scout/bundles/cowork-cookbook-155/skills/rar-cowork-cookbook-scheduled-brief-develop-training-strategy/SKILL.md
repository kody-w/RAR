---
name: "rar-cowork-cookbook-scheduled-brief-develop-training-strategy"
description: "Schedulable morning-brief email summarizing develop training strategy for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_develop_training_strategy", "rar_sha256": "7c0cbddd9e31d802783a2dc44d389158130b94d6636df12d0f5c3df955903b99", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_develop_training_strategy`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_develop_training_strategy_agent.py` and in the RCI capsule.

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
