---
name: "rar-cowork-cookbook-teams-update-allocate-service-parts-inventory"
description: "Drafts a Teams channel post on allocate service parts inventory status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_allocate_service_parts_inventory", "rar_sha256": "0039885e1853b48ab7e473d1810ddb952688bab8d37080a5853aec5450ba8594", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_allocate_service_parts_inventory_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-allocate-service-parts-inventory:5015eae969e17ea9c10710658f0a3a6e7d131f396499acc494990db78a3a57d2", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_allocate_service_parts_inventory`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_allocate_service_parts_inventory_agent.py` is
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

Allocate service parts inventory Teams Channel Update — Drafts a Teams channel post on allocate service parts inventory status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-allocate-service-parts-inventory
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_allocate_service_parts_inventory_agent.py` and embedded as the fenced Python below (sha256 0039885e1853b48a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_allocate_service_parts_inventory_agent.py` first:

```bash
python3 teams_update_allocate_service_parts_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_allocate_service_parts_inventory_agent.py   # or on stdin
python3 teams_update_allocate_service_parts_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Allocate service parts inventory Teams Channel Update — Drafts a Teams channel post on allocate service parts inventory status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-allocate-service-parts-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_allocate_service_parts_inventory',
    "version": '2.0.0',
    "display_name": 'Allocate service parts inventory Teams Channel Update',
    "description": 'Drafts a Teams channel post on allocate service parts inventory status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-allocate-service-parts-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-allocate-service-parts-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b34e68f098d8b3f8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/manage-service-work/allocate-service-parts-inventory'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/teams-update-allocate-service-parts-inventory', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateAllocateServicePartsInventory(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateAllocateServicePartsInventory'
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
    print(TeamsUpdateAllocateServicePartsInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
