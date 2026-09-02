---
name: "rar-cowork-cookbook-bulk-update-conduct-a-compliance-risk-assessment"
description: "Applies a bulk field update across conduct a compliance risk assessment records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_conduct_a_compliance_risk_assessment", "rar_sha256": "33312cffc115bca8cd1d6bf76feea0c91f911f2fa11bd6a0d32a45203f360c44", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_conduct_a_compliance_risk_assessment_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-conduct-a-compliance-risk-assessment:7b893e2b95ad3b7eeffe2ec2706daa07692326adde62b7794ca06e88d9951d78", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_conduct_a_compliance_risk_assessment`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_conduct_a_compliance_risk_assessment_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_conduct_a_compliance_risk_assessment_agent.py` and embedded as the fenced Python below (sha256 33312cffc115bca8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_conduct_a_compliance_risk_assessment_agent.py` first:

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
    "version": '2.0.0',
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
