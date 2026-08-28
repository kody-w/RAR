---
name: "rar-cowork-cookbook-ppt-exec-monitor-budget-to-actuals"
description: "Generates an executive-ready PowerPoint deck on monitor budget to actuals status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_monitor_budget_to_actuals", "rar_sha256": "28731c646cf6942a17ba386f6c1dcbfb24a3a949331dfd9ce957e35098a2da05", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_monitor_budget_to_actuals`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_monitor_budget_to_actuals_agent.py` and in the RCI capsule.

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

Monitor budget to actuals Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on monitor budget to actuals status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-monitor-budget-to-actuals
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_monitor_budget_to_actuals_agent.py` and embedded as the fenced Python below (sha256 28731c646cf6942a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_monitor_budget_to_actuals_agent.py` first:

```bash
python3 ppt_exec_monitor_budget_to_actuals_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_monitor_budget_to_actuals_agent.py   # or on stdin
python3 ppt_exec_monitor_budget_to_actuals_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor budget to actuals Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on monitor budget to actuals status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-monitor-budget-to-actuals
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_monitor_budget_to_actuals',
    "version": '2.0.0',
    "display_name": 'Monitor budget to actuals Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on monitor budget to actuals status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-monitor-budget-to-actuals',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-monitor-budget-to-actuals',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e0036591e7b1cfe2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/analyze-financial-performance/monitor-budget-to-actuals'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/ppt-exec-monitor-budget-to-actuals', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecMonitorBudgetToActuals(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecMonitorBudgetToActuals'
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
    print(PptExecMonitorBudgetToActuals().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
