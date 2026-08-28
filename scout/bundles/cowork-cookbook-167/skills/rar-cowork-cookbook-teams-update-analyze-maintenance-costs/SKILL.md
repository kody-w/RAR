---
name: "rar-cowork-cookbook-teams-update-analyze-maintenance-costs"
description: "Drafts a Teams channel post on analyze maintenance costs status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_analyze_maintenance_costs", "rar_sha256": "a2579a1814090ae2d9e60a0e586d28c3a29d6929a39dd39a9f00199f095acd3a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_analyze_maintenance_costs_agent.py` and embedded as the fenced Python below (sha256 a2579a1814090ae2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_analyze_maintenance_costs_agent.py` first:

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
    "version": '2.0.1',
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
