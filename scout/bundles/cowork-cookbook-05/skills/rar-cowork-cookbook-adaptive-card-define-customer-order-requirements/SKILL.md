---
name: "rar-cowork-cookbook-adaptive-card-define-customer-order-requirements"
description: "Produces a reusable Adaptive Card JSON snapshot of define customer order requirements status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_customer_order_requirements", "rar_sha256": "9c79ea68666e24f1b2c30c3a0e6a4d0b2aed8908e0c8161bc8afab115459a86c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_define_customer_order_requirements_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-define-customer-order-requirements:a489263de985a008cbbda86173353f7c0f86966463bf5da53e362b0821897073", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_define_customer_order_requirements`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_define_customer_order_requirements_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_define_customer_order_requirements_agent.py` and embedded as the fenced Python below (sha256 9c79ea68666e24f1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_define_customer_order_requirements_agent.py` first:

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
    "version": '2.0.0',
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
