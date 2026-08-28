---
name: "rar-cowork-cookbook-ppt-exec-monitor-human-capital-expenses"
description: "Generates an executive-ready PowerPoint deck on monitor human capital expenses status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_monitor_human_capital_expenses", "rar_sha256": "eda4c5aae8c1d1d37960b6bbf1b75cf0a63c89a043018b11d876b2b233026ad7", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_monitor_human_capital_expenses`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_monitor_human_capital_expenses_agent.py` and in the RCI capsule.

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

Monitor human capital expenses Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on monitor human capital expenses status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-monitor-human-capital-expenses
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_monitor_human_capital_expenses_agent.py` and embedded as the fenced Python below (sha256 eda4c5aae8c1d1d3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_monitor_human_capital_expenses_agent.py` first:

```bash
python3 ppt_exec_monitor_human_capital_expenses_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_monitor_human_capital_expenses_agent.py   # or on stdin
python3 ppt_exec_monitor_human_capital_expenses_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor human capital expenses Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on monitor human capital expenses status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-monitor-human-capital-expenses
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_monitor_human_capital_expenses',
    "version": '2.0.1',
    "display_name": 'Monitor human capital expenses Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on monitor human capital expenses status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-monitor-human-capital-expenses',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-monitor-human-capital-expenses',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '79bc630288488ae8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/analyze-hr-programs/monitor-human-capital-expenses'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/ppt-exec-monitor-human-capital-expenses', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecMonitorHumanCapitalExpenses(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecMonitorHumanCapitalExpenses'
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
    print(PptExecMonitorHumanCapitalExpenses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
