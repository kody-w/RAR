---
name: "rar-cowork-cookbook-dashboard-record-ledger-entries"
description: "Produces a self-contained interactive HTML dashboard for record ledger entries - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_record_ledger_entries", "rar_sha256": "b52614dcdc10ffc95dd1e10d003648ad582b7dff15179658e0d4907482b91f97", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_record_ledger_entries_agent.py` and embedded as the fenced Python below (sha256 b52614dcdc10ffc9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_record_ledger_entries_agent.py` first:

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
    "version": '2.0.0',
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
