---
name: "rar-cowork-cookbook-demo-data-define-business-intelligence-reporting-and-analytics-strategy"
description: "Generates and creates realistic demo records for define business intelligence, reporting, and analytics strategy in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_business_intelligence_reporting_and_analytics_strategy", "rar_sha256": "d5f65d8d6c0601c8d1eab48203db05a9cb880ed4eaa691c76d9314dead4106f8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_define_business_intelligence_reporting_and_analytics_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-define-business-intelligence-reporting-and-analytics-strategy:445efd0dfb557be825b94b40bbc93ca0dc8667cbb99485269467ac53f75c56d8", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_define_business_intelligence_reporting_and_analytics_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_define_business_intelligence_reporting_and_analytics_strategy_agent.py` is
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

Define business intelligence, reporting, and analytics strategy Demo Data Generator — Generates and creates realistic demo records for define business intelligence, reporting, and analytics strategy in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-business-intelligence-reporting-and-analytics-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_define_business_intelligence_reporting_and_analytics_strategy_agent.py` and embedded as the fenced Python below (sha256 d5f65d8d6c0601c8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_define_business_intelligence_reporting_and_analytics_strategy_agent.py` first:

```bash
python3 demo_data_define_business_intelligence_reporting_and_analytics_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_define_business_intelligence_reporting_and_analytics_strategy_agent.py   # or on stdin
python3 demo_data_define_business_intelligence_reporting_and_analytics_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define business intelligence, reporting, and analytics strategy Demo Data Generator — Generates and creates realistic demo records for define business intelligence, reporting, and analytics strategy in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-business-intelligence-reporting-and-analytics-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_define_business_intelligence_reporting_and_analytics_strategy',
    "version": '2.0.0',
    "display_name": 'Define business intelligence, reporting, and analytics strategy Demo Data Generator',
    "description": 'Generates and creates realistic demo records for define business intelligence, reporting, and analytics strategy in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-define-business-intelligence-reporting-and-analytics-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-define-business-intelligence-reporting-and-analytics-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6762a72af83b538e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/define-business-intelligence-reporting-and-analytics-strategy'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-define-business-intelligence-reporting-and-analytics-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataDefineBusinessIntelligenceReportingAndAnalyticsStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDefineBusinessIntelligenceReportingAndAnalyticsStrategy'
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
    print(DemoDataDefineBusinessIntelligenceReportingAndAnalyticsStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
