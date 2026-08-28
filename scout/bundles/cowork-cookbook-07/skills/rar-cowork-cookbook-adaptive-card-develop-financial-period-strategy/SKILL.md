---
name: "rar-cowork-cookbook-adaptive-card-develop-financial-period-strategy"
description: "Produces a reusable Adaptive Card JSON snapshot of develop financial period strategy status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_financial_period_strategy", "rar_sha256": "503213b6f015b2d7dba400b9d56d4ac8424c0af8456fbcc45a5c555948a51c48", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_develop_financial_period_strategy`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_develop_financial_period_strategy_agent.py` and in the RCI capsule.

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

Develop financial period strategy Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of develop financial period strategy status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-financial-period-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_develop_financial_period_strategy_agent.py` and embedded as the fenced Python below (sha256 503213b6f015b2d7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_develop_financial_period_strategy_agent.py` first:

```bash
python3 adaptive_card_develop_financial_period_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_develop_financial_period_strategy_agent.py   # or on stdin
python3 adaptive_card_develop_financial_period_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop financial period strategy Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of develop financial period strategy status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-financial-period-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_develop_financial_period_strategy',
    "version": '2.0.1',
    "display_name": 'Develop financial period strategy Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of develop financial period strategy status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-develop-financial-period-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-develop-financial-period-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '264ce1edbd9bb07c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/develop-financial-period-strategy'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/adaptive-card-develop-financial-period-strategy', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardDevelopFinancialPeriodStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDevelopFinancialPeriodStrategy'
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
    print(AdaptiveCardDevelopFinancialPeriodStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
