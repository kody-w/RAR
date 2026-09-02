---
name: "rar-cowork-cookbook-teams-update-list-open-positions"
description: "Drafts a Teams channel post on list open positions status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_list_open_positions", "rar_sha256": "3d343041cb2a080ed75ed4f73afa2fff03e90b6175787e49df19534075f6b4c1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_list_open_positions_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-list-open-positions:887185cd6d1e8c0a8747d1bc03f211bb73f4073939258853bf225fce1c8ab3a4", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_list_open_positions`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_list_open_positions_agent.py` is
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

List open positions Teams Channel Update — Drafts a Teams channel post on list open positions status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-list-open-positions
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_list_open_positions_agent.py` and embedded as the fenced Python below (sha256 3d343041cb2a080e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_list_open_positions_agent.py` first:

```bash
python3 teams_update_list_open_positions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_list_open_positions_agent.py   # or on stdin
python3 teams_update_list_open_positions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
List open positions Teams Channel Update — Drafts a Teams channel post on list open positions status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-list-open-positions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_list_open_positions',
    "version": '2.0.0',
    "display_name": 'List open positions Teams Channel Update',
    "description": 'Drafts a Teams channel post on list open positions status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-list-open-positions',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-list-open-positions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b947bba127dd15f5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/recruit-and-onboard-talent/list-open-positions'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/teams-update-list-open-positions', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateListOpenPositions(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateListOpenPositions'
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
    print(TeamsUpdateListOpenPositions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
