---
name: "rar-cowork-cookbook-adaptive-card-develop-merchandise-and-assortment-plans"
description: "Produces a reusable Adaptive Card JSON snapshot of develop merchandise and assortment plans status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_merchandise_and_assortment_plans", "rar_sha256": "86d0c20eb9225dcb30ebf0cd0c54b552e6ec3e2c4231a5a605ff2d50f8b06447", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_develop_merchandise_and_assortment_plans`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_develop_merchandise_and_assortment_plans_agent.py` and in the RCI capsule.

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

Develop merchandise and assortment plans Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of develop merchandise and assortment plans status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-merchandise-and-assortment-plans
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_develop_merchandise_and_assortment_plans_agent.py` and embedded as the fenced Python below (sha256 86d0c20eb9225dcb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_develop_merchandise_and_assortment_plans_agent.py` first:

```bash
python3 adaptive_card_develop_merchandise_and_assortment_plans_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_develop_merchandise_and_assortment_plans_agent.py   # or on stdin
python3 adaptive_card_develop_merchandise_and_assortment_plans_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop merchandise and assortment plans Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of develop merchandise and assortment plans status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-merchandise-and-assortment-plans
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_develop_merchandise_and_assortment_plans',
    "version": '2.0.1',
    "display_name": 'Develop merchandise and assortment plans Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of develop merchandise and assortment plans status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-develop-merchandise-and-assortment-plans',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-develop-merchandise-and-assortment-plans',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0f6b9c899838882f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/develop-product-strategy/develop-merchandise-and-assortment-plans'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/adaptive-card-develop-merchandise-and-assortment-plans', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardDevelopMerchandiseAndAssortmentPlans(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDevelopMerchandiseAndAssortmentPlans'
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
    print(AdaptiveCardDevelopMerchandiseAndAssortmentPlans().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
