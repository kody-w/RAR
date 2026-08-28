---
name: "rar-cowork-cookbook-teams-update-count-inventory"
description: "Drafts a Teams channel post on count inventory status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_count_inventory", "rar_sha256": "22d721652a2369155e3e60d585059a0dd0016acc1a7a250aba141c7bcea0cd33", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_count_inventory`. The original RAPP
agent is preserved byte-for-byte in `teams_update_count_inventory_agent.py` and in the RCI capsule.

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

Count inventory Teams Channel Update — Drafts a Teams channel post on count inventory status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-count-inventory
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_count_inventory_agent.py` and embedded as the fenced Python below (sha256 22d721652a236915…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_count_inventory_agent.py` first:

```bash
python3 teams_update_count_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_count_inventory_agent.py   # or on stdin
python3 teams_update_count_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Count inventory Teams Channel Update — Drafts a Teams channel post on count inventory status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-count-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_count_inventory',
    "version": '2.0.1',
    "display_name": 'Count inventory Teams Channel Update',
    "description": 'Drafts a Teams channel post on count inventory status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-count-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-count-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a19d51ba4e8ef04e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/maintain-inventory-levels/count-inventory'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/teams-update-count-inventory', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateCountInventory(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateCountInventory'
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
    print(TeamsUpdateCountInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
