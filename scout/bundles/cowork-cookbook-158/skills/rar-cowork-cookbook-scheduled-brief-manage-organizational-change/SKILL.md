---
name: "rar-cowork-cookbook-scheduled-brief-manage-organizational-change"
description: "Schedulable morning-brief email summarizing manage organizational change for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_manage_organizational_change", "rar_sha256": "1f53561da71a9841d290fc5b49baeb8c8911312d9acde4a87dafa322bdd8b073", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_manage_organizational_change_agent.py` and embedded as the fenced Python below (sha256 1f53561da71a9841…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_manage_organizational_change_agent.py` first:

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
    "version": '2.0.1',
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
