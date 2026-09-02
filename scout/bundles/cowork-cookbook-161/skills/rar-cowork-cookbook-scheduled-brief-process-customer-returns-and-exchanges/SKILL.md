---
name: "rar-cowork-cookbook-scheduled-brief-process-customer-returns-and-exchanges"
description: "Schedulable morning-brief email summarizing process customer returns and exchanges for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_process_customer_returns_and_exchanges", "rar_sha256": "ddc67d9d077c380453a9449aa37a842c0f34d50312eb8f3c8d142399d31f4aab", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_process_customer_returns_and_exchanges_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-process-customer-returns-and-exchanges:7ece0c8f794692edff666db76e6aea1c049bfe52db77031a53552a6c77a45af1", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_process_customer_returns_and_exchanges`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_process_customer_returns_and_exchanges_agent.py` is
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
