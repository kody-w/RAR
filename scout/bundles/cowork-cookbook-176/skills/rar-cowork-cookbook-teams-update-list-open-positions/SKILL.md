---
name: "rar-cowork-cookbook-teams-update-list-open-positions"
description: "Drafts a Teams channel post on list open positions status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_list_open_positions", "rar_sha256": "3d343041cb2a080ed75ed4f73afa2fff03e90b6175787e49df19534075f6b4c1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_list_open_positions`. The original RAPP
agent is preserved byte-for-byte in `teams_update_list_open_positions_agent.py` and in the RCI capsule.

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
