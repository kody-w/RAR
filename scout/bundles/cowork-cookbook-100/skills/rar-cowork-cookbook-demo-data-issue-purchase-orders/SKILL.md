---
name: "rar-cowork-cookbook-demo-data-issue-purchase-orders"
description: "Generates and creates realistic demo records for issue purchase orders in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_issue_purchase_orders", "rar_sha256": "18a0fcec5fe7a52225a4ebe5e5f2055a6667e9aabd844bb756fc235c4612528b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_issue_purchase_orders_agent.py` and embedded as the fenced Python below (sha256 18a0fcec5fe7a522…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_issue_purchase_orders_agent.py` first:

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
    "version": '2.0.0',
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
