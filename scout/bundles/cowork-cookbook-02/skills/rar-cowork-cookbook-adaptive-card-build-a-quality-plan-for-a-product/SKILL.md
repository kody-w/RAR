---
name: "rar-cowork-cookbook-adaptive-card-build-a-quality-plan-for-a-product"
description: "Produces a reusable Adaptive Card JSON snapshot of build a quality plan for a product status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_build_a_quality_plan_for_a_product", "rar_sha256": "4245069fee64ab41fe5b79e541da54e0dd512c7ec9e077bcff1157f41fa2fd3c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_build_a_quality_plan_for_a_product`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_build_a_quality_plan_for_a_product_agent.py` and in the RCI capsule.

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

Build a quality plan for a product Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of build a quality plan for a product status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-build-a-quality-plan-for-a-product
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_build_a_quality_plan_for_a_product_agent.py` and embedded as the fenced Python below (sha256 4245069fee64ab41…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_build_a_quality_plan_for_a_product_agent.py` first:

```bash
python3 adaptive_card_build_a_quality_plan_for_a_product_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_build_a_quality_plan_for_a_product_agent.py   # or on stdin
python3 adaptive_card_build_a_quality_plan_for_a_product_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Build a quality plan for a product Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of build a quality plan for a product status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-build-a-quality-plan-for-a-product
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_build_a_quality_plan_for_a_product',
    "version": '2.0.0',
    "display_name": 'Build a quality plan for a product Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of build a quality plan for a product status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-build-a-quality-plan-for-a-product',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-build-a-quality-plan-for-a-product',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '694fcc2d3e47dd9b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-inventory-quality/build-a-quality-plan-for-a-product'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/adaptive-card-build-a-quality-plan-for-a-product', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardBuildAQualityPlanForAProduct(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardBuildAQualityPlanForAProduct'
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
    print(AdaptiveCardBuildAQualityPlanForAProduct().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
