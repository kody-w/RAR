---
name: "rar-cowork-cookbook-demo-data-audit-financial-results"
description: "Generates and creates realistic demo records for audit financial results in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_audit_financial_results", "rar_sha256": "cf3e04d010009694280b9047bd53a563c23e92c162531cc13c6828354dc8c986", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_audit_financial_results_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-audit-financial-results:b860e713c2f4d5992309fa105a451304d5843310101dfae357664ffeba97070f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_audit_financial_results`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_audit_financial_results_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_audit_financial_results_agent.py` and embedded as the fenced Python below (sha256 cf3e04d010009694…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_audit_financial_results_agent.py` first:

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
    "version": '2.0.0',
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
