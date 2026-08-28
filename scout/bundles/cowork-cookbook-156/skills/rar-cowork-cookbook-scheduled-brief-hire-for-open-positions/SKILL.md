---
name: "rar-cowork-cookbook-scheduled-brief-hire-for-open-positions"
description: "Schedulable morning-brief email summarizing hire for open positions for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_hire_for_open_positions", "rar_sha256": "c757053b2b580e89517702c7549d637e29c4e99ac9e2606bbd002748bf446538", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_hire_for_open_positions`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_hire_for_open_positions_agent.py` and in the RCI capsule.

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

Hire for open positions Scheduled Email Brief — Schedulable morning-brief email summarizing hire for open positions for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-hire-for-open-positions
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_hire_for_open_positions_agent.py` and embedded as the fenced Python below (sha256 c757053b2b580e89…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_hire_for_open_positions_agent.py` first:

```bash
python3 scheduled_brief_hire_for_open_positions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_hire_for_open_positions_agent.py   # or on stdin
python3 scheduled_brief_hire_for_open_positions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Hire for open positions Scheduled Email Brief — Schedulable morning-brief email summarizing hire for open positions for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-hire-for-open-positions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_hire_for_open_positions',
    "version": '2.0.1',
    "display_name": 'Hire for open positions Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing hire for open positions for the responsible owner; designed to run daily or weekly.',
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
        "upstream_slug": 'scheduled-brief-hire-for-open-positions',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-hire-for-open-positions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'eb4c64c81733158f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/recruit-and-onboard-talent/hire-for-open-positions'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/scheduled-brief-hire-for-open-positions', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefHireForOpenPositions(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefHireForOpenPositions'
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
    print(ScheduledBriefHireForOpenPositions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
