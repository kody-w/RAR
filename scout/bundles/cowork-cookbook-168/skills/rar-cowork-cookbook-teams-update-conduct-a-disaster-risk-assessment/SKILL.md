---
name: "rar-cowork-cookbook-teams-update-conduct-a-disaster-risk-assessment"
description: "Drafts a Teams channel post on conduct a disaster risk assessment status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_conduct_a_disaster_risk_assessment", "rar_sha256": "0f5dd66a77533cb8defc09afd520237ca8b533691623745ae5f27f4a3fb4a6ff", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_conduct_a_disaster_risk_assessment`. The original RAPP
agent is preserved byte-for-byte in `teams_update_conduct_a_disaster_risk_assessment_agent.py` and in the RCI capsule.

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

Conduct a disaster risk assessment Teams Channel Update — Drafts a Teams channel post on conduct a disaster risk assessment status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-conduct-a-disaster-risk-assessment
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_conduct_a_disaster_risk_assessment_agent.py` and embedded as the fenced Python below (sha256 0f5dd66a77533cb8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_conduct_a_disaster_risk_assessment_agent.py` first:

```bash
python3 teams_update_conduct_a_disaster_risk_assessment_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_conduct_a_disaster_risk_assessment_agent.py   # or on stdin
python3 teams_update_conduct_a_disaster_risk_assessment_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct a disaster risk assessment Teams Channel Update — Drafts a Teams channel post on conduct a disaster risk assessment status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-conduct-a-disaster-risk-assessment
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_conduct_a_disaster_risk_assessment',
    "version": '2.0.1',
    "display_name": 'Conduct a disaster risk assessment Teams Channel Update',
    "description": 'Drafts a Teams channel post on conduct a disaster risk assessment status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-conduct-a-disaster-risk-assessment',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-conduct-a-disaster-risk-assessment',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a21c287dc0eec548',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/conduct-a-disaster-risk-assessment'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-conduct-a-disaster-risk-assessment', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateConductADisasterRiskAssessment(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateConductADisasterRiskAssessment'
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
    print(TeamsUpdateConductADisasterRiskAssessment().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
