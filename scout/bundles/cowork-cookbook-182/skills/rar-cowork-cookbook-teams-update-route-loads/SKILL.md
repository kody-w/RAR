---
name: "rar-cowork-cookbook-teams-update-route-loads"
description: "Drafts a Teams channel post on route loads status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_route_loads", "rar_sha256": "c6f57480b88c6b82e2ac7d1bb69340a45103ccc539fa2f6df804ef86fb84a964", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_route_loads_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-route-loads:9db1f95b9693be12d9194eae615b9f6b645b4d94e1eebc6331f193dc2ca8dff7", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_route_loads`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_route_loads_agent.py` is
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
