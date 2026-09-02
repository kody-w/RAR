---
name: "rar-cowork-cookbook-scheduled-brief-identify-applicable-regulations-and-compliance-requirements"
description: "Schedulable morning-brief email summarizing identify applicable regulations and compliance requirements for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_identify_applicable_regulations_and_compliance_requirements", "rar_sha256": "e1b08d07db56f0277351498886afb5142c96dcf7fb526bae46b85344d190baab", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_identify_applicable_regulations_and_compliance_requirements_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-identify-applicable-regulations-and-compliance-requirements:bf3031b4859b027bb35f89a8c8a093c24738ca85e51c32c6e50750e177d916ac", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_identify_applicable_regulations_and_compliance_requirements`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_identify_applicable_regulations_and_compliance_requirements_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_identify_applicable_regulations_and_compliance_requirements_agent.py` and embedded as the fenced Python below (sha256 e1b08d07db56f027…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_identify_applicable_regulations_and_compliance_requirements_agent.py` first:

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
    "version": '2.0.0',
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
