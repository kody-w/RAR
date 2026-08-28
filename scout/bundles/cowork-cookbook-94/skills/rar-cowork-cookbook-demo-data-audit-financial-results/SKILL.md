---
name: "rar-cowork-cookbook-demo-data-audit-financial-results"
description: "Generates and creates realistic demo records for audit financial results in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_audit_financial_results", "rar_sha256": "d7daeb4d5d980027249b4cbee059763d6e40a17f4dedb6e10f2043d96927d783", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_audit_financial_results`. The original RAPP
agent is preserved byte-for-byte in `demo_data_audit_financial_results_agent.py` and in the RCI capsule.

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

Audit financial results Demo Data Generator — Generates and creates realistic demo records for audit financial results in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-audit-financial-results
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_audit_financial_results_agent.py` and embedded as the fenced Python below (sha256 d7daeb4d5d980027…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_audit_financial_results_agent.py` first:

```bash
python3 demo_data_audit_financial_results_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_audit_financial_results_agent.py   # or on stdin
python3 demo_data_audit_financial_results_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Audit financial results Demo Data Generator — Generates and creates realistic demo records for audit financial results in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-audit-financial-results
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_audit_financial_results',
    "version": '2.0.1',
    "display_name": 'Audit financial results Demo Data Generator',
    "description": 'Generates and creates realistic demo records for audit financial results in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-audit-financial-results',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-audit-financial-results',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '31737e587fdb041a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/analyze-financial-performance/audit-financial-results'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/demo-data-audit-financial-results', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataAuditFinancialResults(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataAuditFinancialResults'
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
    print(DemoDataAuditFinancialResults().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
