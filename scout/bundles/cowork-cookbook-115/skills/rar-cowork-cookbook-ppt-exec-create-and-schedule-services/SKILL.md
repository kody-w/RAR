---
name: "rar-cowork-cookbook-ppt-exec-create-and-schedule-services"
description: "Generates an executive-ready PowerPoint deck on create and schedule services status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_create_and_schedule_services", "rar_sha256": "82afe041fdbde13d7834fb29427a2682f7d2c22a84312be42fe8d917544b8b64", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_create_and_schedule_services_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-create-and-schedule-services:425205248464d72f46fc2523f9a92c5eea6986a4c1aec9bd96ce60360364671d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_create_and_schedule_services`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_create_and_schedule_services_agent.py` is
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

Create and schedule services Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on create and schedule services status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-create-and-schedule-services
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_create_and_schedule_services_agent.py` and embedded as the fenced Python below (sha256 82afe041fdbde13d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_create_and_schedule_services_agent.py` first:

```bash
python3 ppt_exec_create_and_schedule_services_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_create_and_schedule_services_agent.py   # or on stdin
python3 ppt_exec_create_and_schedule_services_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create and schedule services Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on create and schedule services status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-create-and-schedule-services
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_create_and_schedule_services',
    "version": '2.0.0',
    "display_name": 'Create and schedule services Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on create and schedule services status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-create-and-schedule-services',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-create-and-schedule-services',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7bb80887290479c2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/create-and-schedule-services'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/ppt-exec-create-and-schedule-services', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecCreateAndScheduleServices(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecCreateAndScheduleServices'
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
    print(PptExecCreateAndScheduleServices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
