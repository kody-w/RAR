---
name: "rar-cowork-cookbook-adaptive-card-develop-merchandise-and-assortment-plans"
description: "Produces a reusable Adaptive Card JSON snapshot of develop merchandise and assortment plans status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_merchandise_and_assortment_plans", "rar_sha256": "b7615fcfda551037a6468da2b463ee07b93e18f6e24a70525029f69d98121370", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_develop_merchandise_and_assortment_plans_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-develop-merchandise-and-assortment-plans:8924f432990331e18ae8004b28ef879b23b66f57f0bf713e842eeab7b5f9dd16", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_develop_merchandise_and_assortment_plans`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_develop_merchandise_and_assortment_plans_agent.py` is
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
