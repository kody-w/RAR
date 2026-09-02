---
name: "rar-cowork-cookbook-scheduled-brief-analyze-project-metrics"
description: "Schedulable morning-brief email summarizing analyze project metrics for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_analyze_project_metrics", "rar_sha256": "434f8fb6de70ab167fb070cb51e81bba2a1c8d319a9e52250bb67751e933c5cf", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_analyze_project_metrics_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-analyze-project-metrics:f738cb62d785ff3e7353aea1b171bf92bc94ac757fd404e355e4e5776c2e589a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_analyze_project_metrics`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_analyze_project_metrics_agent.py` is
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
