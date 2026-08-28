---
name: "rar-cowork-cookbook-adaptive-card-define-business-intelligence-reporting-and-analytics-strategy"
description: "Produces a reusable Adaptive Card JSON snapshot of define business intelligence, reporting, and analytics strategy status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_business_intelligence_reporting_and_analytics_strategy", "rar_sha256": "68582217014b5587c92fb737a48e8a724992984bdee998e21c373cc5fa42549a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_define_business_intelligence_reporting_and_analytics_strategy`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_define_business_intelligence_reporting_and_analytics_strategy_agent.py` and in the RCI capsule.

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

Define business intelligence, reporting, and analytics strategy Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of define business intelligence, reporting, and analytics strategy status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-business-intelligence-reporting-and-analytics-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_define_business_intelligence_reporting_and_analytics_strategy_agent.py` and embedded as the fenced Python below (sha256 68582217014b5587…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_define_business_intelligence_reporting_and_analytics_strategy_agent.py` first:

```bash
python3 adaptive_card_define_business_intelligence_reporting_and_analytics_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_define_business_intelligence_reporting_and_analytics_strategy_agent.py   # or on stdin
python3 adaptive_card_define_business_intelligence_reporting_and_analytics_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define business intelligence, reporting, and analytics strategy Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of define business intelligence, reporting, and analytics strategy status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-business-intelligence-reporting-and-analytics-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_define_business_intelligence_reporting_and_analytics_strategy',
    "version": '2.0.0',
    "display_name": 'Define business intelligence, reporting, and analytics strategy Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of define business intelligence, reporting, and analytics strategy status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'adaptive-card-define-business-intelligence-reporting-and-analytics-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-define-business-intelligence-reporting-and-analytics-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd552dae8cdc9ebe9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/define-business-intelligence-reporting-and-analytics-strategy'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-define-business-intelligence-reporting-and-analytics-strategy', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AdaptiveCardDefineBusinessIntelligenceReportingAndAnalyticsStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDefineBusinessIntelligenceReportingAndAnalyticsStrategy'
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
    print(AdaptiveCardDefineBusinessIntelligenceReportingAndAnalyticsStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
