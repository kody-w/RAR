---
name: "rar-cowork-cookbook-ppt-exec-monitor-financial-performance"
description: "Generates an executive-ready PowerPoint deck on monitor financial performance status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_monitor_financial_performance", "rar_sha256": "295c4fee4492f23165a7b7bf265a4b41e167ceeb17d4f30ed553957e0e12861c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_monitor_financial_performance`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_monitor_financial_performance_agent.py` and in the RCI capsule.

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

Monitor financial performance Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on monitor financial performance status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-monitor-financial-performance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_monitor_financial_performance_agent.py` and embedded as the fenced Python below (sha256 295c4fee4492f231…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_monitor_financial_performance_agent.py` first:

```bash
python3 ppt_exec_monitor_financial_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_monitor_financial_performance_agent.py   # or on stdin
python3 ppt_exec_monitor_financial_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor financial performance Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on monitor financial performance status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-monitor-financial-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_monitor_financial_performance',
    "version": '2.0.0',
    "display_name": 'Monitor financial performance Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on monitor financial performance status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-monitor-financial-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-monitor-financial-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ee3625af6b05e802',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/analyze-business-performance/monitor-financial-performance'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/ppt-exec-monitor-financial-performance', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecMonitorFinancialPerformance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecMonitorFinancialPerformance'
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
    print(PptExecMonitorFinancialPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
