---
name: "rar-cowork-cookbook-adaptive-card-build-a-quality-plan-for-a-product"
description: "Produces a reusable Adaptive Card JSON snapshot of build a quality plan for a product status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_build_a_quality_plan_for_a_product", "rar_sha256": "3b2a2981fd71f3c4bc39640bd94d801753d5e5263b585fe62fb1531a09518bd0", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_build_a_quality_plan_for_a_product_agent.py` and embedded as the fenced Python below (sha256 3b2a2981fd71f3c4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_build_a_quality_plan_for_a_product_agent.py` first:

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
    "version": '2.0.1',
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
