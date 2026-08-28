---
name: "rar-cowork-cookbook-demo-data-define-credit-and-collections-strategy"
description: "Generates and creates realistic demo records for define credit and collections strategy in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_credit_and_collections_strategy", "rar_sha256": "28d8e2996facb121da33eae5d39764abc6df4bfebf8d8730d265e26c6a97672a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_define_credit_and_collections_strategy`. The original RAPP
agent is preserved byte-for-byte in `demo_data_define_credit_and_collections_strategy_agent.py` and in the RCI capsule.

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

Define credit and collections strategy Demo Data Generator — Generates and creates realistic demo records for define credit and collections strategy in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-credit-and-collections-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_define_credit_and_collections_strategy_agent.py` and embedded as the fenced Python below (sha256 28d8e2996facb121…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_define_credit_and_collections_strategy_agent.py` first:

```bash
python3 demo_data_define_credit_and_collections_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_define_credit_and_collections_strategy_agent.py   # or on stdin
python3 demo_data_define_credit_and_collections_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define credit and collections strategy Demo Data Generator — Generates and creates realistic demo records for define credit and collections strategy in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-credit-and-collections-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_define_credit_and_collections_strategy',
    "version": '2.0.0',
    "display_name": 'Define credit and collections strategy Demo Data Generator',
    "description": 'Generates and creates realistic demo records for define credit and collections strategy in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-define-credit-and-collections-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-define-credit-and-collections-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f755b82bb9955380',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/develop-sales-policies/define-credit-and-collections-strategy'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/demo-data-define-credit-and-collections-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataDefineCreditAndCollectionsStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDefineCreditAndCollectionsStrategy'
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
    print(DemoDataDefineCreditAndCollectionsStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
