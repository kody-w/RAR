---
name: "rar-cowork-cookbook-ppt-exec-monitor-financial-performance"
description: "Generates an executive-ready PowerPoint deck on monitor financial performance status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_monitor_financial_performance", "rar_sha256": "295c4fee4492f23165a7b7bf265a4b41e167ceeb17d4f30ed553957e0e12861c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_monitor_financial_performance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-monitor-financial-performance:63655ad0934af0792889008f25d9c1e581da30b02a8ff1e71fae32ccc61f37a3", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_monitor_financial_performance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_monitor_financial_performance_agent.py` is
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
