---
name: "rar-cowork-cookbook-scheduled-brief-manage-funds"
description: "Schedulable morning-brief email summarizing manage funds for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_manage_funds", "rar_sha256": "3ad34907a79b8319267d050eb81791dc4c9135675f719668f4e0ee64c5057854", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_manage_funds_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-manage-funds:1b56f51e5b490ac0a43a29f7154a86941acb5180cc2971dc4c149812da42b480", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_manage_funds`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_manage_funds_agent.py` is
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

Manage funds Scheduled Email Brief — Schedulable morning-brief email summarizing manage funds for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-funds
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_manage_funds_agent.py` and embedded as the fenced Python below (sha256 3ad34907a79b8319…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_manage_funds_agent.py` first:

```bash
python3 scheduled_brief_manage_funds_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_manage_funds_agent.py   # or on stdin
python3 scheduled_brief_manage_funds_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage funds Scheduled Email Brief — Schedulable morning-brief email summarizing manage funds for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-funds
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_manage_funds',
    "version": '2.0.0',
    "display_name": 'Manage funds Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing manage funds for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'scheduled-brief-manage-funds',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-manage-funds',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8902ce6b0873f094',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-cash/manage-funds'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/scheduled-brief-manage-funds', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class ScheduledBriefManageFunds(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefManageFunds'
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
    print(ScheduledBriefManageFunds().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
