---
name: "rar-cowork-cookbook-dashboard-correct-supplier-payments"
description: "Produces a self-contained interactive HTML dashboard for correct supplier payments - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_correct_supplier_payments", "rar_sha256": "eaca80d1745b07b88a4c738b3ebff2a3157893b74f4c5cbfc4d5ca66794ee686", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_correct_supplier_payments_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-correct-supplier-payments:e49dd61e9f11cc0958dd1d6af63ff5a03d6e71ca9f781027171a967dd83a08dc", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_correct_supplier_payments`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_correct_supplier_payments_agent.py` is
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

Correct supplier payments Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for correct supplier payments - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-correct-supplier-payments
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_correct_supplier_payments_agent.py` and embedded as the fenced Python below (sha256 eaca80d1745b07b8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_correct_supplier_payments_agent.py` first:

```bash
python3 dashboard_correct_supplier_payments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_correct_supplier_payments_agent.py   # or on stdin
python3 dashboard_correct_supplier_payments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Correct supplier payments Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for correct supplier payments - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-correct-supplier-payments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_correct_supplier_payments',
    "version": '2.0.0',
    "display_name": 'Correct supplier payments Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for correct supplier payments - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-correct-supplier-payments',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-correct-supplier-payments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f38a4c99ce6cf5f7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-accounts-payable/correct-supplier-payments'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/dashboard-correct-supplier-payments', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DashboardCorrectSupplierPayments(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardCorrectSupplierPayments'
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
    print(DashboardCorrectSupplierPayments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
