---
name: "rar-cowork-cookbook-scheduled-brief-manage-funds"
description: "Schedulable morning-brief email summarizing manage funds for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_manage_funds", "rar_sha256": "3ad34907a79b8319267d050eb81791dc4c9135675f719668f4e0ee64c5057854", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_manage_funds`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_manage_funds_agent.py` and in the RCI capsule.

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
