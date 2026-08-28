---
name: "rar-cowork-cookbook-teams-update-manage-organizational-structure"
description: "Drafts a Teams channel post on manage organizational structure status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_manage_organizational_structure", "rar_sha256": "a926222d757ff86bb4405f92c8ec992166fa8afd49cbe2fda4b831a9b16ab225", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_manage_organizational_structure`. The original RAPP
agent is preserved byte-for-byte in `teams_update_manage_organizational_structure_agent.py` and in the RCI capsule.

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

Manage organizational structure Teams Channel Update — Drafts a Teams channel post on manage organizational structure status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-manage-organizational-structure
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_manage_organizational_structure_agent.py` and embedded as the fenced Python below (sha256 a926222d757ff86b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_manage_organizational_structure_agent.py` first:

```bash
python3 teams_update_manage_organizational_structure_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_manage_organizational_structure_agent.py   # or on stdin
python3 teams_update_manage_organizational_structure_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage organizational structure Teams Channel Update — Drafts a Teams channel post on manage organizational structure status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-manage-organizational-structure
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_manage_organizational_structure',
    "version": '2.0.1',
    "display_name": 'Manage organizational structure Teams Channel Update',
    "description": 'Drafts a Teams channel post on manage organizational structure status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-manage-organizational-structure',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-manage-organizational-structure',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '80c12d390d5502a1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/manage-organizational-structure'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-manage-organizational-structure', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateManageOrganizationalStructure(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateManageOrganizationalStructure'
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
    print(TeamsUpdateManageOrganizationalStructure().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
