---
name: "rar-cowork-cookbook-demo-data-audit-regulatory-compliance"
description: "Generates and creates realistic demo records for audit regulatory compliance in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_audit_regulatory_compliance", "rar_sha256": "b67d547a264d19c805fea6225a2d7653363cd8587c042118499155de80567c0b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_audit_regulatory_compliance`. The original RAPP
agent is preserved byte-for-byte in `demo_data_audit_regulatory_compliance_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_audit_regulatory_compliance_agent.py` and embedded as the fenced Python below (sha256 b67d547a264d19c8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_audit_regulatory_compliance_agent.py` first:

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
    "version": '2.0.1',
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
