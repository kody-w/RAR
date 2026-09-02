---
name: "rar-cowork-cookbook-teams-update-count-inventory"
description: "Drafts a Teams channel post on count inventory status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_count_inventory", "rar_sha256": "c82441143eb98bc576890881e1441700504992b693f4b3b264583fa7ffdb5e36", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_count_inventory_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-count-inventory:e6f077db586b63fe5dd0fb8a69d5df5d99faf9dd7be444a0d8acf37997fee1d7", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_count_inventory`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_count_inventory_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_count_inventory_agent.py` and embedded as the fenced Python below (sha256 c82441143eb98bc5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_count_inventory_agent.py` first:

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
    "version": '2.0.0',
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
