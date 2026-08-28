---
name: "rar-cowork-cookbook-scheduled-brief-configure-and-run-background-jobs"
description: "Schedulable morning-brief email summarizing configure and run background jobs for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_configure_and_run_background_jobs", "rar_sha256": "85a0c5df39cb9d06a72df6d33713076fb12e3546a6f5ddd6d10ba1d5fe032f1f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_configure_and_run_background_jobs`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_configure_and_run_background_jobs_agent.py` and in the RCI capsule.

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
