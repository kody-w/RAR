---
name: "rar-cowork-cookbook-scheduled-brief-update-access-to-systems"
description: "Schedulable morning-brief email summarizing update access to systems for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_update_access_to_systems", "rar_sha256": "6e2dfdd825e8920daf3d2bfbe65a605bbd30a9ec5951278551e6b2581a5b35e7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_update_access_to_systems_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-update-access-to-systems:98d2741cea7fcc2eb2eb6c225755f21be78c1ba7203f66888a1bfe34ec5eeebf", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_update_access_to_systems`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_update_access_to_systems_agent.py` is
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

Update access to systems Scheduled Email Brief — Schedulable morning-brief email summarizing update access to systems for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-update-access-to-systems
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_update_access_to_systems_agent.py` and embedded as the fenced Python below (sha256 6e2dfdd825e8920d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_update_access_to_systems_agent.py` first:

```bash
python3 scheduled_brief_update_access_to_systems_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_update_access_to_systems_agent.py   # or on stdin
python3 scheduled_brief_update_access_to_systems_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Update access to systems Scheduled Email Brief — Schedulable morning-brief email summarizing update access to systems for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-update-access-to-systems
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_update_access_to_systems',
    "version": '2.0.0',
    "display_name": 'Update access to systems Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing update access to systems for the responsible owner; designed to run daily or weekly.',
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
        "upstream_slug": 'scheduled-brief-update-access-to-systems',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-update-access-to-systems',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '09ad37fd3a260daf',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/update-access-to-systems'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-update-access-to-systems', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefUpdateAccessToSystems(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefUpdateAccessToSystems'
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
    print(ScheduledBriefUpdateAccessToSystems().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
