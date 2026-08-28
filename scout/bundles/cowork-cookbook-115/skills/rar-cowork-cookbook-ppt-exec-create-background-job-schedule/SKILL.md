---
name: "rar-cowork-cookbook-ppt-exec-create-background-job-schedule"
description: "Generates an executive-ready PowerPoint deck on create background job schedule status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_create_background_job_schedule", "rar_sha256": "48aabe8c4c7518b0615d3dbc5c7f0807b1d548c22d6ed2b8dd02cc3f3b8e9d00", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_create_background_job_schedule`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_create_background_job_schedule_agent.py` and in the RCI capsule.

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

Create background job schedule Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on create background job schedule status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-create-background-job-schedule
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_create_background_job_schedule_agent.py` and embedded as the fenced Python below (sha256 48aabe8c4c7518b0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_create_background_job_schedule_agent.py` first:

```bash
python3 ppt_exec_create_background_job_schedule_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_create_background_job_schedule_agent.py   # or on stdin
python3 ppt_exec_create_background_job_schedule_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create background job schedule Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on create background job schedule status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-create-background-job-schedule
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_create_background_job_schedule',
    "version": '2.0.1',
    "display_name": 'Create background job schedule Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on create background job schedule status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-create-background-job-schedule',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-create-background-job-schedule',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2a6fa6491e8d38c4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-background-jobs/create-background-job-schedule'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-create-background-job-schedule', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.75, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'word:schedule'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecCreateBackgroundJobSchedule(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecCreateBackgroundJobSchedule'
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
    print(PptExecCreateBackgroundJobSchedule().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
