---
name: "rar-cowork-cookbook-scheduled-brief-issue-and-settle-supplier-payments"
description: "Schedulable morning-brief email summarizing issue and settle supplier payments for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_issue_and_settle_supplier_payments", "rar_sha256": "c86e4ff8fee97eb28f7046b6a09acacc2a1efe74e954f37713b130cb72e05996", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_issue_and_settle_supplier_payments_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-issue-and-settle-supplier-payments:51bec7bb173274380b9839229e32b1ef4294139f897c236aa02c834046d09e3d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_issue_and_settle_supplier_payments`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_issue_and_settle_supplier_payments_agent.py` is
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

Issue and settle supplier payments Scheduled Email Brief — Schedulable morning-brief email summarizing issue and settle supplier payments for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-issue-and-settle-supplier-payments
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_issue_and_settle_supplier_payments_agent.py` and embedded as the fenced Python below (sha256 c86e4ff8fee97eb2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_issue_and_settle_supplier_payments_agent.py` first:

```bash
python3 scheduled_brief_issue_and_settle_supplier_payments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_issue_and_settle_supplier_payments_agent.py   # or on stdin
python3 scheduled_brief_issue_and_settle_supplier_payments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Issue and settle supplier payments Scheduled Email Brief — Schedulable morning-brief email summarizing issue and settle supplier payments for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-issue-and-settle-supplier-payments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_issue_and_settle_supplier_payments',
    "version": '2.0.0',
    "display_name": 'Issue and settle supplier payments Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing issue and settle supplier payments for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-issue-and-settle-supplier-payments',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-issue-and-settle-supplier-payments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ec9d99bdd1defe57',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-accounts-payable/issue-and-settle-supplier-payments'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/scheduled-brief-issue-and-settle-supplier-payments', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class ScheduledBriefIssueAndSettleSupplierPayments(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefIssueAndSettleSupplierPayments'
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
    print(ScheduledBriefIssueAndSettleSupplierPayments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
