---
name: "rar-cowork-cookbook-dashboard-report-an-injury-or-illness"
description: "Produces a self-contained interactive HTML dashboard for report an injury or illness - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_report_an_injury_or_illness", "rar_sha256": "ae2c0da3b7db6f3da1608c1fc1b45c388592fe6b79c91f64ec0182f1e410963d", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_report_an_injury_or_illness_agent.py` and embedded as the fenced Python below (sha256 ae2c0da3b7db6f3d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_report_an_injury_or_illness_agent.py` first:

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
    "version": '2.0.1',
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
