---
name: "rar-cowork-cookbook-adaptive-card-audit-financial-results"
description: "Produces a reusable Adaptive Card JSON snapshot of audit financial results status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_audit_financial_results", "rar_sha256": "dddabc65d8a0af1728b05f6cfac92c7641c4d4b913f4ee33b51a0a98f38ce5dc", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_audit_financial_results_agent.py` and embedded as the fenced Python below (sha256 dddabc65d8a0af17…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_audit_financial_results_agent.py` first:

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
    "version": '2.0.1',
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
