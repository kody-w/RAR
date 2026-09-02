---
name: "rar-cowork-cookbook-scheduled-brief-manage-organizational-change"
description: "Schedulable morning-brief email summarizing manage organizational change for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_manage_organizational_change", "rar_sha256": "8bec17e19bd0eb0691ffc5340884c74e8daa3f4e1e9cd877203e7d37a0a6afc6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_manage_organizational_change_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-manage-organizational-change:6f67fcdd2ca81251fa04116f4045516b4f0a9a55c5bdb0487ca6483cc53e934f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_manage_organizational_change`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_manage_organizational_change_agent.py` is
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

Manage organizational change Scheduled Email Brief — Schedulable morning-brief email summarizing manage organizational change for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-organizational-change
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_manage_organizational_change_agent.py` and embedded as the fenced Python below (sha256 8bec17e19bd0eb06…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_manage_organizational_change_agent.py` first:

```bash
python3 scheduled_brief_manage_organizational_change_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_manage_organizational_change_agent.py   # or on stdin
python3 scheduled_brief_manage_organizational_change_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage organizational change Scheduled Email Brief — Schedulable morning-brief email summarizing manage organizational change for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-organizational-change
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_manage_organizational_change',
    "version": '2.0.0',
    "display_name": 'Manage organizational change Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing manage organizational change for the responsible owner; designed to run daily or weekly.',
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
        "upstream_slug": 'scheduled-brief-manage-organizational-change',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-manage-organizational-change',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '88fc4b75c49a88f0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/manage-organizational-change'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-manage-organizational-change', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefManageOrganizationalChange(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefManageOrganizationalChange'
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
    print(ScheduledBriefManageOrganizationalChange().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
