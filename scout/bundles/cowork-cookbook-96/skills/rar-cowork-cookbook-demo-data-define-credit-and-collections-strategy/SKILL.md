---
name: "rar-cowork-cookbook-demo-data-define-credit-and-collections-strategy"
description: "Generates and creates realistic demo records for define credit and collections strategy in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_credit_and_collections_strategy", "rar_sha256": "36aa8a9f0df9054362a4842f9d962ecf816379a61d35cc3492213975dbb64791", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_define_credit_and_collections_strategy_agent.py` and embedded as the fenced Python below (sha256 36aa8a9f0df90543…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_define_credit_and_collections_strategy_agent.py` first:

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
    "version": '2.0.1',
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
