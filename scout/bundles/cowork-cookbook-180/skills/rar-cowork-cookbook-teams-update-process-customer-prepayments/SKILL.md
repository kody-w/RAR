---
name: "rar-cowork-cookbook-teams-update-process-customer-prepayments"
description: "Drafts a Teams channel post on process customer prepayments status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_process_customer_prepayments", "rar_sha256": "e391319fb958affbf2db055a33b55773fe6b90f4f5557a74e221ee0930fa9cf0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_process_customer_prepayments_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-process-customer-prepayments:3e19ecca0d47e64d50ce7ea78c167b19ed23f93e044c4f47b6cfbde34033bf71", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_process_customer_prepayments`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_process_customer_prepayments_agent.py` is
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

Process customer prepayments Teams Channel Update — Drafts a Teams channel post on process customer prepayments status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-process-customer-prepayments
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_process_customer_prepayments_agent.py` and embedded as the fenced Python below (sha256 e391319fb958affb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_process_customer_prepayments_agent.py` first:

```bash
python3 teams_update_process_customer_prepayments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_process_customer_prepayments_agent.py   # or on stdin
python3 teams_update_process_customer_prepayments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process customer prepayments Teams Channel Update — Drafts a Teams channel post on process customer prepayments status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-process-customer-prepayments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_process_customer_prepayments',
    "version": '2.0.0',
    "display_name": 'Process customer prepayments Teams Channel Update',
    "description": 'Drafts a Teams channel post on process customer prepayments status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'teams-update-process-customer-prepayments',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-process-customer-prepayments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '45b62e8e59e1516b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/process-customer-prepayments'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/teams-update-process-customer-prepayments', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class TeamsUpdateProcessCustomerPrepayments(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateProcessCustomerPrepayments'
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
    print(TeamsUpdateProcessCustomerPrepayments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
