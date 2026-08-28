---
name: "rar-cowork-cookbook-adaptive-card-manage-bills-of-exchange"
description: "Produces a reusable Adaptive Card JSON snapshot of manage bills of exchange status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_bills_of_exchange", "rar_sha256": "5797e54ccb87f2f28736e0c819ee82adc50eab90ed087986d593caa21ffc275c", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_manage_bills_of_exchange_agent.py` and embedded as the fenced Python below (sha256 5797e54ccb87f2f2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_manage_bills_of_exchange_agent.py` first:

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
    "version": '2.0.1',
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
