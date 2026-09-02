---
name: "rar-cowork-cookbook-dashboard-record-ledger-entries"
description: "Produces a self-contained interactive HTML dashboard for record ledger entries - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_record_ledger_entries", "rar_sha256": "b52614dcdc10ffc95dd1e10d003648ad582b7dff15179658e0d4907482b91f97", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_record_ledger_entries_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-record-ledger-entries:9bb592db6ad0b5d7dfa3014f1f358dda60c9ae7dcb5b2f673a4c6d638cd4df68", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_record_ledger_entries`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_record_ledger_entries_agent.py` is
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
