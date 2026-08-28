---
name: "rar-cowork-cookbook-demo-data-bill-subscriptions"
description: "Generates and creates realistic demo records for bill subscriptions in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_bill_subscriptions", "rar_sha256": "55b8bd9ad17c0f547a16696d963dea412fbddb1494272ffbf6830c0b1f9a41fc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_bill_subscriptions`. The original RAPP
agent is preserved byte-for-byte in `demo_data_bill_subscriptions_agent.py` and in the RCI capsule.

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

Bill subscriptions Demo Data Generator — Generates and creates realistic demo records for bill subscriptions in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-bill-subscriptions
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_bill_subscriptions_agent.py` and embedded as the fenced Python below (sha256 55b8bd9ad17c0f54…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_bill_subscriptions_agent.py` first:

```bash
python3 demo_data_bill_subscriptions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_bill_subscriptions_agent.py   # or on stdin
python3 demo_data_bill_subscriptions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Bill subscriptions Demo Data Generator — Generates and creates realistic demo records for bill subscriptions in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-bill-subscriptions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_bill_subscriptions',
    "version": '2.0.0',
    "display_name": 'Bill subscriptions Demo Data Generator',
    "description": 'Generates and creates realistic demo records for bill subscriptions in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-bill-subscriptions',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-bill-subscriptions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6c3194b792ea58f9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/bill-subscriptions'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/demo-data-bill-subscriptions', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataBillSubscriptions(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataBillSubscriptions'
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
    print(DemoDataBillSubscriptions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
