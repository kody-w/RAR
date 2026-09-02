---
name: "rar-cowork-cookbook-scheduled-brief-configure-and-run-background-jobs"
description: "Schedulable morning-brief email summarizing configure and run background jobs for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_configure_and_run_background_jobs", "rar_sha256": "85a0c5df39cb9d06a72df6d33713076fb12e3546a6f5ddd6d10ba1d5fe032f1f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_configure_and_run_background_jobs_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-configure-and-run-background-jobs:985c3bcbc3f228136013d4e9cc298d1672b2ccde20358334c189d4dfa022e302", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_configure_and_run_background_jobs`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_configure_and_run_background_jobs_agent.py` is
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

Configure and run background jobs Scheduled Email Brief — Schedulable morning-brief email summarizing configure and run background jobs for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-configure-and-run-background-jobs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_configure_and_run_background_jobs_agent.py` and embedded as the fenced Python below (sha256 85a0c5df39cb9d06…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_configure_and_run_background_jobs_agent.py` first:

```bash
python3 scheduled_brief_configure_and_run_background_jobs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_configure_and_run_background_jobs_agent.py   # or on stdin
python3 scheduled_brief_configure_and_run_background_jobs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and run background jobs Scheduled Email Brief — Schedulable morning-brief email summarizing configure and run background jobs for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-configure-and-run-background-jobs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_configure_and_run_background_jobs',
    "version": '2.0.0',
    "display_name": 'Configure and run background jobs Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing configure and run background jobs for the responsible owner; designed to run daily or weekly.',
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
        "upstream_slug": 'scheduled-brief-configure-and-run-background-jobs',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-configure-and-run-background-jobs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f8bdc8e51cbe1f70',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-background-jobs/configure-and-run-background-jobs'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-configure-and-run-background-jobs', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefConfigureAndRunBackgroundJobs(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefConfigureAndRunBackgroundJobs'
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
    print(ScheduledBriefConfigureAndRunBackgroundJobs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
