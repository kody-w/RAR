---
name: "rar-cowork-cookbook-scheduled-brief-process-customer-returns-and-exchanges"
description: "Schedulable morning-brief email summarizing process customer returns and exchanges for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_process_customer_returns_and_exchanges", "rar_sha256": "8312a094a815a8e014a33c97989c8ac8c41c747773606ac889f19bf51555d5c4", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_process_customer_returns_and_exchanges`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_process_customer_returns_and_exchanges_agent.py` and in the RCI capsule.

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

Process customer returns and exchanges Scheduled Email Brief — Schedulable morning-brief email summarizing process customer returns and exchanges for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-process-customer-returns-and-exchanges
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_process_customer_returns_and_exchanges_agent.py` and embedded as the fenced Python below (sha256 8312a094a815a8e0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_process_customer_returns_and_exchanges_agent.py` first:

```bash
python3 scheduled_brief_process_customer_returns_and_exchanges_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_process_customer_returns_and_exchanges_agent.py   # or on stdin
python3 scheduled_brief_process_customer_returns_and_exchanges_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process customer returns and exchanges Scheduled Email Brief — Schedulable morning-brief email summarizing process customer returns and exchanges for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-process-customer-returns-and-exchanges
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_process_customer_returns_and_exchanges',
    "version": '2.0.1',
    "display_name": 'Process customer returns and exchanges Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing process customer returns and exchanges for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-process-customer-returns-and-exchanges',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-process-customer-returns-and-exchanges',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '96cc918606660afe',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-sales-orders/process-customer-returns-and-exchanges'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/scheduled-brief-process-customer-returns-and-exchanges', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefProcessCustomerReturnsAndExchanges(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefProcessCustomerReturnsAndExchanges'
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
    print(ScheduledBriefProcessCustomerReturnsAndExchanges().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
