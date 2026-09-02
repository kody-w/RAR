---
name: "rar-cowork-cookbook-scheduled-brief-hire-for-open-positions"
description: "Schedulable morning-brief email summarizing hire for open positions for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_hire_for_open_positions", "rar_sha256": "4d329b2fed0635c9d70dc2c3e61781bc2439adea57c29cee2d1d3f0a2938c1b2", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_hire_for_open_positions_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-hire-for-open-positions:eb7867f1090a87f7fde5f4564af95b1e35fe9d13be808623ea30758144b4e7b7", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_hire_for_open_positions`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_hire_for_open_positions_agent.py` is
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
