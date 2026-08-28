---
name: "rar-cowork-cookbook-ppt-exec-perform-service-tasks"
description: "Generates an executive-ready PowerPoint deck on perform service tasks status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_perform_service_tasks", "rar_sha256": "dc91239e67ab47abc33e22820e105f1545f78ddce8fcf157770b137bcd32cbac", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_perform_service_tasks_agent.py` and embedded as the fenced Python below (sha256 dc91239e67ab47ab…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_perform_service_tasks_agent.py` first:

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
    "version": '2.0.1',
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
