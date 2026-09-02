---
name: "rar-cowork-cookbook-adaptive-card-develop-financial-period-strategy"
description: "Produces a reusable Adaptive Card JSON snapshot of develop financial period strategy status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_financial_period_strategy", "rar_sha256": "849e19dcd80e3aa4812464e8fb04cd76ea3400500014ad87ce58bf116fb1580f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_develop_financial_period_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-develop-financial-period-strategy:f43b63b5a3ab0079f44c43a093a5568e68ac3f062c885346f9febf29a0bd279c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_develop_financial_period_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_develop_financial_period_strategy_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_develop_financial_period_strategy_agent.py` and embedded as the fenced Python below (sha256 849e19dcd80e3aa4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_develop_financial_period_strategy_agent.py` first:

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
    "version": '2.0.0',
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
