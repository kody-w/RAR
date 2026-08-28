---
name: "rar-cowork-cookbook-configure-conduct-a-compliance-risk-assessment"
description: "Applies a bulk configuration change to conduct a compliance risk assessment from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_conduct_a_compliance_risk_assessment", "rar_sha256": "d668115c3fe3695a5515da41fdb05201ba0abbcdc2e74620312cca85c8287b9b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_conduct_a_compliance_risk_assessment_agent.py` and embedded as the fenced Python below (sha256 d668115c3fe3695a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_conduct_a_compliance_risk_assessment_agent.py` first:

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
    "version": '2.0.1',
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
