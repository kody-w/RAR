---
name: "rar-cowork-cookbook-teams-update-allocate-inventory"
description: "Drafts a Teams channel post on allocate inventory status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_allocate_inventory", "rar_sha256": "eec96c1904e1e963e2b6ccdc371737248b85aab36693a7b3be60b74a97089c63", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
