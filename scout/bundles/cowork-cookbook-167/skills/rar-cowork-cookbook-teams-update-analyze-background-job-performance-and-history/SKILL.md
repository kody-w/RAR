---
name: "rar-cowork-cookbook-teams-update-analyze-background-job-performance-and-history"
description: "Drafts a Teams channel post on analyze background job performance and history status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_analyze_background_job_performance_and_history", "rar_sha256": "0030ab9051b3031fc95dfd09b63c93a891b4ce7fb77adcff655383b291ade4bd", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_analyze_background_job_performance_and_history_agent.py` and embedded as the fenced Python below (sha256 0030ab9051b3031f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_analyze_background_job_performance_and_history_agent.py` first:

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
    "version": '2.0.1',
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
