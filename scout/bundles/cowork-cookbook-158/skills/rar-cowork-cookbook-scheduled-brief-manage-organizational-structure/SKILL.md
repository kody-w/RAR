---
name: "rar-cowork-cookbook-scheduled-brief-manage-organizational-structure"
description: "Schedulable morning-brief email summarizing manage organizational structure for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_manage_organizational_structure", "rar_sha256": "943e0c9297c22a9984cf91954902e2c8c62bb33a0b3bcd25e76638184b664e46", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_manage_organizational_structure_agent.py` and embedded as the fenced Python below (sha256 943e0c9297c22a99…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_manage_organizational_structure_agent.py` first:

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
    "version": '2.0.1',
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
