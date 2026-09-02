---
name: "rar-cowork-cookbook-ppt-exec-create-background-job-schedule"
description: "Generates an executive-ready PowerPoint deck on create background job schedule status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_create_background_job_schedule", "rar_sha256": "ced8fd8b0c78953598ac8af616aff095ab4d51fc8eb6dea8fe1347f04688f921", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_create_background_job_schedule_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-create-background-job-schedule:0a0e5b3fad49686702dab518b61b8135ff8241f520eef0ea36ab6d6b43afb411", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_create_background_job_schedule`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_create_background_job_schedule_agent.py` is
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
