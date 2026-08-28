---
name: "rar-cowork-cookbook-scheduled-brief-hire-for-open-positions"
description: "Schedulable morning-brief email summarizing hire for open positions for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_hire_for_open_positions", "rar_sha256": "4d329b2fed0635c9d70dc2c3e61781bc2439adea57c29cee2d1d3f0a2938c1b2", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_hire_for_open_positions_agent.py` and embedded as the fenced Python below (sha256 4d329b2fed0635c9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_hire_for_open_positions_agent.py` first:

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
    "version": '2.0.0',
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
