---
name: "rar-cowork-cookbook-ppt-exec-monitor-financial-performance"
description: "Generates an executive-ready PowerPoint deck on monitor financial performance status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_monitor_financial_performance", "rar_sha256": "3103ab5b2a7f83964f379d2ab92a85fb2d38c2be192dcadf386c29c06675b26f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_monitor_financial_performance_agent.py` and embedded as the fenced Python below (sha256 3103ab5b2a7f8396…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_monitor_financial_performance_agent.py` first:

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
    "version": '2.0.1',
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
