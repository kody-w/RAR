---
name: "rar-cowork-cookbook-dashboard-report-an-injury-or-illness"
description: "Produces a self-contained interactive HTML dashboard for report an injury or illness - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_report_an_injury_or_illness", "rar_sha256": "bdbdb83b8ce93b6510072af2c801177087e6a4b9ac6e2e88d768bba6a3dc58f3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_report_an_injury_or_illness_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-report-an-injury-or-illness:4ba450ab983ae11d424bb26687db39226f99e0f9bdd1ab2955bd2b5336ec0339", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_report_an_injury_or_illness`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_report_an_injury_or_illness_agent.py` is
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

Report an injury or illness Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for report an injury or illness - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-report-an-injury-or-illness
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_report_an_injury_or_illness_agent.py` and embedded as the fenced Python below (sha256 bdbdb83b8ce93b65…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_report_an_injury_or_illness_agent.py` first:

```bash
python3 dashboard_report_an_injury_or_illness_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_report_an_injury_or_illness_agent.py   # or on stdin
python3 dashboard_report_an_injury_or_illness_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Report an injury or illness Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for report an injury or illness - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-report-an-injury-or-illness
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_report_an_injury_or_illness',
    "version": '2.0.0',
    "display_name": 'Report an injury or illness Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for report an injury or illness - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'dashboard-report-an-injury-or-illness',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-report-an-injury-or-illness',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1750ab09d5eab8e7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-workplace-compliance/report-an-injury-or-illness'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/dashboard-report-an-injury-or-illness', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardReportAnInjuryOrIllness(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardReportAnInjuryOrIllness'
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
    print(DashboardReportAnInjuryOrIllness().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
