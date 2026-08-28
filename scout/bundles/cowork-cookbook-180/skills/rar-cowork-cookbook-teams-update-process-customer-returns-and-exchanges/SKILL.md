---
name: "rar-cowork-cookbook-teams-update-process-customer-returns-and-exchanges"
description: "Drafts a Teams channel post on process customer returns and exchanges status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_process_customer_returns_and_exchanges", "rar_sha256": "692d349a4683992f152bf420a729aa3462714f5a2eb35208ddab5aafefa51af9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_process_customer_returns_and_exchanges_agent.py` and embedded as the fenced Python below (sha256 692d349a4683992f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_process_customer_returns_and_exchanges_agent.py` first:

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
    "version": '2.0.0',
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
