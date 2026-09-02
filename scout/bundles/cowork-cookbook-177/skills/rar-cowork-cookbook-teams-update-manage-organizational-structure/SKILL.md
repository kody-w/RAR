---
name: "rar-cowork-cookbook-teams-update-manage-organizational-structure"
description: "Drafts a Teams channel post on manage organizational structure status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_manage_organizational_structure", "rar_sha256": "5ef35c18f3c33095313bd60e00b1fc109dfe966a243f8bb67e173f508991214b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_manage_organizational_structure_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-manage-organizational-structure:bae98b50a41a1bd1471772be2d517b4bb297cb6fa1f481742282bfcc54e919ac", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_manage_organizational_structure`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_manage_organizational_structure_agent.py` is
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
