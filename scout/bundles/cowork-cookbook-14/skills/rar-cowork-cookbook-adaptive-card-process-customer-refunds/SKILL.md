---
name: "rar-cowork-cookbook-adaptive-card-process-customer-refunds"
description: "Produces a reusable Adaptive Card JSON snapshot of process customer refunds status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_process_customer_refunds", "rar_sha256": "6126670cd219135ce445bf28c999ae31534d32e03bc73bfd7688d28887c1b485", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_process_customer_refunds_agent.py` and embedded as the fenced Python below (sha256 6126670cd219135c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_process_customer_refunds_agent.py` first:

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
    "version": '2.0.0',
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
