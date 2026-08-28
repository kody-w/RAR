---
name: "rar-cowork-cookbook-adaptive-card-evaluate-supplier-performance"
description: "Produces a reusable Adaptive Card JSON snapshot of evaluate supplier performance status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_evaluate_supplier_performance", "rar_sha256": "9868dd6653decd0da72a2eedb5a7b224035db34716aab9364c5b6c63afebc650", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_evaluate_supplier_performance`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_evaluate_supplier_performance_agent.py` and in the RCI capsule.

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

Evaluate supplier performance Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of evaluate supplier performance status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-evaluate-supplier-performance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_evaluate_supplier_performance_agent.py` and embedded as the fenced Python below (sha256 9868dd6653decd0d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_evaluate_supplier_performance_agent.py` first:

```bash
python3 adaptive_card_evaluate_supplier_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_evaluate_supplier_performance_agent.py   # or on stdin
python3 adaptive_card_evaluate_supplier_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Evaluate supplier performance Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of evaluate supplier performance status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-evaluate-supplier-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_evaluate_supplier_performance',
    "version": '2.0.1',
    "display_name": 'Evaluate supplier performance Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of evaluate supplier performance status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-evaluate-supplier-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-evaluate-supplier-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '484c89491902034d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-supplier-relationships/evaluate-supplier-performance'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/adaptive-card-evaluate-supplier-performance', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardEvaluateSupplierPerformance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardEvaluateSupplierPerformance'
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
    print(AdaptiveCardEvaluateSupplierPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
