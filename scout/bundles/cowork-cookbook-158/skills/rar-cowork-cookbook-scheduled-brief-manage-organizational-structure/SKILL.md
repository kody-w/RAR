---
name: "rar-cowork-cookbook-scheduled-brief-manage-organizational-structure"
description: "Schedulable morning-brief email summarizing manage organizational structure for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_manage_organizational_structure", "rar_sha256": "627a892d1b07ffa92ed562971fc3b0d0a9c213095220f96be0d8f36d8941d0a4", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_manage_organizational_structure_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-manage-organizational-structure:f3dcde001178e3bf5be7eda310f3adcd60b1b69a649a4ed222ccc026a4da174f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_manage_organizational_structure`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_manage_organizational_structure_agent.py` is
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

Manage organizational structure Scheduled Email Brief — Schedulable morning-brief email summarizing manage organizational structure for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-organizational-structure
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_manage_organizational_structure_agent.py` and embedded as the fenced Python below (sha256 627a892d1b07ffa9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_manage_organizational_structure_agent.py` first:

```bash
python3 scheduled_brief_manage_organizational_structure_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_manage_organizational_structure_agent.py   # or on stdin
python3 scheduled_brief_manage_organizational_structure_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage organizational structure Scheduled Email Brief — Schedulable morning-brief email summarizing manage organizational structure for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-organizational-structure
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_manage_organizational_structure',
    "version": '2.0.0',
    "display_name": 'Manage organizational structure Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing manage organizational structure for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-manage-organizational-structure',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-manage-organizational-structure',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2b5b81021ceeb8cf',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/manage-organizational-structure'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-manage-organizational-structure', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefManageOrganizationalStructure(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefManageOrganizationalStructure'
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
    print(ScheduledBriefManageOrganizationalStructure().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
