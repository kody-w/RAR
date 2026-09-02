---
name: "rar-cowork-cookbook-teams-update-project-inventory-levels"
description: "Drafts a Teams channel post on project inventory levels status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_project_inventory_levels", "rar_sha256": "a3e6313e1698d86e3200c7df09d500030c2434e29c350dc6a84bff39f548dfa9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_project_inventory_levels_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-project-inventory-levels:af657946abb27a260f9e5996dc3c306e11826e465e6c8a8c70356ee8c958a7ec", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_project_inventory_levels`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_project_inventory_levels_agent.py` is
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

Project inventory levels Teams Channel Update — Drafts a Teams channel post on project inventory levels status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-project-inventory-levels
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_project_inventory_levels_agent.py` and embedded as the fenced Python below (sha256 a3e6313e1698d86e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_project_inventory_levels_agent.py` first:

```bash
python3 teams_update_project_inventory_levels_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_project_inventory_levels_agent.py   # or on stdin
python3 teams_update_project_inventory_levels_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Project inventory levels Teams Channel Update — Drafts a Teams channel post on project inventory levels status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-project-inventory-levels
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_project_inventory_levels',
    "version": '2.0.0',
    "display_name": 'Project inventory levels Teams Channel Update',
    "description": 'Drafts a Teams channel post on project inventory levels status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-project-inventory-levels',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-project-inventory-levels',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '68032c2774d33aab',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-sales-and-operations-planning/project-inventory-levels'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/teams-update-project-inventory-levels', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateProjectInventoryLevels(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateProjectInventoryLevels'
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
    print(TeamsUpdateProjectInventoryLevels().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
