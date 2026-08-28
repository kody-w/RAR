---
name: "rar-cowork-cookbook-teams-update-drive-app-value"
description: "Drafts a Teams channel post on drive app value status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_drive_app_value", "rar_sha256": "993d6a393b40ca1b24a1d5761900ccd160908fe1ab8b1d8e53ca19ec9c982b8b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
