---
name: "rar-cowork-cookbook-scheduled-brief-request-time-off"
description: "Schedulable morning-brief email summarizing request time off for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_request_time_off", "rar_sha256": "a709e01ab5a3c9b9802df3ee613b104b9a7cb31633375402e06923e1a219861e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_request_time_off_agent.py` and embedded as the fenced Python below (sha256 a709e01ab5a3c9b9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_request_time_off_agent.py` first:

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
    "version": '2.0.0',
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
