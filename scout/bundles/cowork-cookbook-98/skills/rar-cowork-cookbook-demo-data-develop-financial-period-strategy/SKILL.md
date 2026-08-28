---
name: "rar-cowork-cookbook-demo-data-develop-financial-period-strategy"
description: "Generates and creates realistic demo records for develop financial period strategy in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_financial_period_strategy", "rar_sha256": "f792f809cd025f62da0e42bb27ce13f907df0f6b989420c0f557b49523f4d00a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_develop_financial_period_strategy`. The original RAPP
agent is preserved byte-for-byte in `demo_data_develop_financial_period_strategy_agent.py` and in the RCI capsule.

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

Develop financial period strategy Demo Data Generator — Generates and creates realistic demo records for develop financial period strategy in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-financial-period-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_develop_financial_period_strategy_agent.py` and embedded as the fenced Python below (sha256 f792f809cd025f62…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_develop_financial_period_strategy_agent.py` first:

```bash
python3 demo_data_develop_financial_period_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_develop_financial_period_strategy_agent.py   # or on stdin
python3 demo_data_develop_financial_period_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop financial period strategy Demo Data Generator — Generates and creates realistic demo records for develop financial period strategy in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-financial-period-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_develop_financial_period_strategy',
    "version": '2.0.0',
    "display_name": 'Develop financial period strategy Demo Data Generator',
    "description": 'Generates and creates realistic demo records for develop financial period strategy in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-develop-financial-period-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-develop-financial-period-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7d86657c98515fb2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/develop-financial-period-strategy'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/demo-data-develop-financial-period-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataDevelopFinancialPeriodStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDevelopFinancialPeriodStrategy'
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
    print(DemoDataDevelopFinancialPeriodStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
