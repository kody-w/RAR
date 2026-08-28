---
name: "rar-cowork-cookbook-teams-update-identify-applicable-regulations-and-compliance-requirements"
description: "Drafts a Teams channel post on identify applicable regulations and compliance requirements status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_identify_applicable_regulations_and_compliance_requirements", "rar_sha256": "a4b893bde7d4ee9d85cd2ff8d4198bd7678fad9bfa5edd26d4bc35acc33d99ed", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_identify_applicable_regulations_and_compliance_requirements`. The original RAPP
agent is preserved byte-for-byte in `teams_update_identify_applicable_regulations_and_compliance_requirements_agent.py` and in the RCI capsule.

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
