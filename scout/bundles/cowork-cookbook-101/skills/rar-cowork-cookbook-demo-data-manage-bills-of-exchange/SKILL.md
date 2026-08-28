---
name: "rar-cowork-cookbook-demo-data-manage-bills-of-exchange"
description: "Generates and creates realistic demo records for manage bills of exchange in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_bills_of_exchange", "rar_sha256": "a8cf0a28d06e55d5bd865721ab9659df36d8e196a01becb95816c21adf611d94", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_manage_bills_of_exchange`. The original RAPP
agent is preserved byte-for-byte in `demo_data_manage_bills_of_exchange_agent.py` and in the RCI capsule.

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

Manage bills of exchange Demo Data Generator — Generates and creates realistic demo records for manage bills of exchange in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-bills-of-exchange
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_manage_bills_of_exchange_agent.py` and embedded as the fenced Python below (sha256 a8cf0a28d06e55d5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_manage_bills_of_exchange_agent.py` first:

```bash
python3 demo_data_manage_bills_of_exchange_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_manage_bills_of_exchange_agent.py   # or on stdin
python3 demo_data_manage_bills_of_exchange_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage bills of exchange Demo Data Generator — Generates and creates realistic demo records for manage bills of exchange in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-bills-of-exchange
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_manage_bills_of_exchange',
    "version": '2.0.1',
    "display_name": 'Manage bills of exchange Demo Data Generator',
    "description": 'Generates and creates realistic demo records for manage bills of exchange in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-manage-bills-of-exchange',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-manage-bills-of-exchange',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '55dbc570073694d0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/manage-bills-of-exchange'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/demo-data-manage-bills-of-exchange', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataManageBillsOfExchange(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataManageBillsOfExchange'
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
    print(DemoDataManageBillsOfExchange().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
