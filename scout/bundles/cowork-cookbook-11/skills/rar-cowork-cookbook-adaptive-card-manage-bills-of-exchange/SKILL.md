---
name: "rar-cowork-cookbook-adaptive-card-manage-bills-of-exchange"
description: "Produces a reusable Adaptive Card JSON snapshot of manage bills of exchange status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_bills_of_exchange", "rar_sha256": "0b0c1a95bd70ed6128a3fc2279fc209455369eea673f189e34a88cfe12c9d9a3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_manage_bills_of_exchange`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_manage_bills_of_exchange_agent.py` and in the RCI capsule.

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
