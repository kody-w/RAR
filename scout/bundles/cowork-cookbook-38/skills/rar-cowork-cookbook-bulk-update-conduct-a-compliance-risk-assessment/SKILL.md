---
name: "rar-cowork-cookbook-bulk-update-conduct-a-compliance-risk-assessment"
description: "Applies a bulk field update across conduct a compliance risk assessment records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_conduct_a_compliance_risk_assessment", "rar_sha256": "9df41be1278b83f711d81e9594374c69f734423e7ceecf4c6e6fc27158155703", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_conduct_a_compliance_risk_assessment`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_conduct_a_compliance_risk_assessment_agent.py` and in the RCI capsule.

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

Conduct a compliance risk assessment Bulk Field Update — Applies a bulk field update across conduct a compliance risk assessment records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-conduct-a-compliance-risk-assessment
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_conduct_a_compliance_risk_assessment_agent.py` and embedded as the fenced Python below (sha256 9df41be1278b83f7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_conduct_a_compliance_risk_assessment_agent.py` first:

```bash
python3 bulk_update_conduct_a_compliance_risk_assessment_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_conduct_a_compliance_risk_assessment_agent.py   # or on stdin
python3 bulk_update_conduct_a_compliance_risk_assessment_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct a compliance risk assessment Bulk Field Update — Applies a bulk field update across conduct a compliance risk assessment records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-conduct-a-compliance-risk-assessment
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_conduct_a_compliance_risk_assessment',
    "version": '2.0.1',
    "display_name": 'Conduct a compliance risk assessment Bulk Field Update',
    "description": 'Applies a bulk field update across conduct a compliance risk assessment records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-conduct-a-compliance-risk-assessment',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-conduct-a-compliance-risk-assessment',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '58963460909c788d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-compliance/conduct-a-compliance-risk-assessment'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-conduct-a-compliance-risk-assessment', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.857, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateConductAComplianceRiskAssessment(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateConductAComplianceRiskAssessment'
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
    print(BulkUpdateConductAComplianceRiskAssessment().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
