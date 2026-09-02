---
name: "rar-cowork-cookbook-adaptive-card-manage-bills-of-exchange"
description: "Produces a reusable Adaptive Card JSON snapshot of manage bills of exchange status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_bills_of_exchange", "rar_sha256": "0b0c1a95bd70ed6128a3fc2279fc209455369eea673f189e34a88cfe12c9d9a3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_manage_bills_of_exchange_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-manage-bills-of-exchange:bfbf6d0d836cdd1dae8ece493c251635e9e7648fb7bd61ac47b83e8e6948224e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_manage_bills_of_exchange`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_manage_bills_of_exchange_agent.py` is
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

Manage bills of exchange Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of manage bills of exchange status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-bills-of-exchange
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_manage_bills_of_exchange_agent.py` and embedded as the fenced Python below (sha256 0b0c1a95bd70ed61…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_manage_bills_of_exchange_agent.py` first:

```bash
python3 adaptive_card_manage_bills_of_exchange_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_manage_bills_of_exchange_agent.py   # or on stdin
python3 adaptive_card_manage_bills_of_exchange_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage bills of exchange Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of manage bills of exchange status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-bills-of-exchange
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_manage_bills_of_exchange',
    "version": '2.0.0',
    "display_name": 'Manage bills of exchange Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of manage bills of exchange status for embedding in dashboards, emails, or Teams.',
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
        "upstream_slug": 'adaptive-card-manage-bills-of-exchange',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-manage-bills-of-exchange',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '131cf201ed5e4f68',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/manage-bills-of-exchange'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/adaptive-card-manage-bills-of-exchange', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardManageBillsOfExchange(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardManageBillsOfExchange'
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
    print(AdaptiveCardManageBillsOfExchange().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
