---
name: "rar-cowork-cookbook-demo-data-forecast-cash-flow"
description: "Generates and creates realistic demo records for forecast cash flow in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_forecast_cash_flow", "rar_sha256": "3151acb8d2a8b0bfb31317cfa462c25e51242c2c505f674cd25bfcce735ee3c2", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_forecast_cash_flow`. The original RAPP
agent is preserved byte-for-byte in `demo_data_forecast_cash_flow_agent.py` and in the RCI capsule.

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

Forecast cash flow Demo Data Generator — Generates and creates realistic demo records for forecast cash flow in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-forecast-cash-flow
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_forecast_cash_flow_agent.py` and embedded as the fenced Python below (sha256 3151acb8d2a8b0bf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_forecast_cash_flow_agent.py` first:

```bash
python3 demo_data_forecast_cash_flow_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_forecast_cash_flow_agent.py   # or on stdin
python3 demo_data_forecast_cash_flow_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Forecast cash flow Demo Data Generator — Generates and creates realistic demo records for forecast cash flow in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-forecast-cash-flow
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_forecast_cash_flow',
    "version": '2.0.1',
    "display_name": 'Forecast cash flow Demo Data Generator',
    "description": 'Generates and creates realistic demo records for forecast cash flow in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-forecast-cash-flow',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-forecast-cash-flow',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd828a9f6ae88ed63',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-cash/forecast-cash-flow'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/demo-data-forecast-cash-flow', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataForecastCashFlow(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataForecastCashFlow'
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
    print(DemoDataForecastCashFlow().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
