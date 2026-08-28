---
name: "rar-cowork-cookbook-analyst-briefing-prep-and-rehearsal-routing"
description: "Prep the [Analyst Firm] briefing package and get the team rehearsed before the room."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/analyst_briefing_prep_and_rehearsal_routing", "rar_sha256": "c15079a0eb67462441949ecec022bddb9373120c7d7a84e9247f363008e11386", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "concept_to_market", "advanced", "read_only", "automation"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/analyst_briefing_prep_and_rehearsal_routing`. The original RAPP
agent is preserved byte-for-byte in `analyst_briefing_prep_and_rehearsal_routing_agent.py` and in the RCI capsule.

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

Analyst briefing prep and rehearsal routing — Prep the [Analyst Firm] briefing package and get the team rehearsed before the room.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/analyst-briefing-prep-and-rehearsal-routing
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `analyst_briefing_prep_and_rehearsal_routing_agent.py` and embedded as the fenced Python below (sha256 c15079a0eb674624…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `analyst_briefing_prep_and_rehearsal_routing_agent.py` first:

```bash
python3 analyst_briefing_prep_and_rehearsal_routing_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 analyst_briefing_prep_and_rehearsal_routing_agent.py   # or on stdin
python3 analyst_briefing_prep_and_rehearsal_routing_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyst briefing prep and rehearsal routing — Prep the [Analyst Firm] briefing package and get the team rehearsed before the room.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/analyst-briefing-prep-and-rehearsal-routing
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/analyst_briefing_prep_and_rehearsal_routing',
    "version": '2.0.1',
    "display_name": 'Analyst briefing prep and rehearsal routing',
    "description": 'Prep the [Analyst Firm] briefing package and get the team rehearsed before the room.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'concept_to_market', 'advanced', 'read_only', 'automation'],
    "category": 'general',
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
        "upstream_slug": 'analyst-briefing-prep-and-rehearsal-routing',
        "upstream_url": 'https://coworkcookbook.com/recipes/analyst-briefing-prep-and-rehearsal-routing',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '033e08f333f9f0e2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'none', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/develop-marketing-strategy/define-value-proposition'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/analyst-briefing-prep-and-rehearsal-routing', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Calendar Management', 'Meetings'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AnalystBriefingPrepAndRehearsalRouting(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AnalystBriefingPrepAndRehearsalRouting'
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
    print(AnalystBriefingPrepAndRehearsalRouting().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
