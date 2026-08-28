---
name: "rar-cowork-cookbook-adaptive-card-define-customer-classifications"
description: "Produces a reusable Adaptive Card JSON snapshot of define customer classifications status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_customer_classifications", "rar_sha256": "59ece9d9debea483aa9a150b4c308322a8f6032a793bfb386ccf6ded05bec2eb", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_define_customer_classifications`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_define_customer_classifications_agent.py` and in the RCI capsule.

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

Define customer classifications Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of define customer classifications status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-customer-classifications
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_define_customer_classifications_agent.py` and embedded as the fenced Python below (sha256 59ece9d9debea483…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_define_customer_classifications_agent.py` first:

```bash
python3 adaptive_card_define_customer_classifications_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_define_customer_classifications_agent.py   # or on stdin
python3 adaptive_card_define_customer_classifications_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define customer classifications Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of define customer classifications status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-customer-classifications
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_define_customer_classifications',
    "version": '2.0.1',
    "display_name": 'Define customer classifications Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of define customer classifications status for embedding in dashboards, emails, or Teams.',
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
        "upstream_slug": 'adaptive-card-define-customer-classifications',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-define-customer-classifications',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3bb499a17f02b974',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/develop-sales-policies/define-customer-classifications'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/adaptive-card-define-customer-classifications', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardDefineCustomerClassifications(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDefineCustomerClassifications'
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
    print(AdaptiveCardDefineCustomerClassifications().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
