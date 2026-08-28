---
name: "rar-cowork-cookbook-teams-update-route-loads"
description: "Drafts a Teams channel post on route loads status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_route_loads", "rar_sha256": "c6f57480b88c6b82e2ac7d1bb69340a45103ccc539fa2f6df804ef86fb84a964", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_route_loads_agent.py` and embedded as the fenced Python below (sha256 c6f57480b88c6b82…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_route_loads_agent.py` first:

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
    "version": '2.0.0',
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
