---
name: "rar-cowork-cookbook-adaptive-card-define-customer-order-requirements"
description: "Produces a reusable Adaptive Card JSON snapshot of define customer order requirements status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_customer_order_requirements", "rar_sha256": "91d1a68364ee5b020d29fb1bcd4ac2f098707d314db21ad2dc635d41d415fe13", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_define_customer_order_requirements`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_define_customer_order_requirements_agent.py` and in the RCI capsule.

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

Define customer order requirements Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of define customer order requirements status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-customer-order-requirements
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_define_customer_order_requirements_agent.py` and embedded as the fenced Python below (sha256 91d1a68364ee5b02…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_define_customer_order_requirements_agent.py` first:

```bash
python3 adaptive_card_define_customer_order_requirements_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_define_customer_order_requirements_agent.py   # or on stdin
python3 adaptive_card_define_customer_order_requirements_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define customer order requirements Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of define customer order requirements status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-customer-order-requirements
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_define_customer_order_requirements',
    "version": '2.0.1',
    "display_name": 'Define customer order requirements Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of define customer order requirements status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-define-customer-order-requirements',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-define-customer-order-requirements',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '49c9f3e8ea2f0a07',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/define-customer-order-requirements'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/adaptive-card-define-customer-order-requirements', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardDefineCustomerOrderRequirements(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDefineCustomerOrderRequirements'
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
    print(AdaptiveCardDefineCustomerOrderRequirements().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
