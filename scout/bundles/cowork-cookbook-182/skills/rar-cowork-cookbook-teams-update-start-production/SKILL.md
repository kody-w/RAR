---
name: "rar-cowork-cookbook-teams-update-start-production"
description: "Drafts a Teams channel post on start production status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_start_production", "rar_sha256": "aa9b0f0bf30fdfb4a96eaf8dac3707cf9e857884343aaf98d90a68e2c3c385bd", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_start_production`. The original RAPP
agent is preserved byte-for-byte in `teams_update_start_production_agent.py` and in the RCI capsule.

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

Start production Teams Channel Update — Drafts a Teams channel post on start production status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-start-production
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_start_production_agent.py` and embedded as the fenced Python below (sha256 aa9b0f0bf30fdfb4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_start_production_agent.py` first:

```bash
python3 teams_update_start_production_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_start_production_agent.py   # or on stdin
python3 teams_update_start_production_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Start production Teams Channel Update — Drafts a Teams channel post on start production status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-start-production
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_start_production',
    "version": '2.0.1',
    "display_name": 'Start production Teams Channel Update',
    "description": 'Drafts a Teams channel post on start production status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-start-production',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-start-production',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3f56a45a2c24b1c5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/run-production-operations/start-production'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/teams-update-start-production', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateStartProduction(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateStartProduction'
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
    print(TeamsUpdateStartProduction().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
