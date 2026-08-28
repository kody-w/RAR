---
name: "rar-cowork-cookbook-demo-data-manage-bills-of-exchange"
description: "Generates and creates realistic demo records for manage bills of exchange in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_bills_of_exchange", "rar_sha256": "57c5671556245dac6acf204d495fb1ed9d52d35484c2f561e3457f7e90a21b19", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_manage_bills_of_exchange_agent.py` and embedded as the fenced Python below (sha256 57c5671556245dac…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_manage_bills_of_exchange_agent.py` first:

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
    "version": '2.0.0',
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
