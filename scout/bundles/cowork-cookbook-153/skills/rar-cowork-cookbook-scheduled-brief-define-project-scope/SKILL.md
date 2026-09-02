---
name: "rar-cowork-cookbook-scheduled-brief-define-project-scope"
description: "Schedulable morning-brief email summarizing define project scope for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_project_scope", "rar_sha256": "179b66b69ba7896b8bd4b847610b99a851b4140c41719acd6f743e3ccaea62ac", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_define_project_scope_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-define-project-scope:f2051fd6a0e10dc38c35f759c193d620291d130779da6756480ca3955a46823f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_define_project_scope`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_define_project_scope_agent.py` is
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
