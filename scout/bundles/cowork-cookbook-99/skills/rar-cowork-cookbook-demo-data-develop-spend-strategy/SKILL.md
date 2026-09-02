---
name: "rar-cowork-cookbook-demo-data-develop-spend-strategy"
description: "Generates and creates realistic demo records for develop spend strategy in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_spend_strategy", "rar_sha256": "1a3b182aea261ac6c1d741b8336fc52a68bb98ed4e6e4091a380decf0b4b348a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_develop_spend_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-develop-spend-strategy:769dfe4c654045706c50106255e91c053e4503d2f48ef6cbad2c30d26459307e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_develop_spend_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_develop_spend_strategy_agent.py` is
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
