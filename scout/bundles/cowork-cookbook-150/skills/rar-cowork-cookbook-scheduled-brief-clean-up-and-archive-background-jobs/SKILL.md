---
name: "rar-cowork-cookbook-scheduled-brief-clean-up-and-archive-background-jobs"
description: "Schedulable morning-brief email summarizing clean up and archive background jobs for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_clean_up_and_archive_background_jobs", "rar_sha256": "05a11b1ed1f6a2fbb68e388e32d2f971f8b87884844f7c0d587dd83938fb5d0e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_clean_up_and_archive_background_jobs_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-clean-up-and-archive-background-jobs:2ee73c4f4b93db6df41952222259244c7536837951e5754affa32746c87fcbd9", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_clean_up_and_archive_background_jobs`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_clean_up_and_archive_background_jobs_agent.py` is
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

Clean up and archive background jobs Scheduled Email Brief — Schedulable morning-brief email summarizing clean up and archive background jobs for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-clean-up-and-archive-background-jobs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_clean_up_and_archive_background_jobs_agent.py` and embedded as the fenced Python below (sha256 05a11b1ed1f6a2fb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_clean_up_and_archive_background_jobs_agent.py` first:

```bash
python3 scheduled_brief_clean_up_and_archive_background_jobs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_clean_up_and_archive_background_jobs_agent.py   # or on stdin
python3 scheduled_brief_clean_up_and_archive_background_jobs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Clean up and archive background jobs Scheduled Email Brief — Schedulable morning-brief email summarizing clean up and archive background jobs for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-clean-up-and-archive-background-jobs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_clean_up_and_archive_background_jobs',
    "version": '2.0.0',
    "display_name": 'Clean up and archive background jobs Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing clean up and archive background jobs for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-clean-up-and-archive-background-jobs',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-clean-up-and-archive-background-jobs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd9238531aa1706a5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-background-jobs/clean-up-and-archive-background-jobs'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-clean-up-and-archive-background-jobs', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefCleanUpAndArchiveBackgroundJobs(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefCleanUpAndArchiveBackgroundJobs'
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
    print(ScheduledBriefCleanUpAndArchiveBackgroundJobs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
