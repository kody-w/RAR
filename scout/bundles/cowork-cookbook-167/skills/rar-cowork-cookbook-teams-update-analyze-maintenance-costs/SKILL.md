---
name: "rar-cowork-cookbook-teams-update-analyze-maintenance-costs"
description: "Drafts a Teams channel post on analyze maintenance costs status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_analyze_maintenance_costs", "rar_sha256": "fa7d5b22c5cd0376b255ba276a67a1e5bb8236adf1ba273919a0e48b0cbd4a10", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_analyze_maintenance_costs`. The original RAPP
agent is preserved byte-for-byte in `teams_update_analyze_maintenance_costs_agent.py` and in the RCI capsule.

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

Analyze maintenance costs Teams Channel Update — Drafts a Teams channel post on analyze maintenance costs status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-analyze-maintenance-costs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_analyze_maintenance_costs_agent.py` and embedded as the fenced Python below (sha256 fa7d5b22c5cd0376…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_analyze_maintenance_costs_agent.py` first:

```bash
python3 teams_update_analyze_maintenance_costs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_analyze_maintenance_costs_agent.py   # or on stdin
python3 teams_update_analyze_maintenance_costs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze maintenance costs Teams Channel Update — Drafts a Teams channel post on analyze maintenance costs status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-analyze-maintenance-costs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_analyze_maintenance_costs',
    "version": '2.0.0',
    "display_name": 'Analyze maintenance costs Teams Channel Update',
    "description": 'Drafts a Teams channel post on analyze maintenance costs status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'teams-update-analyze-maintenance-costs',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-analyze-maintenance-costs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '906081b0cccd8080',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/analyze-assets/analyze-maintenance-costs'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/teams-update-analyze-maintenance-costs', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateAnalyzeMaintenanceCosts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateAnalyzeMaintenanceCosts'
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
    print(TeamsUpdateAnalyzeMaintenanceCosts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
