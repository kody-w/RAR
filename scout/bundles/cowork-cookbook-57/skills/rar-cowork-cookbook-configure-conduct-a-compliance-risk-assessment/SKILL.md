---
name: "rar-cowork-cookbook-configure-conduct-a-compliance-risk-assessment"
description: "Applies a bulk configuration change to conduct a compliance risk assessment from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_conduct_a_compliance_risk_assessment", "rar_sha256": "0dd8c3088c35ffa7416546803a78e80a551b08306d47ba6cec231f670bce4c27", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_conduct_a_compliance_risk_assessment`. The original RAPP
agent is preserved byte-for-byte in `configure_conduct_a_compliance_risk_assessment_agent.py` and in the RCI capsule.

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
