---
name: "rar-cowork-cookbook-teams-update-conduct-a-disaster-risk-assessment"
description: "Drafts a Teams channel post on conduct a disaster risk assessment status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_conduct_a_disaster_risk_assessment", "rar_sha256": "54dd62740aacb4924e41eba3cc5a799e706b5d714c8a4f13439321d2d7607f76", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_conduct_a_disaster_risk_assessment_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-conduct-a-disaster-risk-assessment:0891f8f60b41e1a030a77d10f72796e0ddf33048d101159e506b0bf837f672f1", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_conduct_a_disaster_risk_assessment`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_conduct_a_disaster_risk_assessment_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
