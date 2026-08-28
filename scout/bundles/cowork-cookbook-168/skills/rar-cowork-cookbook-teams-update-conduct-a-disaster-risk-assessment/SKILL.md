---
name: "rar-cowork-cookbook-teams-update-conduct-a-disaster-risk-assessment"
description: "Drafts a Teams channel post on conduct a disaster risk assessment status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_conduct_a_disaster_risk_assessment", "rar_sha256": "54dd62740aacb4924e41eba3cc5a799e706b5d714c8a4f13439321d2d7607f76", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_conduct_a_disaster_risk_assessment_agent.py` and embedded as the fenced Python below (sha256 54dd62740aacb492…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_conduct_a_disaster_risk_assessment_agent.py` first:

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
    "version": '2.0.0',
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
