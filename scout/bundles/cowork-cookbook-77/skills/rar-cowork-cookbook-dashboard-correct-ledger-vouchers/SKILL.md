---
name: "rar-cowork-cookbook-dashboard-correct-ledger-vouchers"
description: "Produces a self-contained interactive HTML dashboard for correct ledger vouchers - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_correct_ledger_vouchers", "rar_sha256": "81d8eb5118593f8674df9e42fa9ee08e8cbca2ae5663f4dab94abfd8912d03ec", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_correct_ledger_vouchers_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-correct-ledger-vouchers:4c8becd8af158144bd7666985999e9cf064cd48c3d157820627c28abc54e0143", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_correct_ledger_vouchers`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_correct_ledger_vouchers_agent.py` is
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
