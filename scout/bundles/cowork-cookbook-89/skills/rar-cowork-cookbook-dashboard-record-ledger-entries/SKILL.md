---
name: "rar-cowork-cookbook-dashboard-record-ledger-entries"
description: "Produces a self-contained interactive HTML dashboard for record ledger entries - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_record_ledger_entries", "rar_sha256": "2fa231c874db1b12ba8bec0faa6a8c4df2eb28c957f82e68570f43105b66249b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_record_ledger_entries`. The original RAPP
agent is preserved byte-for-byte in `dashboard_record_ledger_entries_agent.py` and in the RCI capsule.

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

Record ledger entries Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for record ledger entries - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-record-ledger-entries
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_record_ledger_entries_agent.py` and embedded as the fenced Python below (sha256 2fa231c874db1b12…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_record_ledger_entries_agent.py` first:

```bash
python3 dashboard_record_ledger_entries_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_record_ledger_entries_agent.py   # or on stdin
python3 dashboard_record_ledger_entries_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record ledger entries Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for record ledger entries - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-record-ledger-entries
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_record_ledger_entries',
    "version": '2.0.1',
    "display_name": 'Record ledger entries Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for record ledger entries - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-record-ledger-entries',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-record-ledger-entries',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ce8328a0e96eafc9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/record-ledger-entries'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/dashboard-record-ledger-entries', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class DashboardRecordLedgerEntries(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardRecordLedgerEntries'
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
    print(DashboardRecordLedgerEntries().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
