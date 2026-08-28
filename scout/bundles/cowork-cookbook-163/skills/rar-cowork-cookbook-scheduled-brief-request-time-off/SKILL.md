---
name: "rar-cowork-cookbook-scheduled-brief-request-time-off"
description: "Schedulable morning-brief email summarizing request time off for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_request_time_off", "rar_sha256": "e19d687505463d849c0051980c34721f2c4896b417e09e9a5b28bf7469df2b3d", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_request_time_off`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_request_time_off_agent.py` and in the RCI capsule.

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

Request time off Scheduled Email Brief — Schedulable morning-brief email summarizing request time off for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-request-time-off
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_request_time_off_agent.py` and embedded as the fenced Python below (sha256 e19d687505463d84…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_request_time_off_agent.py` first:

```bash
python3 scheduled_brief_request_time_off_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_request_time_off_agent.py   # or on stdin
python3 scheduled_brief_request_time_off_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Request time off Scheduled Email Brief — Schedulable morning-brief email summarizing request time off for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-request-time-off
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_request_time_off',
    "version": '2.0.1',
    "display_name": 'Request time off Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing request time off for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-request-time-off',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-request-time-off',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c24dd87bc49b0624',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-time-and-attendance/request-time-off'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/scheduled-brief-request-time-off', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefRequestTimeOff(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefRequestTimeOff'
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
    print(ScheduledBriefRequestTimeOff().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
