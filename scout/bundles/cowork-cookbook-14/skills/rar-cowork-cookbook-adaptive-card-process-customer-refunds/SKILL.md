---
name: "rar-cowork-cookbook-adaptive-card-process-customer-refunds"
description: "Produces a reusable Adaptive Card JSON snapshot of process customer refunds status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_process_customer_refunds", "rar_sha256": "8c0ee7c6fac9a01773dbcbe3525cb2841df6b7cf87c2dc004eae485994bbf83d", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_process_customer_refunds`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_process_customer_refunds_agent.py` and in the RCI capsule.

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

Process customer refunds Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of process customer refunds status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-process-customer-refunds
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_process_customer_refunds_agent.py` and embedded as the fenced Python below (sha256 8c0ee7c6fac9a017…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_process_customer_refunds_agent.py` first:

```bash
python3 adaptive_card_process_customer_refunds_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_process_customer_refunds_agent.py   # or on stdin
python3 adaptive_card_process_customer_refunds_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process customer refunds Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of process customer refunds status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-process-customer-refunds
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_process_customer_refunds',
    "version": '2.0.1',
    "display_name": 'Process customer refunds Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of process customer refunds status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-process-customer-refunds',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-process-customer-refunds',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '220fdcdffae77c7d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/process-customer-refunds'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/adaptive-card-process-customer-refunds', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardProcessCustomerRefunds(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardProcessCustomerRefunds'
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
    print(AdaptiveCardProcessCustomerRefunds().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
