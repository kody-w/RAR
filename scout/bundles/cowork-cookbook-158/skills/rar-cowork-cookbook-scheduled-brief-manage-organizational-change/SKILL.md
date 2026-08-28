---
name: "rar-cowork-cookbook-scheduled-brief-manage-organizational-change"
description: "Schedulable morning-brief email summarizing manage organizational change for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_manage_organizational_change", "rar_sha256": "8bec17e19bd0eb0691ffc5340884c74e8daa3f4e1e9cd877203e7d37a0a6afc6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_manage_organizational_change`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_manage_organizational_change_agent.py` and in the RCI capsule.

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

Manage organizational change Scheduled Email Brief — Schedulable morning-brief email summarizing manage organizational change for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-organizational-change
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_manage_organizational_change_agent.py` and embedded as the fenced Python below (sha256 8bec17e19bd0eb06…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_manage_organizational_change_agent.py` first:

```bash
python3 scheduled_brief_manage_organizational_change_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_manage_organizational_change_agent.py   # or on stdin
python3 scheduled_brief_manage_organizational_change_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage organizational change Scheduled Email Brief — Schedulable morning-brief email summarizing manage organizational change for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-organizational-change
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_manage_organizational_change',
    "version": '2.0.0',
    "display_name": 'Manage organizational change Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing manage organizational change for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-manage-organizational-change',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-manage-organizational-change',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '88fc4b75c49a88f0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/manage-organizational-change'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-manage-organizational-change', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefManageOrganizationalChange(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefManageOrganizationalChange'
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
    print(ScheduledBriefManageOrganizationalChange().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
