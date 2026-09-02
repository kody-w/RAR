---
name: "rar-cowork-cookbook-teams-update-process-customer-returns-and-exchanges"
description: "Drafts a Teams channel post on process customer returns and exchanges status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_process_customer_returns_and_exchanges", "rar_sha256": "692d349a4683992f152bf420a729aa3462714f5a2eb35208ddab5aafefa51af9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_process_customer_returns_and_exchanges_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-process-customer-returns-and-exchanges:de8f7825417f39599de79c30568feee4a01228be8fadfa7d498aae0b169b407b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_process_customer_returns_and_exchanges`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_process_customer_returns_and_exchanges_agent.py` is
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
