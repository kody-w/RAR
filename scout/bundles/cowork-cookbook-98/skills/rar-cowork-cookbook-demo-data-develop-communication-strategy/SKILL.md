---
name: "rar-cowork-cookbook-demo-data-develop-communication-strategy"
description: "Generates and creates realistic demo records for develop communication strategy in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_communication_strategy", "rar_sha256": "e5991292073059183eec3405987ff2f3dbf11f7b693335b8be04ea7328196e13", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_develop_communication_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-develop-communication-strategy:1d981da9f28b402b62e2deb5c1b70d78ac76e8cbd7bb38001356bcf31e39cb53", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_develop_communication_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_develop_communication_strategy_agent.py` is
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
