---
name: "rar-cowork-cookbook-teams-update-start-production"
description: "Drafts a Teams channel post on start production status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_start_production", "rar_sha256": "65541fbd34d047a7f028c045b5932f566ee20de3ae1d8d8015db44333eab8ae3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_start_production_agent.py` and embedded as the fenced Python below (sha256 65541fbd34d047a7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_start_production_agent.py` first:

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
    "version": '2.0.0',
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
