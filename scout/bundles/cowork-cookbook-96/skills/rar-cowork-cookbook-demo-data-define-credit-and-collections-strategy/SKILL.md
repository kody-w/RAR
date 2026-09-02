---
name: "rar-cowork-cookbook-demo-data-define-credit-and-collections-strategy"
description: "Generates and creates realistic demo records for define credit and collections strategy in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_credit_and_collections_strategy", "rar_sha256": "28d8e2996facb121da33eae5d39764abc6df4bfebf8d8730d265e26c6a97672a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_define_credit_and_collections_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-define-credit-and-collections-strategy:167731f0d08bf8f279037eaa6f45bdc091d718d98561dea2856d069c1e693fd6", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_define_credit_and_collections_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_define_credit_and_collections_strategy_agent.py` is
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
