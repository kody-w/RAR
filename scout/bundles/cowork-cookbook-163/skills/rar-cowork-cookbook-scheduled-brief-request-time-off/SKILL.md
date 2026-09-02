---
name: "rar-cowork-cookbook-scheduled-brief-request-time-off"
description: "Schedulable morning-brief email summarizing request time off for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_request_time_off", "rar_sha256": "a709e01ab5a3c9b9802df3ee613b104b9a7cb31633375402e06923e1a219861e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_request_time_off_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-request-time-off:8dc8ad143f990e07a35a645b52e4096c919be4d55c3f7cb17c3d6967d9ba9963", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_request_time_off`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_request_time_off_agent.py` is
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
