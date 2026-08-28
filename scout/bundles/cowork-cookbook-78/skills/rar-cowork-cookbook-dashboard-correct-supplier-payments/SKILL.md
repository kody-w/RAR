---
name: "rar-cowork-cookbook-dashboard-correct-supplier-payments"
description: "Produces a self-contained interactive HTML dashboard for correct supplier payments - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_correct_supplier_payments", "rar_sha256": "01bf71fbe2762cfefe3ebdf9239a1b06c5d8dfc1aba808d3c31df9642c397cfa", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_correct_supplier_payments`. The original RAPP
agent is preserved byte-for-byte in `dashboard_correct_supplier_payments_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_correct_supplier_payments_agent.py` and embedded as the fenced Python below (sha256 01bf71fbe2762cfe…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_correct_supplier_payments_agent.py` first:

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
    "version": '2.0.1',
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
