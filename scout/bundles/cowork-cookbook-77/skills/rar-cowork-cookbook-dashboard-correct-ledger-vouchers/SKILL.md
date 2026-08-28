---
name: "rar-cowork-cookbook-dashboard-correct-ledger-vouchers"
description: "Produces a self-contained interactive HTML dashboard for correct ledger vouchers - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_correct_ledger_vouchers", "rar_sha256": "ec5dbcca4c17cc229f723cec713048069abcda17f04c12e0c318e4e4336283d7", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_correct_ledger_vouchers`. The original RAPP
agent is preserved byte-for-byte in `dashboard_correct_ledger_vouchers_agent.py` and in the RCI capsule.

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

Correct ledger vouchers Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for correct ledger vouchers - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-correct-ledger-vouchers
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_correct_ledger_vouchers_agent.py` and embedded as the fenced Python below (sha256 ec5dbcca4c17cc22…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_correct_ledger_vouchers_agent.py` first:

```bash
python3 dashboard_correct_ledger_vouchers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_correct_ledger_vouchers_agent.py   # or on stdin
python3 dashboard_correct_ledger_vouchers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Correct ledger vouchers Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for correct ledger vouchers - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-correct-ledger-vouchers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_correct_ledger_vouchers',
    "version": '2.0.1',
    "display_name": 'Correct ledger vouchers Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for correct ledger vouchers - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-correct-ledger-vouchers',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-correct-ledger-vouchers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '41a5b126380bb783',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/correct-ledger-vouchers'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/dashboard-correct-ledger-vouchers', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class DashboardCorrectLedgerVouchers(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardCorrectLedgerVouchers'
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
    print(DashboardCorrectLedgerVouchers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
