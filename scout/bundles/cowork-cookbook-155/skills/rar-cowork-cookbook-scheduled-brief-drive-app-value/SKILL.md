---
name: "rar-cowork-cookbook-scheduled-brief-drive-app-value"
description: "Schedulable morning-brief email summarizing drive app value for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_drive_app_value", "rar_sha256": "b6f6571bf5d44684e0b96858fbad1193c716c79b7061c1b00565f41677ad0291", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_drive_app_value_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-drive-app-value:ed8a24ec0298c1dca4ae76b3c2e55ff322fa22292ce524b43bf09ec2f190b568", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_drive_app_value`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_drive_app_value_agent.py` is
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

Drive app value Scheduled Email Brief — Schedulable morning-brief email summarizing drive app value for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-drive-app-value
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_drive_app_value_agent.py` and embedded as the fenced Python below (sha256 b6f6571bf5d44684…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_drive_app_value_agent.py` first:

```bash
python3 scheduled_brief_drive_app_value_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_drive_app_value_agent.py   # or on stdin
python3 scheduled_brief_drive_app_value_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Drive app value Scheduled Email Brief — Schedulable morning-brief email summarizing drive app value for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-drive-app-value
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_drive_app_value',
    "version": '2.0.0',
    "display_name": 'Drive app value Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing drive app value for the responsible owner; designed to run daily or weekly.',
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
        "upstream_slug": 'scheduled-brief-drive-app-value',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-drive-app-value',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7e9f29ad0505c9f8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/drive-app-value'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-drive-app-value', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefDriveAppValue(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDriveAppValue'
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
    print(ScheduledBriefDriveAppValue().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
