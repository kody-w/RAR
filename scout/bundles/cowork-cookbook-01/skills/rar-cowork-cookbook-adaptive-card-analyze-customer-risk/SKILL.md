---
name: "rar-cowork-cookbook-adaptive-card-analyze-customer-risk"
description: "Produces a reusable Adaptive Card JSON snapshot of analyze customer risk status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_analyze_customer_risk", "rar_sha256": "7d287c89cc6869c261382dae7084f378d0e507026e842823ae2b6af09b611ce4", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_analyze_customer_risk_agent.py` and embedded as the fenced Python below (sha256 7d287c89cc6869c2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_analyze_customer_risk_agent.py` first:

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
    "version": '2.0.0',
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
