---
name: "rar-cowork-cookbook-teams-update-configure-and-run-background-jobs"
description: "Drafts a Teams channel post on configure and run background jobs status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_configure_and_run_background_jobs", "rar_sha256": "a7f97d8c66d1c9ee6d4c9833cd46d529602a95249e03447035a7beb7a3cdc3f7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_configure_and_run_background_jobs_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-configure-and-run-background-jobs:765dd216453b23835526d3c59c420df63d74f68d7bb8166c0d557a5fce2d8d96", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_configure_and_run_background_jobs`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_configure_and_run_background_jobs_agent.py` is
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

Configure and run background jobs Teams Channel Update — Drafts a Teams channel post on configure and run background jobs status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-configure-and-run-background-jobs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_configure_and_run_background_jobs_agent.py` and embedded as the fenced Python below (sha256 a7f97d8c66d1c9ee…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_configure_and_run_background_jobs_agent.py` first:

```bash
python3 teams_update_configure_and_run_background_jobs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_configure_and_run_background_jobs_agent.py   # or on stdin
python3 teams_update_configure_and_run_background_jobs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and run background jobs Teams Channel Update — Drafts a Teams channel post on configure and run background jobs status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-configure-and-run-background-jobs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_configure_and_run_background_jobs',
    "version": '2.0.0',
    "display_name": 'Configure and run background jobs Teams Channel Update',
    "description": 'Drafts a Teams channel post on configure and run background jobs status with an interactive Adaptive Card for quick triage.',
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
        "upstream_slug": 'teams-update-configure-and-run-background-jobs',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-configure-and-run-background-jobs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '53f598e1bfac3a35',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-background-jobs/configure-and-run-background-jobs'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-configure-and-run-background-jobs', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateConfigureAndRunBackgroundJobs(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateConfigureAndRunBackgroundJobs'
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
    print(TeamsUpdateConfigureAndRunBackgroundJobs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
