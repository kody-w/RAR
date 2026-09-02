---
name: "rar-cowork-cookbook-teams-update-allocate-inventory"
description: "Drafts a Teams channel post on allocate inventory status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_allocate_inventory", "rar_sha256": "eec96c1904e1e963e2b6ccdc371737248b85aab36693a7b3be60b74a97089c63", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_allocate_inventory_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-allocate-inventory:353057f79e8e07c213a7f1876e2432a4fa4e620369982be444f69ed62adeb455", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_allocate_inventory`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_allocate_inventory_agent.py` is
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

Allocate inventory Teams Channel Update — Drafts a Teams channel post on allocate inventory status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-allocate-inventory
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_allocate_inventory_agent.py` and embedded as the fenced Python below (sha256 eec96c1904e1e963…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_allocate_inventory_agent.py` first:

```bash
python3 teams_update_allocate_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_allocate_inventory_agent.py   # or on stdin
python3 teams_update_allocate_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Allocate inventory Teams Channel Update — Drafts a Teams channel post on allocate inventory status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-allocate-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_allocate_inventory',
    "version": '2.0.0',
    "display_name": 'Allocate inventory Teams Channel Update',
    "description": 'Drafts a Teams channel post on allocate inventory status with an interactive Adaptive Card for quick triage.',
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
        "upstream_slug": 'teams-update-allocate-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-allocate-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2957dbf56f0e8b91',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/execute-sales-and-operations/allocate-inventory'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/teams-update-allocate-inventory', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateAllocateInventory(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateAllocateInventory'
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
    print(TeamsUpdateAllocateInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
