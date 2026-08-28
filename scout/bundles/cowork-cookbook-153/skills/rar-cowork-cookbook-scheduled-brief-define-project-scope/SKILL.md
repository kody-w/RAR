---
name: "rar-cowork-cookbook-scheduled-brief-define-project-scope"
description: "Schedulable morning-brief email summarizing define project scope for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_project_scope", "rar_sha256": "179b66b69ba7896b8bd4b847610b99a851b4140c41719acd6f743e3ccaea62ac", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_define_project_scope_agent.py` and embedded as the fenced Python below (sha256 179b66b69ba7896b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_define_project_scope_agent.py` first:

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
    "version": '2.0.0',
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
