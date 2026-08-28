---
name: "rar-cowork-cookbook-demo-data-define-business-intelligence-reporting-and-analytics-strategy"
description: "Generates and creates realistic demo records for define business intelligence, reporting, and analytics strategy in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_business_intelligence_reporting_and_analytics_strategy", "rar_sha256": "3da79834eea63ac618d89c585f4a911f0edde41e1fd5779b8c4244cc847f488e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_define_business_intelligence_reporting_and_analytics_strategy_agent.py` and embedded as the fenced Python below (sha256 3da79834eea63ac6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_define_business_intelligence_reporting_and_analytics_strategy_agent.py` first:

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
    "version": '2.0.1',
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
