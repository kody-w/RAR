---
name: "rar-cowork-cookbook-teams-update-measure-and-analyze-procurement-spend"
description: "Drafts a Teams channel post on measure and analyze procurement spend status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_measure_and_analyze_procurement_spend", "rar_sha256": "1851943934ac7750ba5d1146caaf84bb255fab373a62b4cb5f269c34e498b151", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_measure_and_analyze_procurement_spend`. The original RAPP
agent is preserved byte-for-byte in `teams_update_measure_and_analyze_procurement_spend_agent.py` and in the RCI capsule.

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

Measure and analyze procurement spend Teams Channel Update — Drafts a Teams channel post on measure and analyze procurement spend status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-measure-and-analyze-procurement-spend
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_measure_and_analyze_procurement_spend_agent.py` and embedded as the fenced Python below (sha256 1851943934ac7750…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_measure_and_analyze_procurement_spend_agent.py` first:

```bash
python3 teams_update_measure_and_analyze_procurement_spend_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_measure_and_analyze_procurement_spend_agent.py   # or on stdin
python3 teams_update_measure_and_analyze_procurement_spend_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Measure and analyze procurement spend Teams Channel Update — Drafts a Teams channel post on measure and analyze procurement spend status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-measure-and-analyze-procurement-spend
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_measure_and_analyze_procurement_spend',
    "version": '2.0.0',
    "display_name": 'Measure and analyze procurement spend Teams Channel Update',
    "description": 'Drafts a Teams channel post on measure and analyze procurement spend status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-measure-and-analyze-procurement-spend',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-measure-and-analyze-procurement-spend',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bdf27a411f8d5dca',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/analyze-procurement-and-sourcing/measure-and-analyze-procurement-spend'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/teams-update-measure-and-analyze-procurement-spend', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateMeasureAndAnalyzeProcurementSpend(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateMeasureAndAnalyzeProcurementSpend'
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
    print(TeamsUpdateMeasureAndAnalyzeProcurementSpend().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
