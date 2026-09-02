---
name: "rar-cowork-cookbook-dashboard-prepare-statutory-financial-reports"
description: "Produces a self-contained interactive HTML dashboard for prepare statutory financial reports - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_prepare_statutory_financial_reports", "rar_sha256": "fed863143b57e6966331d08ef0ae3616211fd858b248c44189f39ac8ff7156e6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_prepare_statutory_financial_reports_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-prepare-statutory-financial-reports:778afb5e27059fb0d62b2d425c672d18047eded3fc245c954bac24eaf96fb641", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_prepare_statutory_financial_reports`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_prepare_statutory_financial_reports_agent.py` is
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

Prepare statutory financial reports Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for prepare statutory financial reports - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-prepare-statutory-financial-reports
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_prepare_statutory_financial_reports_agent.py` and embedded as the fenced Python below (sha256 fed863143b57e696…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_prepare_statutory_financial_reports_agent.py` first:

```bash
python3 dashboard_prepare_statutory_financial_reports_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_prepare_statutory_financial_reports_agent.py   # or on stdin
python3 dashboard_prepare_statutory_financial_reports_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Prepare statutory financial reports Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for prepare statutory financial reports - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-prepare-statutory-financial-reports
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_prepare_statutory_financial_reports',
    "version": '2.0.0',
    "display_name": 'Prepare statutory financial reports Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for prepare statutory financial reports - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-prepare-statutory-financial-reports',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-prepare-statutory-financial-reports',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ccb9256a0f20f88b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/close-financial-periods/prepare-statutory-financial-reports'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/dashboard-prepare-statutory-financial-reports', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class DashboardPrepareStatutoryFinancialReports(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardPrepareStatutoryFinancialReports'
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
    print(DashboardPrepareStatutoryFinancialReports().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
