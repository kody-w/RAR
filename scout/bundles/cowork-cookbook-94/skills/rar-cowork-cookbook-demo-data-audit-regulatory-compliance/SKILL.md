---
name: "rar-cowork-cookbook-demo-data-audit-regulatory-compliance"
description: "Generates and creates realistic demo records for audit regulatory compliance in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_audit_regulatory_compliance", "rar_sha256": "5ddc2b3cb6afbfe53905f08698790b765100920cadf3e84db31d1dd3b8b39b1e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_audit_regulatory_compliance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-audit-regulatory-compliance:057efd0a6ec43f86b995bed46040c41a921821f8f53d432dad6900d8043d3583", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_audit_regulatory_compliance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_audit_regulatory_compliance_agent.py` is
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

Audit regulatory compliance Demo Data Generator — Generates and creates realistic demo records for audit regulatory compliance in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-audit-regulatory-compliance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_audit_regulatory_compliance_agent.py` and embedded as the fenced Python below (sha256 5ddc2b3cb6afbfe5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_audit_regulatory_compliance_agent.py` first:

```bash
python3 demo_data_audit_regulatory_compliance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_audit_regulatory_compliance_agent.py   # or on stdin
python3 demo_data_audit_regulatory_compliance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Audit regulatory compliance Demo Data Generator — Generates and creates realistic demo records for audit regulatory compliance in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-audit-regulatory-compliance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_audit_regulatory_compliance',
    "version": '2.0.0',
    "display_name": 'Audit regulatory compliance Demo Data Generator',
    "description": 'Generates and creates realistic demo records for audit regulatory compliance in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-audit-regulatory-compliance',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-audit-regulatory-compliance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '32d11805cecde2c8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/analyze-marketing-operations/audit-regulatory-compliance'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/demo-data-audit-regulatory-compliance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataAuditRegulatoryCompliance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataAuditRegulatoryCompliance'
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
    print(DemoDataAuditRegulatoryCompliance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
