---
name: "rar-cowork-cookbook-teams-update-drive-app-value"
description: "Drafts a Teams channel post on drive app value status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_drive_app_value", "rar_sha256": "993d6a393b40ca1b24a1d5761900ccd160908fe1ab8b1d8e53ca19ec9c982b8b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_drive_app_value_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-drive-app-value:b3ec96a243d5dd5d3eab6bb8d5c5ea72899f2ce9fc71907d68bb86136d379df3", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_drive_app_value`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_drive_app_value_agent.py` is
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

Drive app value Teams Channel Update — Drafts a Teams channel post on drive app value status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-drive-app-value
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_drive_app_value_agent.py` and embedded as the fenced Python below (sha256 993d6a393b40ca1b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_drive_app_value_agent.py` first:

```bash
python3 teams_update_drive_app_value_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_drive_app_value_agent.py   # or on stdin
python3 teams_update_drive_app_value_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Drive app value Teams Channel Update — Drafts a Teams channel post on drive app value status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-drive-app-value
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_drive_app_value',
    "version": '2.0.0',
    "display_name": 'Drive app value Teams Channel Update',
    "description": 'Drafts a Teams channel post on drive app value status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-drive-app-value',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-drive-app-value',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '89ed03b73078caf8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/drive-app-value'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-drive-app-value', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateDriveAppValue(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDriveAppValue'
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
    print(TeamsUpdateDriveAppValue().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
