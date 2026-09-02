---
name: "rar-cowork-cookbook-scheduled-brief-conduct-a-disaster-risk-assessment"
description: "Schedulable morning-brief email summarizing conduct a disaster risk assessment for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_conduct_a_disaster_risk_assessment", "rar_sha256": "d413e3db425080f89ff4a4c34122c62b26310e9be645c3386b9a007811387cf1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_conduct_a_disaster_risk_assessment_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-conduct-a-disaster-risk-assessment:8c03512159262d987f2b70c02c6ee2a8966453eca5473179ef15ad9175064040", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_conduct_a_disaster_risk_assessment`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_conduct_a_disaster_risk_assessment_agent.py` is
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

Conduct a disaster risk assessment Scheduled Email Brief — Schedulable morning-brief email summarizing conduct a disaster risk assessment for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-conduct-a-disaster-risk-assessment
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_conduct_a_disaster_risk_assessment_agent.py` and embedded as the fenced Python below (sha256 d413e3db425080f8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_conduct_a_disaster_risk_assessment_agent.py` first:

```bash
python3 scheduled_brief_conduct_a_disaster_risk_assessment_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_conduct_a_disaster_risk_assessment_agent.py   # or on stdin
python3 scheduled_brief_conduct_a_disaster_risk_assessment_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct a disaster risk assessment Scheduled Email Brief — Schedulable morning-brief email summarizing conduct a disaster risk assessment for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-conduct-a-disaster-risk-assessment
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_conduct_a_disaster_risk_assessment',
    "version": '2.0.0',
    "display_name": 'Conduct a disaster risk assessment Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing conduct a disaster risk assessment for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-conduct-a-disaster-risk-assessment',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-conduct-a-disaster-risk-assessment',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '19702fb82ba84c44',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/conduct-a-disaster-risk-assessment'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-conduct-a-disaster-risk-assessment', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefConductADisasterRiskAssessment(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefConductADisasterRiskAssessment'
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
    print(ScheduledBriefConductADisasterRiskAssessment().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
