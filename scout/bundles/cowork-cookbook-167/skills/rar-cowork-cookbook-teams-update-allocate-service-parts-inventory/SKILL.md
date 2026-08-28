---
name: "rar-cowork-cookbook-teams-update-allocate-service-parts-inventory"
description: "Drafts a Teams channel post on allocate service parts inventory status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_allocate_service_parts_inventory", "rar_sha256": "0039885e1853b48ab7e473d1810ddb952688bab8d37080a5853aec5450ba8594", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_allocate_service_parts_inventory`. The original RAPP
agent is preserved byte-for-byte in `teams_update_allocate_service_parts_inventory_agent.py` and in the RCI capsule.

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
