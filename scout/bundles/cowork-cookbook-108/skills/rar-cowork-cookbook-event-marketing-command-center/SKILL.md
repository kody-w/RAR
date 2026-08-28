---
name: "rar-cowork-cookbook-event-marketing-command-center"
description: "Prep every moment of [Event name] - speaker slots, customer meetings, content drops, social posts - and bring it together in a single interactive command center with live event KPIs."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/event_marketing_command_center", "rar_sha256": "3ae2822fdcb439aa300d42b1151f869dc636721e42e9d2705077051d29fbc2fa", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "advanced", "integration", "fabric_iq"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `event_marketing_command_center_agent.py` and embedded as the fenced Python below (sha256 3ae2822fdcb439aa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `event_marketing_command_center_agent.py` first:

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
    "version": '2.0.1',
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
