---
name: "rar-cowork-cookbook-demo-data-develop-communication-strategy"
description: "Generates and creates realistic demo records for develop communication strategy in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_communication_strategy", "rar_sha256": "e5991292073059183eec3405987ff2f3dbf11f7b693335b8be04ea7328196e13", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_develop_communication_strategy`. The original RAPP
agent is preserved byte-for-byte in `demo_data_develop_communication_strategy_agent.py` and in the RCI capsule.

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

Develop communication strategy Demo Data Generator — Generates and creates realistic demo records for develop communication strategy in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-communication-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_develop_communication_strategy_agent.py` and embedded as the fenced Python below (sha256 e599129207305918…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_develop_communication_strategy_agent.py` first:

```bash
python3 demo_data_develop_communication_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_develop_communication_strategy_agent.py   # or on stdin
python3 demo_data_develop_communication_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop communication strategy Demo Data Generator — Generates and creates realistic demo records for develop communication strategy in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-communication-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_develop_communication_strategy',
    "version": '2.0.0',
    "display_name": 'Develop communication strategy Demo Data Generator',
    "description": 'Generates and creates realistic demo records for develop communication strategy in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-develop-communication-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-develop-communication-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0750c9e98f5bb113',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/develop-people-strategy/develop-communication-strategy'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/demo-data-develop-communication-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataDevelopCommunicationStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDevelopCommunicationStrategy'
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
    print(DemoDataDevelopCommunicationStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
