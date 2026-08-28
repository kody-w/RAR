---
name: "rar-cowork-cookbook-teams-update-drive-app-value"
description: "Drafts a Teams channel post on drive app value status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_drive_app_value", "rar_sha256": "fbc4a457733491c1b70948571d1cf466af4962d186019d7c6fc47bdc43026695", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_drive_app_value`. The original RAPP
agent is preserved byte-for-byte in `teams_update_drive_app_value_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_drive_app_value_agent.py` and embedded as the fenced Python below (sha256 fbc4a457733491c1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_drive_app_value_agent.py` first:

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
    "version": '2.0.1',
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
