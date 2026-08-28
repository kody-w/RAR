---
name: "rar-cowork-cookbook-demo-data-define-business-intelligence-reporting-and-analytics-strategy"
description: "Generates and creates realistic demo records for define business intelligence, reporting, and analytics strategy in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_business_intelligence_reporting_and_analytics_strategy", "rar_sha256": "d5f65d8d6c0601c8d1eab48203db05a9cb880ed4eaa691c76d9314dead4106f8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_define_business_intelligence_reporting_and_analytics_strategy`. The original RAPP
agent is preserved byte-for-byte in `demo_data_define_business_intelligence_reporting_and_analytics_strategy_agent.py` and in the RCI capsule.

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
