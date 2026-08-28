---
name: "rar-cowork-cookbook-scheduled-brief-analyze-project-metrics"
description: "Schedulable morning-brief email summarizing analyze project metrics for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_analyze_project_metrics", "rar_sha256": "434f8fb6de70ab167fb070cb51e81bba2a1c8d319a9e52250bb67751e933c5cf", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_analyze_project_metrics`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_analyze_project_metrics_agent.py` and in the RCI capsule.

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

Analyze project metrics Scheduled Email Brief — Schedulable morning-brief email summarizing analyze project metrics for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-analyze-project-metrics
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_analyze_project_metrics_agent.py` and embedded as the fenced Python below (sha256 434f8fb6de70ab16…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_analyze_project_metrics_agent.py` first:

```bash
python3 scheduled_brief_analyze_project_metrics_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_analyze_project_metrics_agent.py   # or on stdin
python3 scheduled_brief_analyze_project_metrics_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze project metrics Scheduled Email Brief — Schedulable morning-brief email summarizing analyze project metrics for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-analyze-project-metrics
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_analyze_project_metrics',
    "version": '2.0.0',
    "display_name": 'Analyze project metrics Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing analyze project metrics for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-analyze-project-metrics',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-analyze-project-metrics',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '02dff7dce92305f7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/analyze-project-performance/analyze-project-metrics'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/scheduled-brief-analyze-project-metrics', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefAnalyzeProjectMetrics(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefAnalyzeProjectMetrics'
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
    print(ScheduledBriefAnalyzeProjectMetrics().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
