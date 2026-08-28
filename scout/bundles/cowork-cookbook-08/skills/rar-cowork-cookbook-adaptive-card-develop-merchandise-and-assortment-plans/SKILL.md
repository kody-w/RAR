---
name: "rar-cowork-cookbook-adaptive-card-develop-merchandise-and-assortment-plans"
description: "Produces a reusable Adaptive Card JSON snapshot of develop merchandise and assortment plans status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_merchandise_and_assortment_plans", "rar_sha256": "b7615fcfda551037a6468da2b463ee07b93e18f6e24a70525029f69d98121370", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_develop_merchandise_and_assortment_plans_agent.py` and embedded as the fenced Python below (sha256 b7615fcfda551037…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_develop_merchandise_and_assortment_plans_agent.py` first:

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
    "version": '2.0.0',
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
