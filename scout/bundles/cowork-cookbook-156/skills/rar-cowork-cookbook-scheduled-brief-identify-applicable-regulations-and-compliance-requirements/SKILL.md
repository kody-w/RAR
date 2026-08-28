---
name: "rar-cowork-cookbook-scheduled-brief-identify-applicable-regulations-and-compliance-requirements"
description: "Schedulable morning-brief email summarizing identify applicable regulations and compliance requirements for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_identify_applicable_regulations_and_compliance_requirements", "rar_sha256": "2570f50d7572e8657eeefd164bdcfd17aa909cd308f538f834a46c7a3471ad00", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_identify_applicable_regulations_and_compliance_requirements`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_identify_applicable_regulations_and_compliance_requirements_agent.py` and in the RCI capsule.

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

Identify applicable regulations and compliance requirements Scheduled Email Brief — Schedulable morning-brief email summarizing identify applicable regulations and compliance requirements for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-identify-applicable-regulations-and-compliance-requirements
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_identify_applicable_regulations_and_compliance_requirements_agent.py` and embedded as the fenced Python below (sha256 2570f50d7572e865…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_identify_applicable_regulations_and_compliance_requirements_agent.py` first:

```bash
python3 scheduled_brief_identify_applicable_regulations_and_compliance_requirements_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_identify_applicable_regulations_and_compliance_requirements_agent.py   # or on stdin
python3 scheduled_brief_identify_applicable_regulations_and_compliance_requirements_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify applicable regulations and compliance requirements Scheduled Email Brief — Schedulable morning-brief email summarizing identify applicable regulations and compliance requirements for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-identify-applicable-regulations-and-compliance-requirements
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_identify_applicable_regulations_and_compliance_requirements',
    "version": '2.0.1',
    "display_name": 'Identify applicable regulations and compliance requirements Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing identify applicable regulations and compliance requirements for the responsible owner; designed to run daily or weekly.',
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
        "upstream_slug": 'scheduled-brief-identify-applicable-regulations-and-compliance-requirements',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-identify-applicable-regulations-and-compliance-requirements',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd48428467f145dc1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-compliance/identify-applicable-regulations-and-compliance-requirements'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-identify-applicable-regulations-and-compliance-requirements', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefIdentifyApplicableRegulationsAndComplianceRequirements(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefIdentifyApplicableRegulationsAndComplianceRequirements'
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
    print(ScheduledBriefIdentifyApplicableRegulationsAndComplianceRequirements().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
