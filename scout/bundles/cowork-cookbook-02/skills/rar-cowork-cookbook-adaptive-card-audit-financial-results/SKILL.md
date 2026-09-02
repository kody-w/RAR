---
name: "rar-cowork-cookbook-adaptive-card-audit-financial-results"
description: "Produces a reusable Adaptive Card JSON snapshot of audit financial results status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_audit_financial_results", "rar_sha256": "21ec9847834958380f156017a84fb138e43278850983e70dc928a13e49fb20dc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_audit_financial_results_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-audit-financial-results:14f50156d92db4ad074438f37d2ccf04d81374920b3779c20e2d35255f2c387c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_audit_financial_results`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_audit_financial_results_agent.py` is
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

Audit financial results Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of audit financial results status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-audit-financial-results
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_audit_financial_results_agent.py` and embedded as the fenced Python below (sha256 21ec984783495838…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_audit_financial_results_agent.py` first:

```bash
python3 adaptive_card_audit_financial_results_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_audit_financial_results_agent.py   # or on stdin
python3 adaptive_card_audit_financial_results_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Audit financial results Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of audit financial results status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-audit-financial-results
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_audit_financial_results',
    "version": '2.0.0',
    "display_name": 'Audit financial results Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of audit financial results status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-audit-financial-results',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-audit-financial-results',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2b3e21c2fded4896',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/analyze-financial-performance/audit-financial-results'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/adaptive-card-audit-financial-results', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardAuditFinancialResults(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardAuditFinancialResults'
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
    print(AdaptiveCardAuditFinancialResults().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
