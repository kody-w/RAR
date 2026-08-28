---
name: "rar-cowork-cookbook-teams-update-allocate-headcount-to-business-units"
description: "Drafts a Teams channel post on allocate headcount to business units status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_allocate_headcount_to_business_units", "rar_sha256": "87c0ba8198e0ec390cb061b1728ec38dd51d4cada3bc2e38cda6cd36d544dfc8", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_allocate_headcount_to_business_units`. The original RAPP
agent is preserved byte-for-byte in `teams_update_allocate_headcount_to_business_units_agent.py` and in the RCI capsule.

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

Allocate headcount to business units Teams Channel Update — Drafts a Teams channel post on allocate headcount to business units status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-allocate-headcount-to-business-units
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_allocate_headcount_to_business_units_agent.py` and embedded as the fenced Python below (sha256 87c0ba8198e0ec39…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_allocate_headcount_to_business_units_agent.py` first:

```bash
python3 teams_update_allocate_headcount_to_business_units_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_allocate_headcount_to_business_units_agent.py   # or on stdin
python3 teams_update_allocate_headcount_to_business_units_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Allocate headcount to business units Teams Channel Update — Drafts a Teams channel post on allocate headcount to business units status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-allocate-headcount-to-business-units
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_allocate_headcount_to_business_units',
    "version": '2.0.1',
    "display_name": 'Allocate headcount to business units Teams Channel Update',
    "description": 'Drafts a Teams channel post on allocate headcount to business units status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-allocate-headcount-to-business-units',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-allocate-headcount-to-business-units',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'adb9027c266c675c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-financial-planning/allocate-headcount-to-business-units'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/teams-update-allocate-headcount-to-business-units', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateAllocateHeadcountToBusinessUnits(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateAllocateHeadcountToBusinessUnits'
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
    print(TeamsUpdateAllocateHeadcountToBusinessUnits().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
