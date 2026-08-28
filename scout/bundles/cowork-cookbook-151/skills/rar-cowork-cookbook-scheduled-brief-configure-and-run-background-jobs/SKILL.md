---
name: "rar-cowork-cookbook-scheduled-brief-configure-and-run-background-jobs"
description: "Schedulable morning-brief email summarizing configure and run background jobs for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_configure_and_run_background_jobs", "rar_sha256": "e2efebf6f850db8ed5103b557f58e26b088c034172a333033b2ba0ea4bb17144", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_configure_and_run_background_jobs_agent.py` and embedded as the fenced Python below (sha256 e2efebf6f850db8e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_configure_and_run_background_jobs_agent.py` first:

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
    "version": '2.0.1',
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
