---
name: "rar-cowork-cookbook-scheduled-brief-clean-up-and-archive-background-jobs"
description: "Schedulable morning-brief email summarizing clean up and archive background jobs for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_clean_up_and_archive_background_jobs", "rar_sha256": "7919f46cad9d3e11a4eb98c8ddcbabbd0f2e595e7fbed466db9278a81747212f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_clean_up_and_archive_background_jobs`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_clean_up_and_archive_background_jobs_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_clean_up_and_archive_background_jobs_agent.py` and embedded as the fenced Python below (sha256 7919f46cad9d3e11…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_clean_up_and_archive_background_jobs_agent.py` first:

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
    "version": '2.0.1',
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
