---
name: "rar-cowork-cookbook-demo-data-issue-purchase-orders"
description: "Generates and creates realistic demo records for issue purchase orders in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_issue_purchase_orders", "rar_sha256": "18a0fcec5fe7a52225a4ebe5e5f2055a6667e9aabd844bb756fc235c4612528b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_issue_purchase_orders_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-issue-purchase-orders:7a974bbd9b4addfe514939828fc9fadaf116705a9ad6f657f9022f0d32932491", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_issue_purchase_orders`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_issue_purchase_orders_agent.py` is
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
