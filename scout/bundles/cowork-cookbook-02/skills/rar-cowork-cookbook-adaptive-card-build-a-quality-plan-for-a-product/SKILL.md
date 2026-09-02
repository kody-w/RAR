---
name: "rar-cowork-cookbook-adaptive-card-build-a-quality-plan-for-a-product"
description: "Produces a reusable Adaptive Card JSON snapshot of build a quality plan for a product status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_build_a_quality_plan_for_a_product", "rar_sha256": "4245069fee64ab41fe5b79e541da54e0dd512c7ec9e077bcff1157f41fa2fd3c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_build_a_quality_plan_for_a_product_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-build-a-quality-plan-for-a-product:0daba4ef95b48a7d3963630a2dd7f8a8b2c057d47eefa89321fb3deada99f05e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_build_a_quality_plan_for_a_product`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_build_a_quality_plan_for_a_product_agent.py` is
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
