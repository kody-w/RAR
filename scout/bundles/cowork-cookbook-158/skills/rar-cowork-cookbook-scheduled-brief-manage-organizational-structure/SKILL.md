---
name: "rar-cowork-cookbook-scheduled-brief-manage-organizational-structure"
description: "Schedulable morning-brief email summarizing manage organizational structure for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_manage_organizational_structure", "rar_sha256": "627a892d1b07ffa92ed562971fc3b0d0a9c213095220f96be0d8f36d8941d0a4", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_manage_organizational_structure`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_manage_organizational_structure_agent.py` and in the RCI capsule.

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

Manage organizational structure Scheduled Email Brief — Schedulable morning-brief email summarizing manage organizational structure for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-organizational-structure
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_manage_organizational_structure_agent.py` and embedded as the fenced Python below (sha256 627a892d1b07ffa9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_manage_organizational_structure_agent.py` first:

```bash
python3 scheduled_brief_manage_organizational_structure_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_manage_organizational_structure_agent.py   # or on stdin
python3 scheduled_brief_manage_organizational_structure_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage organizational structure Scheduled Email Brief — Schedulable morning-brief email summarizing manage organizational structure for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-organizational-structure
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_manage_organizational_structure',
    "version": '2.0.0',
    "display_name": 'Manage organizational structure Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing manage organizational structure for the responsible owner; designed to run daily or weekly.',
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
        "upstream_slug": 'scheduled-brief-manage-organizational-structure',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-manage-organizational-structure',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2b5b81021ceeb8cf',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/manage-organizational-structure'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-manage-organizational-structure', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefManageOrganizationalStructure(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefManageOrganizationalStructure'
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
    print(ScheduledBriefManageOrganizationalStructure().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
