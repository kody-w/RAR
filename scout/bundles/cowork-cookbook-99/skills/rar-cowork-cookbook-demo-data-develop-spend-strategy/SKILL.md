---
name: "rar-cowork-cookbook-demo-data-develop-spend-strategy"
description: "Generates and creates realistic demo records for develop spend strategy in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_spend_strategy", "rar_sha256": "1a3b182aea261ac6c1d741b8336fc52a68bb98ed4e6e4091a380decf0b4b348a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_develop_spend_strategy_agent.py` and embedded as the fenced Python below (sha256 1a3b182aea261ac6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_develop_spend_strategy_agent.py` first:

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
    "version": '2.0.0',
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
