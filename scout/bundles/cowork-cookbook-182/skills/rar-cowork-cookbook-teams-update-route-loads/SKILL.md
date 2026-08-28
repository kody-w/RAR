---
name: "rar-cowork-cookbook-teams-update-route-loads"
description: "Drafts a Teams channel post on route loads status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_route_loads", "rar_sha256": "1688695dec2b4842777b6a477fb385708c08dfdb242dc72bcb4fb1c4a0c0831d", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_route_loads`. The original RAPP
agent is preserved byte-for-byte in `teams_update_route_loads_agent.py` and in the RCI capsule.

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

Route loads Teams Channel Update — Drafts a Teams channel post on route loads status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-route-loads
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_route_loads_agent.py` and embedded as the fenced Python below (sha256 1688695dec2b4842…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_route_loads_agent.py` first:

```bash
python3 teams_update_route_loads_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_route_loads_agent.py   # or on stdin
python3 teams_update_route_loads_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Route loads Teams Channel Update — Drafts a Teams channel post on route loads status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-route-loads
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_route_loads',
    "version": '2.0.1',
    "display_name": 'Route loads Teams Channel Update',
    "description": 'Drafts a Teams channel post on route loads status with an interactive Adaptive Card for quick triage.',
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
        "upstream_slug": 'teams-update-route-loads',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-route-loads',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3c5ff24841631b58',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-freight-and-transportation/route-loads'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/teams-update-route-loads', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateRouteLoads(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateRouteLoads'
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
    print(TeamsUpdateRouteLoads().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
