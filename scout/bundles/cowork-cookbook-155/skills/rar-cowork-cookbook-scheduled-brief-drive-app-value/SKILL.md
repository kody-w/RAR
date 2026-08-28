---
name: "rar-cowork-cookbook-scheduled-brief-drive-app-value"
description: "Schedulable morning-brief email summarizing drive app value for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_drive_app_value", "rar_sha256": "b6f6571bf5d44684e0b96858fbad1193c716c79b7061c1b00565f41677ad0291", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_drive_app_value`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_drive_app_value_agent.py` and in the RCI capsule.

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
