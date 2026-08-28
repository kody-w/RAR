---
name: "rar-cowork-cookbook-adaptive-card-define-customer-classifications"
description: "Produces a reusable Adaptive Card JSON snapshot of define customer classifications status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_customer_classifications", "rar_sha256": "038571f43c7a346e443d651320441fc5dc93257d81f6280cb1c13e6532bea0eb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_define_customer_classifications_agent.py` and embedded as the fenced Python below (sha256 038571f43c7a346e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_define_customer_classifications_agent.py` first:

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
    "version": '2.0.0',
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
