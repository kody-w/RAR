---
name: "rar-cowork-cookbook-ppt-exec-create-and-schedule-services"
description: "Generates an executive-ready PowerPoint deck on create and schedule services status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_create_and_schedule_services", "rar_sha256": "02616c19b19809367f51329fb06d20429c48f986788cafc1733e7228ba417d11", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_create_and_schedule_services`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_create_and_schedule_services_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_create_and_schedule_services_agent.py` and embedded as the fenced Python below (sha256 02616c19b1980936…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_create_and_schedule_services_agent.py` first:

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
    "version": '2.0.1',
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
