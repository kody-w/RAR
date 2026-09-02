---
name: "rar-cowork-cookbook-ppt-exec-perform-service-tasks"
description: "Generates an executive-ready PowerPoint deck on perform service tasks status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_perform_service_tasks", "rar_sha256": "04f04f41b9976dd86ae041a771735e16cf7b300e4eb28546225cce988803a9d1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_perform_service_tasks_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-perform-service-tasks:45ac1058b1b490e38fcf2f8536a0fdc14313893ce8bbe4c2d48e713f785eb718", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_perform_service_tasks`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_perform_service_tasks_agent.py` is
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

Perform service tasks Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on perform service tasks status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-perform-service-tasks
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_perform_service_tasks_agent.py` and embedded as the fenced Python below (sha256 04f04f41b9976dd8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_perform_service_tasks_agent.py` first:

```bash
python3 ppt_exec_perform_service_tasks_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_perform_service_tasks_agent.py   # or on stdin
python3 ppt_exec_perform_service_tasks_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Perform service tasks Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on perform service tasks status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-perform-service-tasks
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_perform_service_tasks',
    "version": '2.0.0',
    "display_name": 'Perform service tasks Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on perform service tasks status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-perform-service-tasks',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-perform-service-tasks',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6e36b0918ce218e3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/perform-service-tasks'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/ppt-exec-perform-service-tasks', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecPerformServiceTasks(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecPerformServiceTasks'
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
    print(PptExecPerformServiceTasks().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
