---
name: "rar-cowork-cookbook-dashboard-revalue-currency"
description: "Produces a self-contained interactive HTML dashboard for revalue currency - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_revalue_currency", "rar_sha256": "70fc3bdf95b97ea482a1cd4deb5bfd945b1d6ae84f966aa217817476dd655b73", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_revalue_currency_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-revalue-currency:d5b0cb218048f0466e7d59178098518da2fa811ef2433f1c01a5da4c5ba1a5bc", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_revalue_currency`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_revalue_currency_agent.py` is
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

Revalue currency Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for revalue currency - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-revalue-currency
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_revalue_currency_agent.py` and embedded as the fenced Python below (sha256 70fc3bdf95b97ea4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_revalue_currency_agent.py` first:

```bash
python3 dashboard_revalue_currency_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_revalue_currency_agent.py   # or on stdin
python3 dashboard_revalue_currency_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Revalue currency Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for revalue currency - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-revalue-currency
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_revalue_currency',
    "version": '2.0.0',
    "display_name": 'Revalue currency Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for revalue currency - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-revalue-currency',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-revalue-currency',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7a8e65201f2e2061',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/close-financial-periods/revalue-currency'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/dashboard-revalue-currency', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class DashboardRevalueCurrency(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardRevalueCurrency'
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
    print(DashboardRevalueCurrency().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
