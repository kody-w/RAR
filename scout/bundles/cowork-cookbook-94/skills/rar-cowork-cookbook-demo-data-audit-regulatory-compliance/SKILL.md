---
name: "rar-cowork-cookbook-demo-data-audit-regulatory-compliance"
description: "Generates and creates realistic demo records for audit regulatory compliance in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_audit_regulatory_compliance", "rar_sha256": "5ddc2b3cb6afbfe53905f08698790b765100920cadf3e84db31d1dd3b8b39b1e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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
