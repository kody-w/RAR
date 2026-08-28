---
name: "rar-cowork-cookbook-ppt-exec-create-background-job-schedule"
description: "Generates an executive-ready PowerPoint deck on create background job schedule status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_create_background_job_schedule", "rar_sha256": "ced8fd8b0c78953598ac8af616aff095ab4d51fc8eb6dea8fe1347f04688f921", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_create_background_job_schedule_agent.py` and embedded as the fenced Python below (sha256 ced8fd8b0c789535…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_create_background_job_schedule_agent.py` first:

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
    "version": '2.0.0',
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
