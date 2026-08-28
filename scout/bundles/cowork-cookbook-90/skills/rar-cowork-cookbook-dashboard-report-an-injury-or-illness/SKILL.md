---
name: "rar-cowork-cookbook-dashboard-report-an-injury-or-illness"
description: "Produces a self-contained interactive HTML dashboard for report an injury or illness - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_report_an_injury_or_illness", "rar_sha256": "bdbdb83b8ce93b6510072af2c801177087e6a4b9ac6e2e88d768bba6a3dc58f3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_report_an_injury_or_illness`. The original RAPP
agent is preserved byte-for-byte in `dashboard_report_an_injury_or_illness_agent.py` and in the RCI capsule.

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
