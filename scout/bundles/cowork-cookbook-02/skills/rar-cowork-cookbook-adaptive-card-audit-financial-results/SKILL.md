---
name: "rar-cowork-cookbook-adaptive-card-audit-financial-results"
description: "Produces a reusable Adaptive Card JSON snapshot of audit financial results status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_audit_financial_results", "rar_sha256": "21ec9847834958380f156017a84fb138e43278850983e70dc928a13e49fb20dc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_audit_financial_results`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_audit_financial_results_agent.py` and in the RCI capsule.

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
