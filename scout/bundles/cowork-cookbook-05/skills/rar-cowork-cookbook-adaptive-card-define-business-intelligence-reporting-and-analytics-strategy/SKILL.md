---
name: "rar-cowork-cookbook-adaptive-card-define-business-intelligence-reporting-and-analytics-strategy"
description: "Produces a reusable Adaptive Card JSON snapshot of define business intelligence, reporting, and analytics strategy status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_business_intelligence_reporting_and_analytics_strategy", "rar_sha256": "68582217014b5587c92fb737a48e8a724992984bdee998e21c373cc5fa42549a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_define_business_intelligence_reporting_and_analytics_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-define-business-intelligence-reporting-and-analytics-strategy:83b80024f27b781721aa41957bda912478c32b126c33422dbf51bc09b05d1b07", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_define_business_intelligence_reporting_and_analytics_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_define_business_intelligence_reporting_and_analytics_strategy_agent.py` is
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
