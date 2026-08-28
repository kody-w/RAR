---
name: "rar-cowork-cookbook-scheduled-brief-conduct-a-disaster-risk-assessment"
description: "Schedulable morning-brief email summarizing conduct a disaster risk assessment for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_conduct_a_disaster_risk_assessment", "rar_sha256": "f8eb431d57255a1fa28a7b16cd2a3075ec38fb78d0127b3d792beef817df9b8c", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_conduct_a_disaster_risk_assessment`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_conduct_a_disaster_risk_assessment_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_conduct_a_disaster_risk_assessment_agent.py` and embedded as the fenced Python below (sha256 f8eb431d57255a1f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_conduct_a_disaster_risk_assessment_agent.py` first:

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
    "version": '2.0.1',
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
