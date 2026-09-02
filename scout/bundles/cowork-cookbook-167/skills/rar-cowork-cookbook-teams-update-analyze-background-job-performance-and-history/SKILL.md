---
name: "rar-cowork-cookbook-teams-update-analyze-background-job-performance-and-history"
description: "Drafts a Teams channel post on analyze background job performance and history status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_analyze_background_job_performance_and_history", "rar_sha256": "e652334716c779979d70c8f9bf6df06ac824c11ca8c2d352000bf0efb5aec09e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_analyze_background_job_performance_and_history_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-analyze-background-job-performance-and-history:159ae6903791d97313ac0bb36dd3ddb90d8df1fd33d3236de4b45dbcc1217146", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_analyze_background_job_performance_and_history`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_analyze_background_job_performance_and_history_agent.py` is
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

Analyze background job performance and history Teams Channel Update — Drafts a Teams channel post on analyze background job performance and history status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-analyze-background-job-performance-and-history
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_analyze_background_job_performance_and_history_agent.py` and embedded as the fenced Python below (sha256 e652334716c77997…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_analyze_background_job_performance_and_history_agent.py` first:

```bash
python3 teams_update_analyze_background_job_performance_and_history_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_analyze_background_job_performance_and_history_agent.py   # or on stdin
python3 teams_update_analyze_background_job_performance_and_history_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze background job performance and history Teams Channel Update — Drafts a Teams channel post on analyze background job performance and history status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-analyze-background-job-performance-and-history
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_analyze_background_job_performance_and_history',
    "version": '2.0.0',
    "display_name": 'Analyze background job performance and history Teams Channel Update',
    "description": 'Drafts a Teams channel post on analyze background job performance and history status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-analyze-background-job-performance-and-history',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-analyze-background-job-performance-and-history',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3c28562c26c7ec97',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-background-jobs/analyze-background-job-performance-and-history'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-analyze-background-job-performance-and-history', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateAnalyzeBackgroundJobPerformanceAndHistory(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateAnalyzeBackgroundJobPerformanceAndHistory'
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
    print(TeamsUpdateAnalyzeBackgroundJobPerformanceAndHistory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
