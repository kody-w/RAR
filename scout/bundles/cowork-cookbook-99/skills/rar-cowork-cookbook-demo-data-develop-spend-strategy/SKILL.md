---
name: "rar-cowork-cookbook-demo-data-develop-spend-strategy"
description: "Generates and creates realistic demo records for develop spend strategy in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_spend_strategy", "rar_sha256": "4fe8d3b8acd84b5fdb567b6604067fcd7946e583b477dea1dadac3e4e13449a2", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_develop_spend_strategy`. The original RAPP
agent is preserved byte-for-byte in `demo_data_develop_spend_strategy_agent.py` and in the RCI capsule.

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

Develop spend strategy Demo Data Generator — Generates and creates realistic demo records for develop spend strategy in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-spend-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_develop_spend_strategy_agent.py` and embedded as the fenced Python below (sha256 4fe8d3b8acd84b5f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_develop_spend_strategy_agent.py` first:

```bash
python3 demo_data_develop_spend_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_develop_spend_strategy_agent.py   # or on stdin
python3 demo_data_develop_spend_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop spend strategy Demo Data Generator — Generates and creates realistic demo records for develop spend strategy in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-spend-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_develop_spend_strategy',
    "version": '2.0.1',
    "display_name": 'Develop spend strategy Demo Data Generator',
    "description": 'Generates and creates realistic demo records for develop spend strategy in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-develop-spend-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-develop-spend-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '55210fa9dbe643df',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/develop-procurement-and-sourcing-strategy/develop-spend-strategy'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/demo-data-develop-spend-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataDevelopSpendStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDevelopSpendStrategy'
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
    print(DemoDataDevelopSpendStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
