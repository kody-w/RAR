---
name: "rar-cowork-cookbook-scheduled-brief-define-project-scope"
description: "Schedulable morning-brief email summarizing define project scope for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_project_scope", "rar_sha256": "fa81889ff89903d506764fab2cedd2286a48059e761251a3b0f9efad7e9fb43f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_define_project_scope`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_define_project_scope_agent.py` and in the RCI capsule.

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

Define project scope Scheduled Email Brief — Schedulable morning-brief email summarizing define project scope for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-project-scope
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_define_project_scope_agent.py` and embedded as the fenced Python below (sha256 fa81889ff89903d5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_define_project_scope_agent.py` first:

```bash
python3 scheduled_brief_define_project_scope_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_define_project_scope_agent.py   # or on stdin
python3 scheduled_brief_define_project_scope_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define project scope Scheduled Email Brief — Schedulable morning-brief email summarizing define project scope for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-project-scope
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_define_project_scope',
    "version": '2.0.1',
    "display_name": 'Define project scope Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing define project scope for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-define-project-scope',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-define-project-scope',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e1ef7c75ca308a88',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/plan-projects/define-project-scope'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/scheduled-brief-define-project-scope', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefDefineProjectScope(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDefineProjectScope'
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
    print(ScheduledBriefDefineProjectScope().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
