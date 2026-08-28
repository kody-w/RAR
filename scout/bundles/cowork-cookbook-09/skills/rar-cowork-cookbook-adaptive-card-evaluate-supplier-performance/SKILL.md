---
name: "rar-cowork-cookbook-adaptive-card-evaluate-supplier-performance"
description: "Produces a reusable Adaptive Card JSON snapshot of evaluate supplier performance status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_evaluate_supplier_performance", "rar_sha256": "8040f20bd863cae186d15d0f2f3d0fe4122224d2190d30f62acec477a731e119", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_evaluate_supplier_performance_agent.py` and embedded as the fenced Python below (sha256 8040f20bd863cae1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_evaluate_supplier_performance_agent.py` first:

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
    "version": '2.0.0',
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
