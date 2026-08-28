---
name: "rar-cowork-cookbook-scheduled-brief-issue-and-settle-supplier-payments"
description: "Schedulable morning-brief email summarizing issue and settle supplier payments for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_issue_and_settle_supplier_payments", "rar_sha256": "c86e4ff8fee97eb28f7046b6a09acacc2a1efe74e954f37713b130cb72e05996", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_issue_and_settle_supplier_payments`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_issue_and_settle_supplier_payments_agent.py` and in the RCI capsule.

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
