---
name: "rar-cowork-cookbook-scheduled-brief-conduct-a-disaster-risk-assessment"
description: "Schedulable morning-brief email summarizing conduct a disaster risk assessment for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_conduct_a_disaster_risk_assessment", "rar_sha256": "d413e3db425080f89ff4a4c34122c62b26310e9be645c3386b9a007811387cf1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
