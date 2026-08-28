---
name: "rar-cowork-cookbook-teams-update-analyze-background-job-performance-and-history"
description: "Drafts a Teams channel post on analyze background job performance and history status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_analyze_background_job_performance_and_history", "rar_sha256": "e652334716c779979d70c8f9bf6df06ac824c11ca8c2d352000bf0efb5aec09e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_analyze_background_job_performance_and_history`. The original RAPP
agent is preserved byte-for-byte in `teams_update_analyze_background_job_performance_and_history_agent.py` and in the RCI capsule.

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
