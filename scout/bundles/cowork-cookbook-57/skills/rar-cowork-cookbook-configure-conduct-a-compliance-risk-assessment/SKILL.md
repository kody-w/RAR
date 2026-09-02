---
name: "rar-cowork-cookbook-configure-conduct-a-compliance-risk-assessment"
description: "Applies a bulk configuration change to conduct a compliance risk assessment from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_conduct_a_compliance_risk_assessment", "rar_sha256": "0dd8c3088c35ffa7416546803a78e80a551b08306d47ba6cec231f670bce4c27", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_conduct_a_compliance_risk_assessment_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-conduct-a-compliance-risk-assessment:0c102bc6d6f0862c1ef990e8830c3cdd9e16d1bccf21d692895a5cf4b65ada1b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_conduct_a_compliance_risk_assessment`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_conduct_a_compliance_risk_assessment_agent.py` is
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

Conduct a compliance risk assessment Configuration Bulk Setup — Applies a bulk configuration change to conduct a compliance risk assessment from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-conduct-a-compliance-risk-assessment
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_conduct_a_compliance_risk_assessment_agent.py` and embedded as the fenced Python below (sha256 0dd8c3088c35ffa7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_conduct_a_compliance_risk_assessment_agent.py` first:

```bash
python3 configure_conduct_a_compliance_risk_assessment_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_conduct_a_compliance_risk_assessment_agent.py   # or on stdin
python3 configure_conduct_a_compliance_risk_assessment_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct a compliance risk assessment Configuration Bulk Setup — Applies a bulk configuration change to conduct a compliance risk assessment from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-conduct-a-compliance-risk-assessment
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_conduct_a_compliance_risk_assessment',
    "version": '2.0.0',
    "display_name": 'Conduct a compliance risk assessment Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to conduct a compliance risk assessment from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-conduct-a-compliance-risk-assessment',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-conduct-a-compliance-risk-assessment',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'eaf50f4fe6791b6a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-compliance/conduct-a-compliance-risk-assessment'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-conduct-a-compliance-risk-assessment', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureConductAComplianceRiskAssessment(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureConductAComplianceRiskAssessment'
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
    print(ConfigureConductAComplianceRiskAssessment().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
