---
name: "rar-cowork-cookbook-adaptive-card-process-customer-refunds"
description: "Produces a reusable Adaptive Card JSON snapshot of process customer refunds status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_process_customer_refunds", "rar_sha256": "6126670cd219135ce445bf28c999ae31534d32e03bc73bfd7688d28887c1b485", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_process_customer_refunds_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-process-customer-refunds:d90a9e45e6479db60940c4790649b1dba7b698ca4c6e60d09ddc76acb6c5a2b6", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_process_customer_refunds`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_process_customer_refunds_agent.py` is
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
