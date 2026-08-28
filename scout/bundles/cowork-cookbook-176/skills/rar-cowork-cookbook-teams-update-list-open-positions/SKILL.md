---
name: "rar-cowork-cookbook-teams-update-list-open-positions"
description: "Drafts a Teams channel post on list open positions status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_list_open_positions", "rar_sha256": "93523fe2d10d119217ac1609e5e6161e20951bb44393b5b18ce34093b335db38", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_list_open_positions_agent.py` and embedded as the fenced Python below (sha256 93523fe2d10d1192…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_list_open_positions_agent.py` first:

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
    "version": '2.0.1',
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
