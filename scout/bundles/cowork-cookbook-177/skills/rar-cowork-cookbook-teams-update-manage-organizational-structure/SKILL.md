---
name: "rar-cowork-cookbook-teams-update-manage-organizational-structure"
description: "Drafts a Teams channel post on manage organizational structure status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_manage_organizational_structure", "rar_sha256": "5ef35c18f3c33095313bd60e00b1fc109dfe966a243f8bb67e173f508991214b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_manage_organizational_structure_agent.py` and embedded as the fenced Python below (sha256 5ef35c18f3c33095…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_manage_organizational_structure_agent.py` first:

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
    "version": '2.0.0',
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
