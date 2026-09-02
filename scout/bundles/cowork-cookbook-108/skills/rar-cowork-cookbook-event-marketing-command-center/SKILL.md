---
name: "rar-cowork-cookbook-event-marketing-command-center"
description: "Prep every moment of [Event name] - speaker slots, customer meetings, content drops, social posts - and bring it together in a single interactive command center with live event KPIs."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/event_marketing_command_center", "rar_sha256": "bf5e15f1e4eccb2d938c9ad2d28037fc7642baee0b16f13a3174964eeb349e79", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "event_marketing_command_center_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/event-marketing-command-center:79b14f26e0600a48e6b926156449738a26d5863ab200d74b52f91ee56c7ef130", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "advanced", "integration", "fabric_iq"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/event_marketing_command_center`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `event_marketing_command_center_agent.py` is
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
