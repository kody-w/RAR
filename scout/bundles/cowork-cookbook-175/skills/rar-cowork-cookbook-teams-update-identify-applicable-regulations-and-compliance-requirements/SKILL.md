---
name: "rar-cowork-cookbook-teams-update-identify-applicable-regulations-and-compliance-requirements"
description: "Drafts a Teams channel post on identify applicable regulations and compliance requirements status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_identify_applicable_regulations_and_compliance_requirements", "rar_sha256": "a4b893bde7d4ee9d85cd2ff8d4198bd7678fad9bfa5edd26d4bc35acc33d99ed", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_identify_applicable_regulations_and_compliance_requirements_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-identify-applicable-regulations-and-compliance-requirements:c915097019fe7ace05b4437610fafb9581e18a15c6e046917b4060ab1ca681fa", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_identify_applicable_regulations_and_compliance_requirements`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_identify_applicable_regulations_and_compliance_requirements_agent.py` is
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

Identify applicable regulations and compliance requirements Teams Channel Update — Drafts a Teams channel post on identify applicable regulations and compliance requirements status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-identify-applicable-regulations-and-compliance-requirements
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_identify_applicable_regulations_and_compliance_requirements_agent.py` and embedded as the fenced Python below (sha256 a4b893bde7d4ee9d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_identify_applicable_regulations_and_compliance_requirements_agent.py` first:

```bash
python3 teams_update_identify_applicable_regulations_and_compliance_requirements_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_identify_applicable_regulations_and_compliance_requirements_agent.py   # or on stdin
python3 teams_update_identify_applicable_regulations_and_compliance_requirements_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify applicable regulations and compliance requirements Teams Channel Update — Drafts a Teams channel post on identify applicable regulations and compliance requirements status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-identify-applicable-regulations-and-compliance-requirements
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_identify_applicable_regulations_and_compliance_requirements',
    "version": '2.0.0',
    "display_name": 'Identify applicable regulations and compliance requirements Teams Channel Update',
    "description": 'Drafts a Teams channel post on identify applicable regulations and compliance requirements status with an interactive Adaptive Card for quick triage.',
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
        "upstream_slug": 'teams-update-identify-applicable-regulations-and-compliance-requirements',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-identify-applicable-regulations-and-compliance-requirements',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1791e6cc16a736c9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-compliance/identify-applicable-regulations-and-compliance-requirements'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-identify-applicable-regulations-and-compliance-requirements', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateIdentifyApplicableRegulationsAndComplianceRequirements(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateIdentifyApplicableRegulationsAndComplianceRequirements'
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
    print(TeamsUpdateIdentifyApplicableRegulationsAndComplianceRequirements().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
