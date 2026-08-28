---
name: "rar-cowork-cookbook-scheduled-brief-identify-applicable-regulations-and-compliance-requirements"
description: "Schedulable morning-brief email summarizing identify applicable regulations and compliance requirements for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_identify_applicable_regulations_and_compliance_requirements", "rar_sha256": "e1b08d07db56f0277351498886afb5142c96dcf7fb526bae46b85344d190baab", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
