---
name: "rar-cowork-cookbook-demo-data-forecast-cash-flow"
description: "Generates and creates realistic demo records for forecast cash flow in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_forecast_cash_flow", "rar_sha256": "f0a6f1df0475af160714b3f1916858e094ed5305e22996303c45dce701426667", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_forecast_cash_flow_agent.py` and embedded as the fenced Python below (sha256 f0a6f1df0475af16…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_forecast_cash_flow_agent.py` first:

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
    "version": '2.0.0',
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
