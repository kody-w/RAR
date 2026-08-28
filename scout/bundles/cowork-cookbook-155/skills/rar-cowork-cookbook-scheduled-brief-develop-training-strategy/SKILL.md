---
name: "rar-cowork-cookbook-scheduled-brief-develop-training-strategy"
description: "Schedulable morning-brief email summarizing develop training strategy for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_develop_training_strategy", "rar_sha256": "ee5873f5f83e3714938937c0ddafd64bc0e63cdcbaa850dc92224688d226c6e7", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_develop_training_strategy_agent.py` and embedded as the fenced Python below (sha256 ee5873f5f83e3714…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_develop_training_strategy_agent.py` first:

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
    "version": '2.0.1',
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
