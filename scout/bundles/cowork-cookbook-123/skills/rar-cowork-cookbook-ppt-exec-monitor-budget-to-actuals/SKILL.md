---
name: "rar-cowork-cookbook-ppt-exec-monitor-budget-to-actuals"
description: "Generates an executive-ready PowerPoint deck on monitor budget to actuals status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_monitor_budget_to_actuals", "rar_sha256": "b9fb5f56600a5cfd2a0a47753c8da5cefa03e173335602920b7494b84a462c60", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_monitor_budget_to_actuals_agent.py` and embedded as the fenced Python below (sha256 b9fb5f56600a5cfd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_monitor_budget_to_actuals_agent.py` first:

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
    "version": '2.0.1',
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
