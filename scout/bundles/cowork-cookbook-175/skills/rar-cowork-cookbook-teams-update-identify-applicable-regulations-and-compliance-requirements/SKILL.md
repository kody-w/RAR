---
name: "rar-cowork-cookbook-teams-update-identify-applicable-regulations-and-compliance-requirements"
description: "Drafts a Teams channel post on identify applicable regulations and compliance requirements status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_identify_applicable_regulations_and_compliance_requirements", "rar_sha256": "d2def918a7ad4ab61556bb417bc26c4f533e61969c76524fed8385d38555b38c", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_identify_applicable_regulations_and_compliance_requirements_agent.py` and embedded as the fenced Python below (sha256 d2def918a7ad4ab6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_identify_applicable_regulations_and_compliance_requirements_agent.py` first:

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
    "version": '2.0.1',
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
