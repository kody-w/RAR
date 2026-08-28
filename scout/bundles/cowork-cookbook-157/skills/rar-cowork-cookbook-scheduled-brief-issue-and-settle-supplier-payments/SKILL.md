---
name: "rar-cowork-cookbook-scheduled-brief-issue-and-settle-supplier-payments"
description: "Schedulable morning-brief email summarizing issue and settle supplier payments for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_issue_and_settle_supplier_payments", "rar_sha256": "63488edc435f7be49fe6528dd8e70b8c4bd923d98dad97c657e75ffbf6861af7", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_issue_and_settle_supplier_payments_agent.py` and embedded as the fenced Python below (sha256 63488edc435f7be4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_issue_and_settle_supplier_payments_agent.py` first:

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
    "version": '2.0.1',
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
