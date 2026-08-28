---
name: "rar-cowork-cookbook-ppt-exec-perform-service-tasks"
description: "Generates an executive-ready PowerPoint deck on perform service tasks status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_perform_service_tasks", "rar_sha256": "04f04f41b9976dd86ae041a771735e16cf7b300e4eb28546225cce988803a9d1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_perform_service_tasks`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_perform_service_tasks_agent.py` and in the RCI capsule.

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
