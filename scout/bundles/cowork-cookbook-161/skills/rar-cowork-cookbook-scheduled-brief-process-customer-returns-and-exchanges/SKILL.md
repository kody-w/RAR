---
name: "rar-cowork-cookbook-scheduled-brief-process-customer-returns-and-exchanges"
description: "Schedulable morning-brief email summarizing process customer returns and exchanges for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_process_customer_returns_and_exchanges", "rar_sha256": "ddc67d9d077c380453a9449aa37a842c0f34d50312eb8f3c8d142399d31f4aab", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_process_customer_returns_and_exchanges_agent.py` and embedded as the fenced Python below (sha256 ddc67d9d077c3804…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_process_customer_returns_and_exchanges_agent.py` first:

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
    "version": '2.0.0',
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
