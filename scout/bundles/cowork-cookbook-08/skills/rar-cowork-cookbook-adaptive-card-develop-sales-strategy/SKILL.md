---
name: "rar-cowork-cookbook-adaptive-card-develop-sales-strategy"
description: "Produces a reusable Adaptive Card JSON snapshot of develop sales strategy status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_sales_strategy", "rar_sha256": "c23ffff6036606310d0c0a83601b15c4988acb0cd961effd04ea3d783c78fabb", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_develop_sales_strategy`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_develop_sales_strategy_agent.py` and in the RCI capsule.

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

Develop sales strategy Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of develop sales strategy status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-sales-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_develop_sales_strategy_agent.py` and embedded as the fenced Python below (sha256 c23ffff603660631…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_develop_sales_strategy_agent.py` first:

```bash
python3 adaptive_card_develop_sales_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_develop_sales_strategy_agent.py   # or on stdin
python3 adaptive_card_develop_sales_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop sales strategy Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of develop sales strategy status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-sales-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_develop_sales_strategy',
    "version": '2.0.1',
    "display_name": 'Develop sales strategy Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of develop sales strategy status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-develop-sales-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-develop-sales-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '77068d7b46c48b37',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/develop-sales-strategy'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/adaptive-card-develop-sales-strategy', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardDevelopSalesStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDevelopSalesStrategy'
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
    print(AdaptiveCardDevelopSalesStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
