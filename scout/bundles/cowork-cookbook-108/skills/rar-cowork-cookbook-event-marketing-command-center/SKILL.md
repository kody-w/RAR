---
name: "rar-cowork-cookbook-event-marketing-command-center"
description: "Prep every moment of [Event name] - speaker slots, customer meetings, content drops, social posts - and bring it together in a single interactive command center with live event KPIs."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/event_marketing_command_center", "rar_sha256": "bf5e15f1e4eccb2d938c9ad2d28037fc7642baee0b16f13a3174964eeb349e79", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "advanced", "integration", "fabric_iq"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/event_marketing_command_center`. The original RAPP
agent is preserved byte-for-byte in `event_marketing_command_center_agent.py` and in the RCI capsule.

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

Event marketing command center — Prep every moment of [Event name] - speaker slots, customer meetings, content drops, social posts - and bring it together in a single interactive command center with live event KPIs.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/event-marketing-command-center
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `event_marketing_command_center_agent.py` and embedded as the fenced Python below (sha256 bf5e15f1e4eccb2d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `event_marketing_command_center_agent.py` first:

```bash
python3 event_marketing_command_center_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 event_marketing_command_center_agent.py   # or on stdin
python3 event_marketing_command_center_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Event marketing command center — Prep every moment of [Event name] - speaker slots, customer meetings, content drops, social posts - and bring it together in a single interactive command center with live event KPIs.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/event-marketing-command-center
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/event_marketing_command_center',
    "version": '2.0.0',
    "display_name": 'Event marketing command center',
    "description": 'Prep every moment of [Event name] - speaker slots, customer meetings, content drops, social posts - and bring it together in a single interactive command center with live event KPIs.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'concept_to_market', 'advanced', 'integration', 'fabric_iq'],
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
        "upstream_slug": 'event-marketing-command-center',
        "upstream_url": 'https://coworkcookbook.com/recipes/event-marketing-command-center',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '49c0820930fe9aa0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'fabric-iq', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/plan-events'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/event-marketing-command-center', 'uses_skills': {'custom': [], 'ootb': ['Word', 'PowerPoint', 'Email', 'Calendar Management', 'Meetings'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class EventMarketingCommandCenter(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'EventMarketingCommandCenter'
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
    print(EventMarketingCommandCenter().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
