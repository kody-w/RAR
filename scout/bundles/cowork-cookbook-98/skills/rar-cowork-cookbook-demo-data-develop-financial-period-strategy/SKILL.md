---
name: "rar-cowork-cookbook-demo-data-develop-financial-period-strategy"
description: "Generates and creates realistic demo records for develop financial period strategy in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_financial_period_strategy", "rar_sha256": "ffbb2bde0bcf60d2fb46a8ebd856ae5a0abda1d54b4037af105038737424cf54", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_develop_financial_period_strategy_agent.py` and embedded as the fenced Python below (sha256 ffbb2bde0bcf60d2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_develop_financial_period_strategy_agent.py` first:

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
    "version": '2.0.1',
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
