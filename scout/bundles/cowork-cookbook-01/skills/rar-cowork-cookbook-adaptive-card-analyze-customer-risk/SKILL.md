---
name: "rar-cowork-cookbook-adaptive-card-analyze-customer-risk"
description: "Produces a reusable Adaptive Card JSON snapshot of analyze customer risk status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_analyze_customer_risk", "rar_sha256": "b157a502d8f0b10e63fad23c6ce3f22a7b7ea85b3a6343d4d53494065562b764", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_analyze_customer_risk`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_analyze_customer_risk_agent.py` and in the RCI capsule.

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

Analyze customer risk Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of analyze customer risk status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-analyze-customer-risk
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_analyze_customer_risk_agent.py` and embedded as the fenced Python below (sha256 b157a502d8f0b10e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_analyze_customer_risk_agent.py` first:

```bash
python3 adaptive_card_analyze_customer_risk_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_analyze_customer_risk_agent.py   # or on stdin
python3 adaptive_card_analyze_customer_risk_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze customer risk Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of analyze customer risk status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-analyze-customer-risk
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_analyze_customer_risk',
    "version": '2.0.1',
    "display_name": 'Analyze customer risk Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of analyze customer risk status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-analyze-customer-risk',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-analyze-customer-risk',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8a12f1a1cee4c15f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/analyze-sales-performance/analyze-customer-risk'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/adaptive-card-analyze-customer-risk', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardAnalyzeCustomerRisk(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardAnalyzeCustomerRisk'
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
    print(AdaptiveCardAnalyzeCustomerRisk().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
