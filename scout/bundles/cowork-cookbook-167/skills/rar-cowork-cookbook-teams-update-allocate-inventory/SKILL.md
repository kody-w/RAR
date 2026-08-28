---
name: "rar-cowork-cookbook-teams-update-allocate-inventory"
description: "Drafts a Teams channel post on allocate inventory status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_allocate_inventory", "rar_sha256": "bafbe08d98911a8601ed2bf10ec81373aa8dcfcc3dcc6502f87a42b0f4592409", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_allocate_inventory`. The original RAPP
agent is preserved byte-for-byte in `teams_update_allocate_inventory_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_allocate_inventory_agent.py` and embedded as the fenced Python below (sha256 bafbe08d98911a86…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_allocate_inventory_agent.py` first:

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
    "version": '2.0.1',
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
