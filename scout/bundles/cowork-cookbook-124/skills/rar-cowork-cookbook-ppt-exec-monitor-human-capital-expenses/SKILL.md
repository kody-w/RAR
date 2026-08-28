---
name: "rar-cowork-cookbook-ppt-exec-monitor-human-capital-expenses"
description: "Generates an executive-ready PowerPoint deck on monitor human capital expenses status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_monitor_human_capital_expenses", "rar_sha256": "8ca4f6eb4348883d7c5bf9d2e9acebc990b4227ab62c363217478a755e4ce781", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_monitor_human_capital_expenses_agent.py` and embedded as the fenced Python below (sha256 8ca4f6eb4348883d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_monitor_human_capital_expenses_agent.py` first:

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
    "version": '2.0.0',
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
