---
name: "rar-cowork-cookbook-teams-update-process-customer-returns-and-exchanges"
description: "Drafts a Teams channel post on process customer returns and exchanges status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_process_customer_returns_and_exchanges", "rar_sha256": "c6fb0eba8fc0d8cbd7e6e59c1b72ba14310eb9e3fa30b342e56417c466da72b6", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_process_customer_returns_and_exchanges`. The original RAPP
agent is preserved byte-for-byte in `teams_update_process_customer_returns_and_exchanges_agent.py` and in the RCI capsule.

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

Process customer returns and exchanges Teams Channel Update — Drafts a Teams channel post on process customer returns and exchanges status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-process-customer-returns-and-exchanges
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_process_customer_returns_and_exchanges_agent.py` and embedded as the fenced Python below (sha256 c6fb0eba8fc0d8cb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_process_customer_returns_and_exchanges_agent.py` first:

```bash
python3 teams_update_process_customer_returns_and_exchanges_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_process_customer_returns_and_exchanges_agent.py   # or on stdin
python3 teams_update_process_customer_returns_and_exchanges_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process customer returns and exchanges Teams Channel Update — Drafts a Teams channel post on process customer returns and exchanges status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-process-customer-returns-and-exchanges
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_process_customer_returns_and_exchanges',
    "version": '2.0.1',
    "display_name": 'Process customer returns and exchanges Teams Channel Update',
    "description": 'Drafts a Teams channel post on process customer returns and exchanges status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-process-customer-returns-and-exchanges',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-process-customer-returns-and-exchanges',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e01a6bbd0637b706',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-sales-orders/process-customer-returns-and-exchanges'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/teams-update-process-customer-returns-and-exchanges', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateProcessCustomerReturnsAndExchanges(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateProcessCustomerReturnsAndExchanges'
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
    print(TeamsUpdateProcessCustomerReturnsAndExchanges().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
