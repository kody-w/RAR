---
name: "rar-cowork-cookbook-demo-data-bill-subscriptions"
description: "Generates and creates realistic demo records for bill subscriptions in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_bill_subscriptions", "rar_sha256": "40e71a2d3f4c0eeadde3cad3f69f6328989a88f1f03d7af06097fad541db024a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_bill_subscriptions_agent.py` and embedded as the fenced Python below (sha256 40e71a2d3f4c0eea…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_bill_subscriptions_agent.py` first:

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
    "version": '2.0.1',
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
