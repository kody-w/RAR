---
name: "rar-cowork-cookbook-demo-data-bill-subscriptions"
description: "Generates and creates realistic demo records for bill subscriptions in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_bill_subscriptions", "rar_sha256": "55b8bd9ad17c0f547a16696d963dea412fbddb1494272ffbf6830c0b1f9a41fc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_bill_subscriptions_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-bill-subscriptions:1692b05dca713ea08988dffd5920d1b9955d92f6917d8530da9ff3b1ff285f5c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_bill_subscriptions`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_bill_subscriptions_agent.py` is
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
