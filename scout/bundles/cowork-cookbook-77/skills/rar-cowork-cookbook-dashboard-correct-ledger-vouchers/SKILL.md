---
name: "rar-cowork-cookbook-dashboard-correct-ledger-vouchers"
description: "Produces a self-contained interactive HTML dashboard for correct ledger vouchers - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_correct_ledger_vouchers", "rar_sha256": "81d8eb5118593f8674df9e42fa9ee08e8cbca2ae5663f4dab94abfd8912d03ec", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_correct_ledger_vouchers_agent.py` and embedded as the fenced Python below (sha256 81d8eb5118593f86…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_correct_ledger_vouchers_agent.py` first:

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
    "version": '2.0.0',
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
