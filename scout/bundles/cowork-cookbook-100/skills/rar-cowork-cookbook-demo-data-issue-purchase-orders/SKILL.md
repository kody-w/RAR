---
name: "rar-cowork-cookbook-demo-data-issue-purchase-orders"
description: "Generates and creates realistic demo records for issue purchase orders in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_issue_purchase_orders", "rar_sha256": "30a00e4a4083ec866bbe10c7f91ba135257593a9f3613e1ac2caa30f04068c5a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_issue_purchase_orders`. The original RAPP
agent is preserved byte-for-byte in `demo_data_issue_purchase_orders_agent.py` and in the RCI capsule.

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

Issue purchase orders Demo Data Generator — Generates and creates realistic demo records for issue purchase orders in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-issue-purchase-orders
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_issue_purchase_orders_agent.py` and embedded as the fenced Python below (sha256 30a00e4a4083ec86…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_issue_purchase_orders_agent.py` first:

```bash
python3 demo_data_issue_purchase_orders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_issue_purchase_orders_agent.py   # or on stdin
python3 demo_data_issue_purchase_orders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Issue purchase orders Demo Data Generator — Generates and creates realistic demo records for issue purchase orders in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-issue-purchase-orders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_issue_purchase_orders',
    "version": '2.0.1',
    "display_name": 'Issue purchase orders Demo Data Generator',
    "description": 'Generates and creates realistic demo records for issue purchase orders in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-issue-purchase-orders',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-issue-purchase-orders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2b27daf3268ca958',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/procure-goods-and-services/issue-purchase-orders'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/demo-data-issue-purchase-orders', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataIssuePurchaseOrders(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataIssuePurchaseOrders'
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
    print(DemoDataIssuePurchaseOrders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
