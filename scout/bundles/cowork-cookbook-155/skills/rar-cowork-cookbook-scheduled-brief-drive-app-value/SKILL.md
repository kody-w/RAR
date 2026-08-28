---
name: "rar-cowork-cookbook-scheduled-brief-drive-app-value"
description: "Schedulable morning-brief email summarizing drive app value for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_drive_app_value", "rar_sha256": "3b5ca74124eb8296ad89c66216ced28a78ed5fff9b85b7edb005bebc5d2281b6", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_drive_app_value_agent.py` and embedded as the fenced Python below (sha256 3b5ca74124eb8296…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_drive_app_value_agent.py` first:

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
    "version": '2.0.1',
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
