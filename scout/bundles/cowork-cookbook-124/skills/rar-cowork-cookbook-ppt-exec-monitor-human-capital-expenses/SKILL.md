---
name: "rar-cowork-cookbook-ppt-exec-monitor-human-capital-expenses"
description: "Generates an executive-ready PowerPoint deck on monitor human capital expenses status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_monitor_human_capital_expenses", "rar_sha256": "8ca4f6eb4348883d7c5bf9d2e9acebc990b4227ab62c363217478a755e4ce781", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_monitor_human_capital_expenses_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-monitor-human-capital-expenses:44e40826c0afcd5c72ec189904043ec0f0cd37950d92b46d3dd93ec150ee8867", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_monitor_human_capital_expenses`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_monitor_human_capital_expenses_agent.py` is
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
